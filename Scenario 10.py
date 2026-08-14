class Player:
    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def categorize(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("\nCricket Team Player Details")
        print("---------------------------")

        for player in self.players:
            print("Player Name  :", player.name)
            print("Jersey No.   :", player.jersey_number)
            print("Runs         :", player.runs)
            print("Category     :", player.categorize())
            print("---------------------------")


team = Team()

n = int(input("Enter number of players: "))

for i in range(n):
    print("\nEnter details of Player", i + 1)
    name = input("Player Name: ")
    jersey_number = int(input("Jersey Number: "))
    runs = int(input("Runs: "))

    player = Player(name, jersey_number, runs)
    team.add_player(player)

team.display_players()