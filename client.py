import json, requests
from pprint import pprint
from apps.EPLNews.models import *

SKY_API_BASE = "https://skysportsapi.herokuapp.com"
# API_KEY = "9ynWTXljOQ3Mw4vP7HMEN6ymaHxVydbh1jINFhxv"

ENDPOINT_GENERAL_NEWS_SKY = "/sky/getnews/football/v1.0/"
ENDPOINT_TEAM_NEWS_SKY = "/sky/football/getteamnews/{0}/v1.0/"
SKYSPORTS_SOURCE_ID = 1

# DEFAULT_HEADER = {"X-API-Key":API_KEY}

teams = {'arsenal': 'Aresenal', 'bournemouth': 'AFC Bournemouth', 'brighton-and-hove-albion': 'Brighton and Hove Albion', 'burnley': 'Burnely',
            'chelsea': 'Chelsea', 'crystal-palace': 'Crystal Palace', 'everton': 'Everton', 'huddersfield-town': "Huddersfield Town", 'leicester-city': 'Leicester City',
            'liverpool': 'Liverpool', 'manchester-city': 'Manchester City', 'manchester-united': 'Manchester United', 'newcastle-united': 'Newcastle United', 'southampton':'Southampton',
            'stoke-city': 'Stoke City', 'swansea-city': 'Swansea City', 'tottenham-hotspur': 'Tottenham Hotspur', 'watford': 'Watford', 'west-bromwich-albion': 'West Bromwich Albion',
            'west-ham-united': 'West Ham United'}

def get_data(url):    
    response = requests.get(url)
    return json.loads(response.text)

def get_general_news_sky():
    data = get_data(SKY_API_BASE + ENDPOINT_GENERAL_NEWS_SKY)
    for news in data:
        try:
            entry, created = News.objects.get_or_create(title = news['title'], url = news['link'], img_url = news['imgsrc'], description = news['shortdesc'], source = SKYSPORTS_SOURCE_ID)
        except:
            continue
    

def get_team_news_sky(teams):
    for team, name in teams.iteritems():
        data = get_data(SKY_API_BASE + ENDPOINT_TEAM_NEWS_SKY.format(team))
        news_team = Team.objects.get(name=name)
        for news in data:
            team_news = News.objects.create(title = news['title'], url = news['link'], img_url = news['imgsrc'], description = news['shortdesc'], source = SKYSPORTS_SOURCE_ID)
            team_news.teams.add(news_team)

def create_team_table(teams):
    for api_name, name in teams.iteritems():
        Team.objects.create(api_name = api_name, name = name)

get_general_news_sky()
get_team_news_sky(teams)
