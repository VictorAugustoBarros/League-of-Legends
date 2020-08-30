import sys

from controller.api_controller import ApiController
from utils.constant import API_KEY, NOME_PLAYER, LIMIT_CAMPEOES_MAESTRIA


def main():
    api_controller = ApiController(api_key=API_KEY)

    # top_5_br = api_controller.get_top_5_players_br()
    # print("TOP 5 Americas")
    # for player in top_5_br:
    #     print("[%s] %s" % (player['rank'], player['name']))

    print("------------------------------------------------------------------------------")

    player = api_controller.get_summoner_data_by_name(username=NOME_PLAYER)
    if not player:
        print("Player não existe")
        sys.exit(0)

    print("[%s]" % NOME_PLAYER)
    print("ID: %s" % player.id_player)
    print("Level: %s" % player.level)

    champions = api_controller.get_champions()

    masteries_champions = api_controller.get_masteries_champions(id_player=player.id_player, champions=champions,
                                                                 limit=LIMIT_CAMPEOES_MAESTRIA)
    print("\n[Top %s Maestrias]" % LIMIT_CAMPEOES_MAESTRIA)
    for nome, dados in masteries_champions.items():
        print("%s -> %s" % (nome, dados))


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
