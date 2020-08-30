from models.request import Request


class Api(Request):
    def __init__(self, api_key):
        super().__init__(api_key)

    def summoner_by_name(self, username: str) -> dict:
        """
            Pesquisa os dados básicos referente ao jogador *username*
        :param username:
        :return:
        """
        method = "/lol/summoner/v4/summoners/by-name/%s" % username
        resp = self.do_request_br(method=method)
        return resp

    def top_5_players(self) -> dict:
        """
            Pesquisa o top 5 players da america
        :return:
        """
        method = "/lor/ranked/v1/leaderboards"
        resp = self.do_request_america(method=method)
        return resp

    def masteries_champions(self, id_summoner: int) -> dict:
        """
            Pesquisa todas as maestria dos campeões
        :return:
        """

        method = "/lol/champion-mastery/v4/champion-masteries/by-summoner/%s" % id_summoner
        resp = self.do_request_br(method=method)
        return resp

    def get_champions_list(self):
        url = "http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json"
        resp = self.do_get_request(url=url)
        return resp
