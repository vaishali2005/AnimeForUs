import requests
# from routes import AnimeData,db
from urllib.parse import quote
import time

#WORKING
#All Anime 
def anime_data():
    time.sleep(0.5)
    return jikan_request(
            "https://api.jikan.moe/v4/anime"
        )


def jikan_request(url, params=None):
    max_retries = 3

    for attempt in range(max_retries):
        try:
            res = requests.get(
                url,
                params=params,
                timeout=15
            )

            print("JIKAN URL:", res.url)
            print("JIKAN STATUS:", res.status_code)

            if res.status_code == 200:
                response = res.json()
                return response.get("data") or []

            if res.status_code in (429, 500, 502, 503, 504):
                print(
                    f"JIKAN TEMPORARY ERROR: {res.status_code} "
                    f"(attempt {attempt + 1}/{max_retries})"
                )

                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue

            print("JIKAN ERROR:", res.text[:500])
            return []

        except requests.RequestException as e:
            print(
                f"JIKAN CONNECTION ERROR "
                f"(attempt {attempt + 1}/{max_retries}): {e}"
            )

            if attempt < max_retries - 1:
                time.sleep(2)
                continue

            return []



#Popular Anime
def popular_anime():
    time.sleep(0.5)
    return jikan_request(
        "https://api.jikan.moe/v4/top/anime",
        params={
            "filter": "bypopularity"
        }
    ) or []
#top anime
def top_anime():
    time.sleep(0.5)
    return jikan_request("https://api.jikan.moe/v4/top/anime")

#Trending Anime
def trending_anime():
    time.sleep(0.5)
    return jikan_request("https://api.jikan.moe/v4/seasons/now")
#Airing Anime
def airing_anime():
    time.sleep(0.5)
    return jikan_request("https://api.jikan.moe/v4/top/anime?filter=airing")

#. Recently Released Anime
def recent_anime():
    time.sleep(0.5)
    anime = anime_data() or []
    res = sorted(anime,key=lambda x: x.get('aired', {}).get('from') or "",reverse=True)
    return res

#Upcoming Anime
def upcoming_anime():
    time.sleep(0.5)
    return jikan_request("https://api.jikan.moe/v4/seasons/upcoming")

#Movies
def movies():
    return jikan_request("https://api.jikan.moe/v4/anime?type=movie")

#TV series
def TV_series():
    return jikan_request("https://api.jikan.moe/v4/anime?type=tv")

#Search Anime by query/name
def search_by_query(query):
    return jikan_request(
        "https://api.jikan.moe/v4/anime",
        params={
            "q": query
        }
    )

#Search Anime by mal_id
def search_by_id(mal_id):
    return jikan_request(f"https://api.jikan.moe/v4/anime/{mal_id}")

#search anime by genre
def get_anime_by_genre(id):
    return jikan_request(f"https://api.jikan.moe/v4/anime?genres={id}")


#Main Genres
#Action Anime
def action_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=1")

#Comedy Anime
def comedy_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=4")

#Advanture Anime
def advanture_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=2")

#Drama
def drama_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=8")
#Rommance
def rommance_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=22")
#Horror
def horror_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=14")
#Avant Garde
def avant_garde_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=5")
#Award Winning
def award_winning_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=46")
#Fantsy
def fantasy_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=10")
#Mystery
def mystery_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=7")
#Sci-Fi
def sci_fi_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=24")
#Slice of Life
def slice_of_life_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=36")
#Sports
def sports_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=30")
#Supernatural
def supernatura_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=37")
#Suspense
def suspense_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=41")

#Themes (Sub-genres)
#SSchool
def school_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=23")
#Shounen
def shounen_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=27")
#Shoujo
def shoujo_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=25")
#Seinen
def seinen_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=42")
#Harem
def harem_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=35")
#Josei
def josei_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=43")
#Isekai
def isekai_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=62")
#Mecha
def mecha_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=18")
#Military
def military_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=38")
#Music
def music_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=19")
#Psychological
def psychological_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=40")
#Historical
def historical_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=13")
#Parody
def parody_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=20")
#Samurai
def samurai_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=21")
#Super Power
def super_power_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=31")
#Vampire
def vampire_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=32")
#Kids
def kid_anime():
    return jikan_request("https://api.jikan.moe/v4/anime?genres=15")




