# You have to implement 3 classes, School, Team, and Player, such that an instance of a School 
# should contain instances of Team objects. Similarly, a Team object can contain instances of Player class.
# The Player class should have three properties that will be set using an initializer:

# ID
# name
# teamName

# The Team class will have two properties that will be set using an initializer:
# name
# players: a list with player class objects in it
# It will have two methods:
# addPlayer(), which will add new player objects in the players list
# getNumberOfPlayers(), which will return the total number of players in the players list

# The School class will contain two properties that will be set using an initializer:

# teams, a list of team class objects
# name
# It will have two methods:

# addTeam, which will add new team objects in the teams list
# getTotalPlayersInSchool(), which will count the total players in all of the teams in the School and return the count

# My solution

class Player:
    def __init__(self, ID=None, name=None, teamName=None):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:
    def __init__(self, name=None):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)


class School:
    def __init__(self, name=None):
        self.teams = []
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        total = 0
        for n in self.teams:
            total += n.getNumberOfPlayers()
        return total

       
# Educative solution was equivalent.    
