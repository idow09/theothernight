from game_objects import Role


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
        super().__init__("Werewolf", 2)

    def provide_info(self, players):
        other_werewolves = list(
            filter(lambda p: p is not self.player, filter(lambda p: p.current_role_name is "Werewolf", players)))
        print("Your companion werewolf is: {}".format(other_werewolves[0].name))


class MinionRole(InfoRole):
    def __init__(self) -> None:
        super().__init__("Minion", 3)

    def provide_info(self, players):
        werewolves = list(filter(lambda p: p.current_role_name is "Werewolf", players))
        print("The werewolves are: {} and {}".format(werewolves[0].name, werewolves[1].name))


class MasonRole(InfoRole):
    def __init__(self) -> None:
        super().__init__("Mason", 4)

    def provide_info(self, players):
        other_masons = list(
            filter(lambda p: p is not self.player, filter(lambda p: p.current_role_name is "Mason", players)))
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
