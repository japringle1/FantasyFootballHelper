import json
from unittest import TestCase
from scraper.Scraper import restructureFixtureData


class ScraperTest(TestCase):
    def test_givenEmptyFixtureList_whenRestructured_thenNewFixtureListIsEmpty(self):
        playerData = json.loads("{"
                                "\"fixture_history\":{\"all\":[],\"summary\":[]}"
                                "}")
        newList = restructureFixtureData(playerData)
        self.assertEquals(len(newList), 0)


    def givenFixtureListWithOneFixture_whenRestructured_thenNewFixtureListIsCorrectlyRestructures(self):
        playerData = json.loads("{"
                                "\"fixture_history\":{"
                                "   \"all\":["
                                "       [\"10 Aug 20:00\",1,\"WBA(A) 3-0\",28,0,0,0,0,0,0,0,0,0,0,0,9,-2,0,130,1]"
                                "   ],"
                                "   \"summary\":[]}"
                                "}")
        newList = restructureFixtureData(playerData)
        self.assertEquals(len(newList), 1)


