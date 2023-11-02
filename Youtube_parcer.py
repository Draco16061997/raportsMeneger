import json
from googleapiclient.discovery import build
import google.oauth2
import sqlite3
import re
import paths

API_KEY = paths.API_Youtube



#
# DO = "UC1h4sv6jq8vrKvtyNSqbpYQ"
# NM = "UCaU3czdSiC8YbC7VM0ebEtQ"
# DP = "UCK3Js2yhZYjxpdfYkMveoGg"



db = sqlite3.connect(paths.pathDb)
c = db.cursor()
def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS YoutubeVideo 
    (data DATA, 
    name NVARCHAR(256), 
    url TEXT, 
    chanel TEXT,
    key TEXT)''')

    db.commit()

def get_service():
    service = build('youtube', 'v3', developerKey=API_KEY)
    return service
def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # Emoticons
                               u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
                               u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
                               u"\U0001F700-\U0001F77F"  # Alchemical Symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U0001F004-\U0001F0CF"  # Additional emoticons
                               u"\U0001F200-\U0001F251"  # Additional symbols
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', text)

def getlist(chanelId):
    keyUrl = "https://www.youtube.com/watch?v="

    service = build('youtube', 'v3', developerKey=API_KEY)

    r = service.search().list(
        channelId=chanelId,
        part="snippet",
        type="video",
        order="date",
        maxResults='50'
    ).execute()

    dat = r['items'][0]['snippet']['publishedAt']
    title = r['items'][0]['snippet']['title']
    l = r['items']
    youYubeList = []

    for i in l:
        titleChanel = i['snippet']['channelTitle']
        title = i['snippet']['title'].replace("&quot;","")

        dataPublish = i['snippet']['publishedAt'].split('T')[0]
        url = keyUrl+i['id']['videoId']
        # key = title.replace(":","")
        # key = key.replace("?","")
        # key = key.replace('"','')
        # key = key.replace('!','')
        # key = key.replace('❗️', '')
        # key = key.replace('⚡️ ', '')
        # key = key.replace("-", " ")
        # key = key.replace("&#39;", "")
        # key = remove_emoji(key)
        key = i['id']['videoId']
    #
        youYubeList.append((dataPublish, title, url, titleChanel, key))
    #
    #     # print(titleChanel)
    #     # print(title)
    #     # print(dataPublish)
    #     # print(url)



    return youYubeList

# def get_video_info(video_id):
#     r = get_service().videos().list(id=video_id, part='snippet').execute()
#     # print(json.dumps(r['items']))
#
#     print(r)

def writheBdYoutube(idChenal):
    createTable()
    for i in getlist(idChenal):
        c.execute(f"SELECT name FROM YoutubeVideo WHERE name = '{i[1]}'")
        if c.fetchone() is None:
            c.execute(f"INSERT INTO YoutubeVideo VALUES (?, ?, ?, ?, ?)", (i[0], i[1], i[2], i[3], i[4]))
        db.commit()
    if idChenal == 'UC1h4sv6jq8vrKvtyNSqbpYQ':
        print(f'Data baise {i[3]} UPDATES!')
    elif idChenal == "UCaU3czdSiC8YbC7VM0ebEtQ":
        print(f'Data baise {i[3]} UPDATES!')
    elif idChenal == "UCK3Js2yhZYjxpdfYkMveoGg":
        print(f'Data baise {i[3]} UPDATES!')
    else:
        print(" none")



# for i in getlist(NM):
#     print(i)

# for i in getlist(DO):
#     print(i)

# createTable()
#
for i in paths.Chanels:
    writheBdYoutube(i)

    print(i + "======= OK!")
# writheBdYoutube(paths.Chanels[0])
# writheBdYoutube(NM)
# writheBdYoutube(DP)


db.close()

if __name__ =="__main__":
    print("youtube OK!")