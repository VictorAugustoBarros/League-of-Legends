from models.api import Api
from models.player import Player


class ApiController:
    def __init__(self, api_key: str):
        self.api = Api(api_key=api_key)

    def get_summoner_data_by_name(self, username: str) -> Player:
        player_data = self.api.summoner_by_name(username)
        player = Player(id_player=player_data.get("id"), account_id=player_data.get("accountId"),
                        puuid=player_data.get("puuid"), level=player_data.get("summonerLevel"))
        return player

    def get_top_5_players_br(self):
        players_top = []
        top_5 = self.api.top_5_players()
        for count, player in enumerate(top_5['players']):
            if count == 5:
                break

            players_top.append({
                "rank": player.get("rank") + 1,
                "name": player.get("name")
            })

        return players_top

    def get_masteries_champions(self, id_player: int, champions: dict, limit):
        maestrias = {}
        champions_masteries = self.api.masteries_champions(id_summoner=id_player)
        for count, masterie in enumerate(champions_masteries):
            if count == limit:
                break

            campeao = champions[masterie['championId']]
            maestrias[campeao.get('name')] = {
                "level": masterie.get("championLevel"),
                "pontos": masterie.get("championPoints"),
                "Bau Disponivel": "não" if masterie.get("chestGranted") else "sim",
            }
        return maestrias

    def get_champions(self):
        champions_list = {}
        champions = self.api.get_champions_list()
        for nm_champion, champion in champions['data'].items():
            champions_list[int(champion.get('key'))] = champion
        return champions_list
