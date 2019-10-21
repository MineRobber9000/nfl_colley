# convenience mappings so teams show up as their names and not abbreviations
# first the current teams, then some older team name/abbreviation pairs so you
# can use whatever season you want
TEAMS = dict(
	NE="New England Patriots",
	BUF="Buffalo Bills",
	NYJ="New York Jets",
	MIA="Miami Dolphins",
	BAL="Baltimore Ravens",
	PIT="Pittsburgh Steelers",
	CLE="Cleveland Browns",
	CIN="Cincinnati Bengals",
	HOU="Houston Texans",
	IND="Indianapolis Colts",
	JAX="Jacksonville Jaguars",
	TEN="Tennessee Titans",
	KC="Kansas City Chiefs",
	OAK="Oakland Raiders",
	LAC="Los Angeles Chargers",
	DEN="Denver Broncos",
	DAL="Dallas Cowboys",
	PHI="Philadelphia Eagles",
	NYG="New York Giants",
	WAS="Washington Redskins",
	GB="Green Bay Packers",
	MIN="Minnesota Vikings",
	CHI="Chicago Bears",
	DET="Detroit Lions",
	NO="New Orleans Saints",
	CAR="Carolina Panthers",
	TB="Tampa Bay Buccaneers",
	ATL="Atlanta Falcons",
	SF="San Francisco 49ers",
	SEA="Seattle Seahawks",
	LAR="Los Angeles Rams",
	ARI="Arizona Cardinals",
	SD="San Diego Chargers",
	STL="Saint Louis Rams"
)

team_name = lambda abbr: TEAMS.get(abbr,abbr)
