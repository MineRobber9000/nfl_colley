import csv, abbr2team, sys
assert len(sys.argv)==3,"usage: generate_partial_rankings.py <games.csv> <week>"
from Colley import *

def adjust_ot(notes):
	if notes=="OT":
		return 0.75
	return 1

week = int(sys.argv[2])

with open(sys.argv[1]) as f: games = [row[1:] for row in csv.reader(f) if int(row[0])<=week]

c = Colley(games)
rankings = c.process(weight_fn=adjust_ot,use_margin=True)

for i,t in enumerate(rankings,1):
	team,score = t
	print("#{!s} {} (rating: {:.06f})".format(i,abbr2team.team_name(team),score))

with open("rankings.part.csv","w") as f: csv.writer(f).writerows([[i]+list(ranking) for i,ranking in enumerate(rankings,1)])
