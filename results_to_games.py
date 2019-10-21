import csv,sys
assert len(sys.argv) in (1,2),"Usage: results_to_games.py [out]"
from normalize_abbr import normal_abbr

with open("results.csv") as f: results = list(csv.reader(f))

results = [x for x in results if x[0].isdigit()]

out = []
for game in results:
	g = [game[8]]
	home, away = normal_abbr(game[1]), normal_abbr(game[7])
	home_score, away_score = map(int,game[11].split()[-1].split("-"))
	if home_score==away_score: continue # ignore ties
	if home_score>away_score: # home team won
		g.extend([home,home_score,away,away_score])
	else: # away team won
		g.extend([away,away_score,home,home_score])
	g.append(game[-1]) # was the game decided in OT?
	out.append(g)

with open(sys.argv[1] if len(sys.argv)==2 else "games.csv","w") as f:
	w = csv.writer(f)
	w.writerows(out)
