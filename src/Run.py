from scraper.Scraper import scrapePlayerData

players = scrapePlayerData()

# Populate database
# myconstants.PLAYER_COLLECTION.remove()
# new_players = scraper.populate_collection(myconstants.PLAYER_COLLECTION, players)

# Run forecasts
# myconstants.FORECASTS_COLLECTION.remove()
# forecast.run_forecasts()

# Run simulation of season
# myconstants.SQUADS_COLLECTION.remove()
# simulation.run_simulation("LG")
# simulation.run_simulation("WA")
# simulation.run_simulation("ES")
