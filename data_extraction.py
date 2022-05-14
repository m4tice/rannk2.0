class DataExtraction:

    def __init__(self):
        self.__data = []
        self.__input_file = None

    def __extract_team_info(self, team):
        """
        Extract team name and score from the input information
        """
        # Split the words to get the score and name parts
        team_name_parts = team.split()[:-1]
        team_score = team.split()[-1]

        # Join the name parts to get team name
        team_name = ' '.join(team_name_parts)

        return [team_name, int(team_score)]

    def __extract_match_info(self, match):
        """
        Extract teams' names and scores from the input match
        """
        team1, team2 = match.split(",")
        team1_name, team1_score = self.__extract_team_info(team1)
        team2_name, team2_score = self.__extract_team_info(team2)

        return [[team1_name, team1_score], [team2_name, team2_score]]

    def __extract(self):
        """
        Extract phase: extract data from input text file
        """

        with open(self.__input_file) as f:
            lines = f.readlines()

            for line in lines:
                # Extract match information from each line
                match = self.__extract_match_info(line)
                self.__data.append(match)

    def setFile(self, input_file):
        self.__input_file = input_file

    def getFile(self):
        return self.__input_file

    def getData(self):
        self.__extract()
        return self.__data




