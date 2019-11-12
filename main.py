import random


class OneNight(object):
    def __init__(self, payers, roles) -> None:
        self.players = payers
        self.roles = roles
        self.winner = None

    def run(self):
        self.assign_roles()
        print("Good night... zZzZz")
        for player in self.players_by_play_order():
            player.original_role.play(self.players)
        print("Good Morning!")
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
            player.original_role = role
            player.current_role_name = role.name
            role.player = player

    def calculate_game_results(self):
        votes = {}
        for player in self.players:
            votes[player.vote] = votes.get(player.vote, 0) + 1
        dead_player = max(votes.items(), key=lambda it: it[1])[0]
        if dead_player.current_role_name is "Tanner":
            self.winner = "Tanner"  # TODO
        elif dead_player.current_role_name is "Werewolf":
            self.winner = "Village"  # TODO
        else:
            self.winner = "Werewolves"  # TODO

    def print_results(self):
        print("Game over!")
        print("The winner is/are: {}".format(self.winner))


class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self.original_role = None
        self.current_role_name = None
        self.vote = None

    def __str__(self) -> str:
        return "{}, playing a {}".format(self.name, self.original_role)

    def take_vote(self, players):
        i = input(self.name + " please vote against a player ([1-{}]): ".format(len(players)))
        self.vote = players[int(i) - 1]


class Role(object):
    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.player = None

    def play(self, players):
        print("{}, you're a {}.".format(self.player.name, self.name))


class InfoRole(Role):
    def __init__(self, name, index) -> None:
        super().__init__(name, index)

    def play(self, players):
        super().play(players)
        self.provide_info(players)

    def provide_info(self, players):
        pass


class ActionRole(Role):
    def __init__(self, name, index) -> None:
        super().__init__(name, index)

    def play(self, players):
        super().play(players)
        action = input(self.action_request())
        self.play_action(action, players)

    def action_request(self):
        pass

    def play_action(self, action, players):
        pass  # TODO : force subclasses to implement


class DoppelgangerRole(ActionRole):
    def __init__(self) -> None:
        super().__init__("Doppelganger", 1)

    def action_request(self):
        pass

    def play_action(self, action, players):
        pass


class WerewolfRole(InfoRole):
    def __init__(self) -> None:
        super().__init__("Werewolf", 2)  # "You're a werewolf with ???"

    def provide_info(self, players):
        pass


class MinionRole(InfoRole):
    def __init__(self) -> None:
        super().__init__("Minion", 3)

    def provide_info(self, players):
        pass


class MasonRole(InfoRole):
    def __init__(self) -> None:
        super().__init__("Mason", 4)

    def provide_info(self, players):
        other_masons = list(filter(lambda p: p is not self.player, filter(lambda p: p.current_role_name is "Mason", players)))
        print("Your companion mason is: {}".format(other_masons[0].name))


class SeerRole(ActionRole):
    def __init__(self) -> None:
        super().__init__("Seer", 5)  # "You're a seer. Choose whom to look at: "

    def action_request(self):
        return "Please choose the player you want to check on: "

    def play_action(self, action, players):
        p = players[int(action) - 1]
        print("{} is a {}".format(p.name, p.current_role_name))


class VillagerRole(Role):
    def __init__(self) -> None:
        super().__init__("Villager", 10)


if __name__ == "__main__":
    _players = [Player("player1"), Player("player2"), Player("player3"), Player("player4"), Player("player5")]
    _roles = [WerewolfRole(), SeerRole(), VillagerRole(), MasonRole(), MasonRole()]
    game = OneNight(_players, _roles)
    game.run()

# Roles should all inherit Role, in a flat hierarchy. With only one abstract method: play
# Players should have ids, which will be used in voting and other referencing instead of name
# The game end should be somehow dependent upon the current participating roles.
# Input and output should be decoupled from the core BL.
# Async streams should be used as message buses in both communication directions.
