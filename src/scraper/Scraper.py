import urllib2
import json
import re

from constants import MyConstants
from constants.MyConstants import FIXTURE_KEY_MAP, PLAYER_COLLECTION


def scrapePlayerData():
    players = []
    index = 1
    errorFlag = False
    print "Scraping...\n"

    while not errorFlag:
        try:
            jsonData = urllib2.urlopen('http://fantasy.premierleague.com/web/api/elements/%d/' % (index))
            playerData = json.load(jsonData)
            players.append(formatPlayer(playerData))
            printScrapingMessage(playerData)
            index += 1
        except ValueError:
            print str(index) + " wasn't a valid JSON."
        except urllib2.URLError:
            errorFlag = True
    print str(len(players)) + " players scraped.\n"

    populateCollection(players)
    return players


def formatPlayer(playerData):
    addLastSeasonsPoints(playerData)

    newFixtureList = restructureFixtureData(playerData)

    newFixtures = {}
    for fixture in newFixtureList:
        gameweek = str(fixture["gw"])
        del fixture["gw"]
        if gameweek not in newFixtures:
            newFixtures[gameweek] = []
        newFixtures[gameweek].append(fixture)

        processGameweekResult(fixture)

    playerData["fixture_history"] = newFixtures

    return playerData


def restructureFixtureData(playerData):
    del playerData["fixture_history"]["summary"]
    newFixtureList = []
    for fixture in playerData["fixture_history"]["all"][:-1]:
        fixtureData = {}
        for key in FIXTURE_KEY_MAP.keys():
            fixtureData[MyConstants.FIXTURE_KEY_MAP[key]] = fixture[key]
        newFixtureList.append(fixtureData)
    return newFixtureList


def processGameweekResult(fixture):
    result = fixture["opponent_result"]
    resultPattern = re.compile("([A-Z]{3})\\((H|A)\\) ([0-9]+)-([0-9]+)")
    resultMatcher = resultPattern.match(result)

    fixture["opposition"] = resultMatcher.group(1)
    fixture["home_away"] = resultMatcher.group(2)
    fixture["team_goals_scored"] = int(resultMatcher.group(3))
    del fixture["opponent_result"]


def addLastSeasonsPoints(playerData):
    if len(playerData["season_history"]) > 0:
        playerData["last_seasons_points"] = playerData["season_history"][-1][-1]
    else:
        playerData["last_seasons_points"] = 0


def printScrapingMessage(playerData):
    print "Scraped " + playerData["web_name"] + " from " + playerData["team_name"]


def populateCollection(players):
    print "Inserting into database..."
    PLAYER_COLLECTION.remove()
    for player in players:
        PLAYER_COLLECTION.insert(player)
