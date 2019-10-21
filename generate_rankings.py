import csv, abbr2team, sys
assert len(sys.argv)==2,"usage: generate_rankings.py <games>"
from Colley import *

def adjust_ot(notes):
	if notes=="OT":
		return 0.75
	return 1

with open(sys.argv[1]) as f: games = [row[1:] for row in csv.reader(f)]

c = Colley(games)
rankings = c.process(weight_fn=adjust_ot,use_margin=True)

for i,t in enumerate(rankings,1):
	team,score = t
	print("#{!s} {} (rating: {:.06f})".format(i,abbr2team.team_name(team),score))

with open("rankings.csv","w") as f:
	w=csv.writer(f)
	w.writerow(["Rank","Team","Score"])
	w.writerows([[i,x[0],"{:.06f}".format(round(x[1],6))] for i,x in enumerate(rankings,1)])
