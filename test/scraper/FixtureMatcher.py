__author__ = 'Jonny'


class FixtureMatcher(object):
    def __init__(self, fixture):
        self.fixture = fixture

    def hasDate(self, date):
        assert date == self.fixture["date"]
        return self

    def hasOpposition(self, opposition):
        assert opposition == self.fixture["opposition"]
        return self

    def hasHomeAway(self, homeAway):
        assert homeAway == self.fixture["home_away"]
        return self

    def hasTeamGoalsScored(self, teamGoalsScored):
        assert teamGoalsScored == self.fixture["team_goals_scored"]
        return self

    def hasMinutesPlayed(self, minutesPlayed):
        assert minutesPlayed == self.fixture["mins_played"]
        return self

    def hasPpi(self, ppi):
        assert ppi == self.fixture["ppi"]
        return self

    def hasBps(self, bps):
        assert bps == self.fixture["bps"]
        return self

    def hasValue(self, value):
        assert value == self.fixture["value"]
        return self

    def hasPoints(self, points):
        assert points == self.fixture["points"]
        return self

    def hasGoalsScored(self, goalsScored):
        assert goalsScored == self.fixture["goals"]
        return self

    def hasNetTransfers(self, netTransfers):
        assert netTransfers == self.fixture["net_transfers"]
        return self

    def hasAssists(self, assists):
        assert assists == self.fixture["assists"]
        return self

    def hasCleanSheets(self, cleanSheets):
        assert cleanSheets == self.fixture["clean_sheet"]
        return self

    def hasGoalsConceded(self, goalsConceded):
        assert goalsConceded == self.fixture["goals_conceded"]
        return self

    def hasOwnGoals(self, ownGoals):
        assert ownGoals == self.fixture["own_goals"]
        return self

    def hasPensSaved(self, pensSaved):
        assert pensSaved == self.fixture["pens_saved"]
        return self

    def hasPensMissed(self, pensMissed):
        assert pensMissed == self.fixture["pens_missed"]
        return self

    def hasYellows(self, yellows):
        assert yellows == self.fixture["yellows"]
        return self

    def hasReds(self, reds):
        assert reds == self.fixture["reds"]
        return self

    def hasSaves(self, saves):
        assert saves == self.fixture["saves"]
        return self

    def hasBonus(self, bonus):
        assert bonus == self.fixture["bonus"]
        return self
