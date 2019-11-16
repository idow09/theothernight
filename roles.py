from containers import Interfaces
from game_objects import Role


class Doppelganger(Role):
    def __init__(self) -> None:
        super().__init__("Doppelganger", 1)

    def action_request(self):
        pass

    def play_action(self, action, players):
        pass


class Werewolf(Role):
    def __init__(self) -> None:
        super().__init__("Werewolf", 2)

    def play(self, players):
        super().play(players)
        other_werewolves = list(
            filter(lambda p: p is not self.player, filter(lambda p: p.current_role_name is "Werewolf", players)))
        print("Your companion werewolf is: {}".format(other_werewolves[0].name))


class Minion(Role):
    def __init__(self) -> None:
        super().__init__("Minion", 3)

    def play(self, players):
        super().play(players)
        werewolves = list(filter(lambda p: p.current_role_name is "Werewolf", players))
        print("The werewolves are: {} and {}".format(werewolves[0].name, werewolves[1].name))


class Mason(Role):
    def __init__(self) -> None:
        super().__init__("Mason", 4)

    def play(self, players):
        super().play(players)
        other_masons = list(
            filter(lambda p: p is not self.player, filter(lambda p: p.current_role_name is "Mason", players)))
        print("Your companion mason is: {}".format(other_masons[0].name))


class Seer(Role):
    def __init__(self) -> None:
        super().__init__("Seer", 5)

    def play(self, players):
        super().play(players)
        p = Interfaces.console_ui().pick_from_list(players, "Please choose the player you want to check on.")
        print("{} is a {}".format(p.name, p.current_role_name))


class Robber(Role):
    def __init__(self) -> None:
        super().__init__("Robber", 6)

    def play(self, players):
        super().play(players)
        p = Interfaces.console_ui().pick_from_list(players, "Please choose the player you want to rob from.")
        print("You took {} from {}".format(p.current_role_name, p.name))
        self.player.current_role_name = p.current_role_name
        p.current_role_name = self.name


class Troublemaker(Role):
    def __init__(self) -> None:
        super().__init__("Troublemaker", 7)

    def play(self, players):
        super().play(players)
        p_l = Interfaces.console_ui().pick_from_list(players, "Please choose the players you want to swap.", count=2)
        print("Swapped.")
        p1, p2 = p_l[0], p_l[1]
        temp = p1.current_role_name
        p1.current_role_name = p2.current_role_name
        p2.current_role_name = temp


class Insomniac(Role):
    def __init__(self) -> None:
        super().__init__("Insomniac", 8)

    def play(self, players):
        super().play(players)
        print("Your current role is: {}".format(self.player.current_role_name))


class Villager(Role):
    def __init__(self) -> None:
        super().__init__("Villager", 10)
