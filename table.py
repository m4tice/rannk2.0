class Table:

    def __init__(self):
        self.__table = {}

    def addEntry(self, match_result):
        """
        add points and goal differences for teams to table based on a single match
        """
        for entry in match_result:
            team_name, point, gd = entry

            if team_name in self.__table:
                self.__table[team_name]['point'] += point
                self.__table[team_name]['gd'] += gd
            else:
                self.__table[team_name] = {'point': point, 'gd': gd, 'rank': 0}

    def sort_table(self):
        """
        Sort table based on points, goal differences and Team's initial letter
        """

        sorted_table = dict(sorted(self.__table.items(),
                                   key=lambda item: (item[1]['point'], item[1]['gd'], item[0][0]),
                                   reverse=True))
        self.__table = sorted_table

    def rank_table(self):
        """
        Add rank to teams based on their points
        """

        keys = list(self.__table.keys())
        for idx, (item, team) in enumerate(zip(self.__table.items(), keys)):

            # assign rank for the first team
            if item[0] == keys[0]:
                item[1]['rank'] = 1

            # if the point of the current team equal to the previous team's, assign the same rank
            elif item[1]['point'] == self.__table[keys[idx - 1]]['point']:
                item[1]['rank'] = self.__table[keys[idx - 1]]['rank']

            else:
                item[1]['rank'] = idx + 1

    def getTableDict(self):
        return self.__table
