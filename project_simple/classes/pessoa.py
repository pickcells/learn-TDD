class Pessoa:
    def __init__(self):
        self.__name = ""
        self.birth_year = 0
        self.__weight = 0.0

    @property
    def get_name(self):
        return self.__name

    @property
    def get_birth_year(self):
        return self.birth_year

    @property
    def get_weight(self):
        return self.__weight

    def set_name(self, name):
        self.__name = name

    def set_birth_year(self, age):
        self.birth_year = age

    def set_weight(self, weight):
        self.__weight = weight

    #functions
    def calculate_age(self, act_year):
        return act_year - self.birth_year
    
    def remainder_to_goal_weight(self, goal_weight):
        return goal_weight - self.__weight
    
    def __str__(self):
        return "Name: {}, Birth Year: {}, Weight: {}".format(self.__name, self.birth_year, self.__weight)
