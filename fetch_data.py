import requests
# from routes import AnimeData,db
from urllib.parse import quote
import time


#WORKING
#All Anime 
def anime_data():
    return jikan_request(
            "https://api.jikan.moe/v4/anime"
        )


import requests
import time

def jikan_request(url, params=None):
    """Improved version with retries and better headers"""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    # Try 3 times with different endpoints
    endpoints = [
        url,  # Primary
        url.replace('api.jikan.moe', 'api2.jikan.moe'),  # Backup 1
        url.replace('api.jikan.moe', 'api3.jikan.moe'),  # Backup 2
    ]
    
    for attempt, endpoint in enumerate(endpoints):
        try:
            print(f"[Attempt {attempt + 1}] Fetching: {endpoint}")
            
            res = requests.get(
                endpoint,
                params=params,
                timeout=10,  # Reduced timeout
                headers=headers
            )

            if res.status_code == 200:
                response = res.json()
                data = response.get("data") or []
                print(f"✅ Success! Got {len(data)} items")
                return data
            
            elif res.status_code == 429:  # Rate limited
                print(f"⚠️ Rate limited. Waiting 2 seconds...")
                time.sleep(2)
                continue
            
            elif res.status_code == 504:  # Bad Gateway
                print(f"⚠️ 504 Error. Trying next endpoint...")
                time.sleep(1)
                continue
            
            else:
                print(f"❌ Error {res.status_code}: {res.text[:100]}")
                continue

        except requests.Timeout:
            print(f"⏱️ Timeout on {endpoint}. Trying next...")
            time.sleep(1)
            continue
            
        except requests.RequestException as e:
            print(f"❌ Connection error: {e}")
            continue
    
    # If all endpoints fail, return empty list
    print(f"❌ All endpoints failed for {url}")
    return []



#Popular Anime
def popular_anime():
    return jikan_request(
        "https://api.jikan.moe/v4/top/anime",
        params={
            "filter": "bypopularity"
        }
    ) or []
#top anime
def top_anime():
    return jikan_request("https://api.jikan.moe/v4/top/anime")

#Trending Anime
def trending_anime():
    return jikan_request("https://api.jikan.moe/v4/seasons/now")
#Airing Anime
def airing_anime():
    return jikan_request("https://api.jikan.moe/v4/top/anime?filter=airing")

#. Recently Released Anime
def recent_anime():
    anime = anime_data() or []
    res = sorted(anime,key=lambda x: x.get('aired', {}).get('from') or "",reverse=True)
    return res

#Upcoming Anime
def upcoming_anime():
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




