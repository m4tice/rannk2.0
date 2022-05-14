class Match:

    def __init__(self):
        self.__t1 = None
        self.__t1_goals = None
        self.__t2 = None
        self.__t2_goals = None

    def update_match(self, t1_info, t2_info):
        self.__t1 = t1_info[0]
        self.__t1_goals = t1_info[1]
        self.__t2 = t2_info[0]
        self.__t2_goals = t2_info[1]

    def analyze(self):
        cond1 = self.__t1_goals > self.__t2_goals
        cond2 = self.__t1_goals < self.__t2_goals
        gd = abs(self.__t1_goals - self.__t2_goals)

        if cond1:
            return [[self.__t1, 3, gd], [self.__t2, 0, -gd]]
        elif cond2:
            return [[self.__t1, 0, -gd], [self.__t2, 3, gd]]
        else:
            return [[self.__t1, 1, gd], [self.__t2, 1, gd]]
