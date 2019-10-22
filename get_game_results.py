import requests,json,csv
from bs4 import BeautifulSoup
from time import sleep

URL = "https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min={year}&year_max={year}&game_type={type}&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&game_location=H&c5val=1.0&order_by=game_date&order_by_asc=Y"

def get(year,include_postseason=False,offset=None):
	u=URL.format(year=year,type="E" if include_postseason else "R")
	if offset is not None:
		u+="&offset={!s}".format(offset)
	r=requests.get(u)
	r.raise_for_status()
	return BeautifulSoup(r.content,"html.parser")

def soup2csv(soup):
	table = soup.table
	if not table: return []
	rows = table.findAll("tr")
	out = []
	for row in rows:
		cells = row.findAll("th")+row.findAll("td")
		out_row = []
		for cell in cells:
			out_row.append(cell.text)
		out.append(out_row)
	# I know the first row is empty, so I can ignore it.
	out.pop(0)
	return out

def _header_sort(x):
	try:
		if x[0]=="Rk":
			return 0
		return int(x[0])
	except:
		print(x)
		return 0

def uniq(l):
	s=set()
	[s.add(json.dumps(i)) for i in l if json.dumps(i) not in s]
	return [json.loads(x) for x in s]

def getyear(year,include_postseason=False):
	print("Loading page 1...")
	soup = get(year,include_postseason)
	out = soup2csv(soup)
	page = 1
	while soup.find("a",{"class":"next"}): # next page
		print("Page {!s} finished!".format(page))
		print("Loading page {!s}...".format(page+1))
		sleep(3) # 3 seconds sleep (about how long it takes me to scroll to the bottom of the page IRL)
		soup = get(year,include_postseason,offset=(page*100))
		page+=1
		out.extend(soup2csv(soup))
	out=uniq(out)
	out.sort(key=_header_sort)
	return out

from datetime import date

def get_season(y,m,d):
	if m<2: # latest a SB has occurred is February...
		return y-1
	elif m==2 and d<=7: # ...7th.
		return y-1
	else:
		return y

def get_this_season():
	today=date.today()
	return get_season(today.year,today.month,today.day)

import argparse
if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Gets game results from Pro-Football-Reference.")
	parser.add_argument("-p","--postseason",action="store_true",help="Include postseason games.")
	parser.add_argument("year",nargs="?",default=get_this_season(),type=int,help="The season from which you get your games.")
	args = parser.parse_args()
	out = getyear(args.year,args.postseason)
	with open("results.csv","w") as f:
		w = csv.writer(f)
		w.writerows(out)
