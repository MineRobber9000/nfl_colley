# nfl_colley

Calculates the Colley Matrix rankings of the NFL.

`Colley.py` is copyright 2014 Eugene Bulkin, licensed under MIT.

## Method

For a season of NFL games as returned by Pro-Football-Reference:

1. All tie games are discarded. The Colley Matrix library I'm using has no 
contingency for tie games.
2. The team abbreviations are normalized. Pro-Football-Reference has an 
obsession with making sure that team abbreviations are 3 characters long, so we 
trim the ones that need to be trimmed.
3. The final `games.csv` is organized as such: `Week,Winner abbreviation,Winner 
score,Loser abbreviation,Loser score,OT`
4. The Colley method is ran on these games. Overtime is counted as .75 of a 
game.
5. The finalized rankings are output.

By default, postseason games are excluded. They can be added by supplying the 
`-p` flag to `get_game_results.py`.

## Workflow for NFL season rankings:

Run:

```
python get_game_results.py
python results_to_games.py
python generate_rankings.py games.csv
```

The rankings in CSV form are in `rankings.csv`.
