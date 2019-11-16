from game_objects import Player
from game_server import OneNight
from roles import Werewolf, Seer, Villager, Mason, Minion, Robber, Troublemaker

if __name__ == "__main__":
    _roles = [Werewolf(), Werewolf(), Minion(), Seer(), Robber(), Troublemaker(), Mason(), Mason(), Villager()]
    _players = [Player("Player{}".format(i)) for i in range(len(_roles))]
    game = OneNight(_players, _roles)
    game.run()

# The game end should be somehow dependent upon the current participating roles.
# Input and output should be decoupled from the core BL.
# Async streams should be used as message buses in both communication directions.
