from game_objects import Player
from game_server import OneNight
from roles import Werewolf, Seer, Villager, Mason, Minion, Robber

if __name__ == "__main__":
    _roles = [Werewolf(), Werewolf(), Minion(), Seer(), Robber(), Mason(), Mason(),
              Villager()]
    _players = [Player("Player{}".format(i)) for i in range(1, len(_roles) + 1)]
    game = OneNight(_players, _roles)
    game.run()

# Roles should all inherit Role, in a flat hierarchy. With only one abstract method: play
# Players should have ids, which will be used in voting and other referencing instead of name
# The game end should be somehow dependent upon the current participating roles.
# Input and output should be decoupled from the core BL.
# Async streams should be used as message buses in both communication directions.
