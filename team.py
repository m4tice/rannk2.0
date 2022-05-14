class Team:

    def __init__(self):
        self.__team_name = None
        self.__point = 0
        self.__gd = 0

    def setTeamName(self, team_name):
        self.__team_name = team_name

    def getTeamName(self):
        return self.__team_name

    def setPoint(self, point):
        self.__point = point

    def getPoint(self):
        return self.__point

    def setGD(self, gd):
        self.__gd = gd

    def getGD(self):
        return self.__gd

    def addPoint(self, point):
        self.__point += point

    def addGD(self, gd):
        self.__gd += gd