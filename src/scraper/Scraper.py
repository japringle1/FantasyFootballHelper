import urllib2
import json

from constants import MyConstants
from constants.FplJsonKeyNames import LAST_SEASONS_POINTS, WEB_NAME, SEASON_HISTORY, TEAM_NAME
from constants.MyConstants import FIXTURE_KEY_MAP


def scrapePlayerData():
    players = []
    index = 1
    errorFlag = False
    print "Scraping...\n"

    while not errorFlag:
        try:
            jsonData = urllib2.urlopen('http://fantasy.premierleague.com/web/api/elements/%d/' % (index))
            playerData = json.load(jsonData)
            printScrapingMessage(playerData)
            players.append(formatPlayer(playerData))
            index += 1
        except ValueError:
            print str(index) + " wasn't a valid JSON."
        except urllib2.URLError:
            errorFlag = True
    print str(len(players)) + " players scraped.\n"
    return players


def formatPlayer(playerData):
    addLastSeasonsPoints(playerData)

    newFixtureList = restructureFixtureData(playerData)

    all_fixtures = {}

    last_gw = 0

    # Handle double gameweeks
    for fixture in newFixtureList:
        if (fixture["gw"] == last_gw):
            duplicate = all_fixtures[str(fixture["gw"])]
            fixtures = [duplicate, fixture]
            points = (duplicate["points"] + fixture["points"]) / float(len(fixtures))
            value = fixture["value"]
            mins_played = fixture["mins_played"]
            net_transfers = fixture["net_transfers"]
            opposition_result = fixture["opponent_result"]
            all_fixtures[str(fixture["gw"])] = {"gw": fixture["gw"], "fixtures": fixtures, "points": points,
                                                "value": value, "mins_played": mins_played,
                                                "net_transfers": net_transfers, "opponent_result": opposition_result}
        else:
            all_fixtures[str(fixture["gw"])] = fixture

        last_gw = fixture["gw"]

    playerData["fixture_history"] = all_fixtures

    return playerData


def restructureFixtureData(playerData):
    del playerData["fixture_history"]["summary"]
    newFixtureList = []
    for fixture in playerData["fixture_history"]["all"]:
        fixtureData = {}
        for key in FIXTURE_KEY_MAP.keys():
            fixtureData[MyConstants.FIXTURE_KEY_MAP[key]] = fixture[key]
        newFixtureList.append(fixtureData)
    return newFixtureList


def addLastSeasonsPoints(playerData):
    if len(playerData[SEASON_HISTORY]) > 0:
        playerData[LAST_SEASONS_POINTS] = playerData[SEASON_HISTORY][-1][-1]
    else:
        playerData[LAST_SEASONS_POINTS] = 0


def populateCollection(collection, players):
    for player in players:
        collection.insert(player)


def printScrapingMessage(playerData):
    print "Scraped " + playerData[WEB_NAME] + " from " + playerData[TEAM_NAME]
