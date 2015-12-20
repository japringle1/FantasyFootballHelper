import json
from unittest import TestCase

from scraper.Scraper import formatPlayer
from test.scraper.FixtureMatcher import FixtureMatcher


def assertThatFixture(fixture):
    return FixtureMatcher(fixture)


class ScraperTest(TestCase):
    def test_givenEmptyFixtureList_whenRestructured_thenNewFixtureListIsEmpty(self):
        playerData = json.loads("{"
                                "   \"fixture_history\":{\"all\":[],\"summary\":[]},"
                                "   \"season_history\":[]"
                                "}")
        newFixtures = formatPlayer(playerData)["fixture_history"]
        self.assertEquals(len(newFixtures), 0)

    def test_givenFixtureListWithUpcomingFixture_whenRestructured_thenNewFixtureListIsEmpty(self):
        playerData = json.loads("{"
                                "   \"fixture_history\":{"
                                "       \"all\":["
                                "           [\"11 Aug 20:00\",2,\"WBA(A)\",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
                                "           ],"
                                "       \"summary\":[]"
                                "   },"
                                "   \"season_history\":[]"
                                "}")
        newFixtures = formatPlayer(playerData)["fixture_history"]
        self.assertEquals(len(newFixtures), 0)

    def test_givenFixtureListWithOneValidFixture_whenRestructured_thenNewFixtureListIsCorrectlyRestructures(self):
        playerData = json.loads("{"
                                "   \"fixture_history\":{"
                                "       \"all\":["
                                "           [\"10 Aug 20:00\",1,\"WBA(A) 3-0\",28,1,2,3,4,5,6,7,8,9,10,11,9,-2,0,130,1],"
                                "           [\"11 Aug 20:00\",2,\"WBA(A)\",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
                                "       ],"
                                "       \"summary\":[]"
                                "   },"
                                "   \"season_history\":[]"
                                "}")

        newFixtures = formatPlayer(playerData)["fixture_history"]

        self.assertEquals(len(newFixtures["1"]), 1)
        assertThatFixture(newFixtures["1"][0]) \
            .hasDate("10 Aug 20:00") \
            .hasOpposition("WBA") \
            .hasHomeAway("A") \
            .hasTeamGoalsScored(3) \
            .hasMinutesPlayed(28) \
            .hasGoalsScored(1) \
            .hasAssists(2) \
            .hasCleanSheets(3) \
            .hasGoalsConceded(4) \
            .hasOwnGoals(5) \
            .hasPensSaved(6) \
            .hasPensMissed(7) \
            .hasYellows(8) \
            .hasReds(9) \
            .hasSaves(10) \
            .hasBonus(11) \
            .hasPpi(9) \
            .hasBps(-2) \
            .hasNetTransfers(0) \
            .hasValue(130) \
            .hasPoints(1)

    def test_givenFixtureListWithDoubleGameweek_whenRestructured_thenNewFixtureListIsCorrectlyRestructured(self):
        playerData = json.loads("{"
                                "   \"fixture_history\":{"
                                "       \"all\":["
                                "           [\"10 Aug 20:00\",1,\"WBA(A) 3-0\",28,0,0,0,0,0,0,0,0,0,0,0,9,-2,0,130,1],"
                                "           [\"16 Aug 16:00\",1,\"CHE(H) 3-0\",82,1,0,1,0,0,0,0,0,0,0,0,46,26,24104,130,6],"
                                "           [\"11 Aug 20:00\",2,\"WBA(A)\",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
                                "       ],"
                                "       \"summary\":[]"
                                "   },"
                                "   \"season_history\":[]"
                                "}")
        newFixtures = formatPlayer(playerData)["fixture_history"]

        self.assertEquals(len(newFixtures["1"]), 2)
        assertThatFixture(newFixtures["1"][0]) \
            .hasDate("10 Aug 20:00") \
            .hasOpposition("WBA") \
            .hasHomeAway("A") \
            .hasTeamGoalsScored(3) \
            .hasMinutesPlayed(28) \
            .hasGoalsScored(0) \
            .hasPpi(9) \
            .hasBps(-2) \
            .hasNetTransfers(0) \
            .hasValue(130) \
            .hasPoints(1)
        assertThatFixture(newFixtures["1"][1]) \
            .hasDate("16 Aug 16:00") \
            .hasOpposition("CHE") \
            .hasHomeAway("H") \
            .hasTeamGoalsScored(3) \
            .hasMinutesPlayed(82) \
            .hasGoalsScored(1) \
            .hasPpi(46) \
            .hasBps(26) \
            .hasNetTransfers(24104) \
            .hasValue(130) \
            .hasPoints(6)
