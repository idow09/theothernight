import random


class OneNight(object):
    def __init__(self, payers, roles) -> None:
        self.dead_player = None
        self.players = payers
        self.roles = roles
        self.winner = None

    def run(self):
        self.assign_roles()
        print("=== Good night... zZzZz ===")
        for player in self.players_by_play_order():
            player.original_role.play(self.players)
        print("=== Good Morning! ===")
        print("You have 5 minutes. You can chat freely.")
        # TODO: Chat, timer...
        for player in self.players:
            player.take_vote(self.players)
        self.calculate_game_results()
        self.print_results()

    def players_by_play_order(self):
        return sorted(self.players, key=lambda p: p.original_role.index)

    def assign_roles(self):
        print("Assigning roles")
        for player, role in zip(self.players, random.sample(self.roles, len(self.roles))):
            player.assign(role)

    def calculate_game_results(self):
        votes = {}
        for player in self.players:
            votes[player.vote] = votes.get(player.vote, 0) + 1
        dead_player = max(votes.items(), key=lambda it: it[1])[0]
        self.dead_player = dead_player
        if dead_player.current_role_name is "Tanner":
            self.winner = "Tanner"  # TODO
        elif dead_player.current_role_name is "Werewolf":
            self.winner = "Village"  # TODO
        else:
            self.winner = "Werewolves"  # TODO

    def print_results(self):
        print("Game over!")
        print("The village have decided, and {} was hung.".format(self.dead_player))
        print("{} was a {}".format(self.dead_player, self.dead_player.current_role_name))
        print("The winner(s) is/are: {}".format(self.winner))
