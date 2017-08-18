import json, requests
from pprint import pprint
from apps.EPLNews.models import *
from threading import Timer
from time import sleep

SKY_API_BASE = "https://skysportsapi.herokuapp.com"
# API_KEY = "9ynWTXljOQ3Mw4vP7HMEN6ymaHxVydbh1jINFhxv"

SPORTSMONK_API_BASE = "https://soccer.sportmonks.com/api/v2.0/"
SPORTSMONK_API_KEY = "1i6OFOuWKoHGsy5ODzLxEvhBaBYzdp8CW03Y6nVTmLPVB3STb7Y0MRuP2IZx"
ENDPOINT_EPL_STANDING_SPORTSMONT = "standings/season/6397"
ENDPOINT_EPL_PLAYER_STAT = "topscorers/season/6397"
ENDPOINT_EPL_PLATYER_STAT_INCLUDE = "&include=goalscorers.player,%20goalscorers.team,assistscorers.player,assistscorers.team,cardscorers.player,cardscorers.team"
SPORTSMONK_PAYLOAD = { 'api_token': SPORTSMONK_API_KEY}

ENDPOINT_GENERAL_NEWS_SKY = "/sky/getnews/football/v1.0/"
ENDPOINT_TEAM_NEWS_SKY = "/sky/football/getteamnews/{0}/v1.0/"
SKYSPORTS_SOURCE_ID = 1

TRIGGER = True

# DEFAULT_HEADER = {"X-API-Key":API_KEY}

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

teams = {'arsenal': 'Aresenal', 'bournemouth': 'AFC Bournemouth', 'brighton-and-hove-albion': 'Brighton and Hove Albion', 'burnley': 'Burnely',
            'chelsea': 'Chelsea', 'crystal-palace': 'Crystal Palace', 'everton': 'Everton', 'huddersfield-town': "Huddersfield Town", 'leicester-city': 'Leicester City',
            'liverpool': 'Liverpool', 'manchester-city': 'Manchester City', 'manchester-united': 'Manchester United', 'newcastle-united': 'Newcastle United', 'southampton':'Southampton',
            'stoke-city': 'Stoke City', 'swansea-city': 'Swansea City', 'tottenham-hotspur': 'Tottenham Hotspur', 'watford': 'Watford', 'west-bromwich-albion': 'West Bromwich Albion',
            'west-ham-united': 'West Ham United'}

def get_data(url, payload=None):
    if payload != None:
        response = requests.get(url, params=payload)
        return json.loads(response.text)
    else:
        response = requests.get(url)
        return json.loads(response.text)

def get_general_news_sky():
    data = get_data(SKY_API_BASE + ENDPOINT_GENERAL_NEWS_SKY)
    News.objects.all().delete()
    for news in data:
        try:
            entry, created = News.objects.get_or_create(title = news['title'], url = news['link'], img_url = news['imgsrc'], description = news['shortdesc'], source = SKYSPORTS_SOURCE_ID)
        except:
            continue
    
def get_team_news_sky(teams):
    News.objects.exclude(teams=None).delete()
    for team, name in teams.iteritems():
        data = get_data(SKY_API_BASE + ENDPOINT_TEAM_NEWS_SKY.format(team))
        news_team = Team.objects.get(name=name)
        for news in data:
            team_news = News.objects.create(title = news['title'], url = news['link'], img_url = news['imgsrc'], description = news['shortdesc'], source = SKYSPORTS_SOURCE_ID)
            team_news.teams.add(news_team)

def create_team_table(teams):
    for api_name, name in teams.iteritems():
        Team.objects.create(api_name = api_name, name = name)

def get_sportsmonk_data(payload, action):
    if action == 'standing':
        data = get_data(SPORTSMONK_API_BASE + ENDPOINT_EPL_STANDING_SPORTSMONT, payload)
        Standing.objects.all().delete()
        for team in data['data'][0]['standings']['data']:
            logo_path = get_team_logo_url(team['team_name'])
            Standing.objects.create(name=team['team_name'], gp=team['overall']['games_played'], won=team['overall']['won'],
                                    draw=team['overall']['draw'], lost=team['overall']['lost'], gs=team['overall']['goals_scored'],
                                    ga=team['overall']['goals_against'],gd=team['total']['goal_difference'],point=team['total']['points'],
                                    recent_form=team['recent_form'], status=team['status'],logo_url=logo_path, position=team['position'])
    elif action == 'player_stat':
        data = get_data(SPORTSMONK_API_BASE + ENDPOINT_EPL_PLAYER_STAT + "?api_token=" + SPORTSMONK_API_KEY + ENDPOINT_EPL_PLATYER_STAT_INCLUDE)
        Score.objects.all().delete()
        Assist.objects.all().delete()
        Card.objects.all().delete()
        for player in data['data']['goalscorers']['data']:
            Score.objects.create(goal=player['goals'], name=player['player']['data']['fullname'], nationality=player['player']['data']['nationality'], 
                                img_url=player['player']['data']['image_path'], logo_url=player['team']['data']['logo_path'])
        for player in data['data']['cardscorers']['data']:
            yellow_card = player['yellowcards']
            red_card = player['redcards']
            total_card = red_card + yellow_card
            Card.objects.create(yellow_card=yellow_card, red_card=red_card, 
                                name=player['player']['data']['fullname'], nationality=player['player']['data']['nationality'], 
                                img_url=player['player']['data']['image_path'], logo_url=player['team']['data']['logo_path'], 
                                total_card=total_card)
    

def get_team_logo_url(team_name):
    return {
        'Manchester United': 'EPLNews/img/manu_logo.png',
        'Huddersfield Town': 'EPLNews/img/huddersfield_logo.png',
        'Manchester City': 'EPLNews/img/manc_logo.png',
        'Tottenham Hotspur': 'EPLNews/img/tottenham_logo.png',
        'Arsenal': 'EPLNews/img/arsenal_logo.png',
        'Burnley': 'EPLNews/img/burnley_logo.png',
        'Everton': 'EPLNews/img/everton_logo.png',
        'West Bromwich Albion': 'EPLNews/img/wba_logo.png',
        'Liverpool': 'EPLNews/img/liverpool_logo.png',
        'Watford': 'EPLNews/img/watford_logo.png',
        'Southampton': 'EPLNews/img/southampton_logo.png',
        'Swansea City': 'EPLNews/img/swansea_logo.png',
        'Leicester City': 'EPLNews/img/leicester_logo.png',
        'Chelsea': 'EPLNews/img/chelsea_logo.png',
        'Stoke City': 'EPLNews/img/stokecity_logo.png',
        'AFC Bournemouth': 'EPLNews/img/bournemouth_logo.png',
        'Newcastle United': 'EPLNews/img/newcastle_logo.png',
        'Brighton & Hove Albion': 'EPLNews/img/brighton_logo.png',
        'Crystal Palace': 'EPLNews/img/crystalpalace_logo.png',
        'West Ham United': 'EPLNews/img/westham_logo.png',
    }.get(team_name, None)


while TRIGGER:
    general_news = RepeatedTimer(600, get_general_news_sky)
    team_news = RepeatedTimer(500, get_team_news_sky, teams)
    standing = RepeatedTimer(400, get_sportsmonk_data, SPORTSMONK_PAYLOAD,'standing')
    player_stat = RepeatedTimer(300, get_sportsmonk_data, SPORTSMONK_PAYLOAD,'player_stat')
    try:
        sleep(1000) # your long-running job goes here...
    finally:
        general_news.stop() # better in a try/finally block to make sure the program ends!
        team_news.stop()
        standing.stop()
        player_stat.stop()
        progress.stop()
        TRIGGER = False

# get_general_news_sky()
# get_team_news_sky(teams)

# get_sportsmonk_data(SPORTSMONK_PAYLOAD, 'player_stat')
# get_sportsmonk_data(SPORTSMONK_PAYLOAD, 'standing')


