from game_objects import Player
from game_server import OneNight
from roles import WerewolfRole, SeerRole, VillagerRole, MasonRole, MinionRole

if __name__ == "__main__":
    _players = [Player("Player{}".format(i)) for i in range(1, 8)]
    _roles = [WerewolfRole(), WerewolfRole(), MinionRole(), SeerRole(), MasonRole(), MasonRole(), VillagerRole()]
    game = OneNight(_players, _roles)
    game.run()

# Roles should all inherit Role, in a flat hierarchy. With only one abstract method: play
# Players should have ids, which will be used in voting and other referencing instead of name
# The game end should be somehow dependent upon the current participating roles.
# Input and output should be decoupled from the core BL.
# Async streams should be used as message buses in both communication directions.
