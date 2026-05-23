import requests
# from routes import AnimeData,db


#WORKING
#All Anime 
def anime_data():
    res = requests.get("https://api.jikan.moe/v4/anime")
    return res.json()['data']

#Popular Anime
def popular_anime():
    res = requests.get("https://api.jikan.moe/v4/top/anime?filter=bypopularity")
    return res.json()['data']
#top anime
def top_anime():
    res = requests.get("https://api.jikan.moe/v4/top/anime")
    return res.json()['data']

#Trending Anime
def trending_anime():
    res = requests.get("https://api.jikan.moe/v4/seasons/now")
    return res.json()['data']
#Airing Anime
def airing_anime():
    res = requests.get("https://api.jikan.moe/v4/top/anime?filter=airing")
    return res.json()['data']

#. Recently Released Anime
def recent_anime():
    anime = anime_data()
    res = sorted(anime,key=lambda x: x.get('aired', {}).get('from') or "",reverse=True)
    return res

#Upcoming Anime
def upcoming_anime():
    res = requests.get("https://api.jikan.moe/v4/seasons/upcoming")
    return res.json()['data']

#Movies
def movies():
    res = requests.get("https://api.jikan.moe/v4/anime?type=movie")
    return res.json()['data']

#TV series
def TV_series():
    res = requests.get("https://api.jikan.moe/v4/anime?type=tv")
    return res.json()['data']

#Search Anime by query/name
def search_by_query(query):
    # query = request.args.get('q')
    res = requests.get(f"https://api.jikan.moe/v4/anime?q={query}")
    return res.json()['data']

#Search Anime by mal_id
def search_by_id(mal_id):
    # query = request.args.get('q')
    res = requests.get(f"https://api.jikan.moe/v4/anime/{mal_id}")
    return res.json().get('data')

#search anime by genre
def get_anime_by_genre(id):
    res = requests.get(f"https://api.jikan.moe/v4/anime?genres={id}")
    return res.json()['data']


#Main Genres
#Action Anime
def action_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=1")
    return res.json()['data']

#Comedy Anime
def comedy_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=4")
    return res.json()['data']

#Advanture Anime
def advanture_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=2")
    return res.json()['data']

#Drama
def drama_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=8")
    return res.json()['data']
#Rommance
def rommance_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=22")
    return res.json()['data']
#Horror
def horror_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=14")
    return res.json()['data']
#Avant Garde
def avant_garde_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=5")
    return res.json()['data']
#Award Winning
def award_winning_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=46")
    return res.json()['data']
#Fantsy
def fantasy_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=10")
    return res.json()['data']
#Mystery
def mystery_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=7")
    return res.json()['data']
#Sci-Fi
def sci_fi_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=24")
    return res.json()['data']
#Slice of Life
def slice_of_life_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=36")
    return res.json()['data']
#Sports
def sports_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=30")
    return res.json()['data']
#Supernatural
def supernatura_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=37")
    return res.json()['data']
#Suspense
def suspense_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=41")
    return res.json()['data']

#Themes (Sub-genres)
#SSchool
def school_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=23")
    return res.json()['data']
#Shounen
def shounen_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=27")
    return res.json()['data']
#Shoujo
def shoujo_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=25")
    return res.json()['data']
#Seinen
def seinen_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=42")
    return res.json()['data']
#Harem
def harem_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=35")
    return res.json()['data']
#Josei
def josei_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=43")
    return res.json()['data']
#Isekai
def isekai_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=62")
    return res.json()['data']
#Mecha
def mecha_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=18")
    return res.json()['data']
#Military
def military_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=38")
    return res.json()['data']
#Music
def music_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=19")
    return res.json()['data']
#Psychological
def psychological_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=40")
    return res.json()['data']
#Historical
def historical_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=13")
    return res.json()['data']
#Parody
def parody_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=20")
    return res.json()['data']
#Samurai
def samurai_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=21")
    return res.json()['data']
#Super Power
def super_power_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=31")
    return res.json()['data']
#Vampire
def vampire_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=32")
    return res.json()['data']
#Kids
def kid_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=15")
    return res.json()['data']
#Military
def military_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=38")
    return res.json()['data']
#Military
def military_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=38")
    return res.json()['data']
#Military
def military_anime():
    res = requests.get("https://api.jikan.moe/v4/anime?genres=38")
    return res.json()['data']




