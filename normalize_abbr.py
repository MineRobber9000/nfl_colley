# convenience mappings so teams use their actual abbreviations
# first the current teams, then some older team name/abbreviation pairs so you
# can use whatever season you want
TEAMS = dict(
	NWE="NE",
	KAN="KC",
	GNB="GB",
	NOR="NO",
	TAM="TB",
	SFO="SF",
	SDC="SD"
)

normal_abbr = lambda abbr: TEAMS.get(abbr,abbr)
