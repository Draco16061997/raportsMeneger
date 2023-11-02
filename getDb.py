import sqlite3
import paths

pathDb = paths.pathDb

def ExecuteJurnDB(isShorts, IDJurn, ot, do):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    selecter = None
    if isShorts:
        selecter = '='
    else:
        selecter = '<>'

    c.execute(f'''SELECT YoutubeVideo.data, YoutubeVideo.name, typeVideo.name,YoutubeVideo.chanel, Jurn.name AS JurnName, Dir.name AS DirName, YoutubeVideo.url
            FROM YoutubeVideo
            LEFT JOIN VideoStorage ON VideoStorage.key = YoutubeVideo.key
            LEFT JOIN typeVideo ON typeVideo.id = VideoStorage.TypeClip
            LEFT JOIN emploues AS Jurn ON Jurn.id = VideoStorage.NameJurn
            LEFT JOIN emploues AS Dir ON Dir.id = VideoStorage.NameDirector
            WHERE VideoStorage.NameJurn = {IDJurn} AND typeVideo.id {selecter} 2  AND YoutubeVideo.data BETWEEN '{ot}' AND '{do}'
            ORDER BY YoutubeVideo.data DESC;
                        ''')

    rows = c.fetchall()
    # t = 0
    # for i in rows:
    #     print(i)
    #     t += 1
    # print(t)

    db.close()
    return rows

def ExecuteDirDB(isShorts, IDDir, ot, do):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    selecter = None
    if isShorts:
        selecter = '='
    else:
        selecter = '<>'

    c.execute(f'''SELECT YoutubeVideo.data, YoutubeVideo.name, typeVideo.name,YoutubeVideo.chanel, Jurn.name AS JurnName, Dir.name AS DirName, YoutubeVideo.url
            FROM YoutubeVideo
            LEFT JOIN VideoStorage ON VideoStorage.key = YoutubeVideo.key
            LEFT JOIN typeVideo ON typeVideo.id = VideoStorage.TypeClip
            LEFT JOIN emploues AS Jurn ON Jurn.id = VideoStorage.NameJurn
            LEFT JOIN emploues AS Dir ON Dir.id = VideoStorage.NameDirector
            WHERE VideoStorage.NameDirector = {IDDir} AND typeVideo.id {selecter} 2  AND YoutubeVideo.data BETWEEN '{ot}' AND '{do}'
            ORDER BY YoutubeVideo.data DESC;
                        ''')

    rows = c.fetchall()
    db.close()
    return rows

def ExecuteResDB(isShorts, res, ot, do):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    list = ('Дніпро Оперативний - життя великого міста','Наше Місто','Дніпровська Панорама')

    selecter = None
    if isShorts:
        selecter = '='
    else:
        selecter = '<>'

    c.execute(f'''SELECT YoutubeVideo.data, YoutubeVideo.name, typeVideo.name,YoutubeVideo.chanel, Jurn.name AS JurnName, Dir.name AS DirName, YoutubeVideo.url
            FROM YoutubeVideo
            LEFT JOIN VideoStorage ON VideoStorage.key = YoutubeVideo.key
            LEFT JOIN typeVideo ON typeVideo.id = VideoStorage.TypeClip
            LEFT JOIN emploues AS Jurn ON Jurn.id = VideoStorage.NameJurn
            LEFT JOIN emploues AS Dir ON Dir.id = VideoStorage.NameDirector
            WHERE YoutubeVideo.chanel = '{list[res]}' AND typeVideo.id {selecter} 2  AND YoutubeVideo.data BETWEEN '{ot}' AND '{do}'
            ORDER BY YoutubeVideo.data DESC;
                        ''')

    rows = c.fetchall()
    db.close()
    return rows

# #
for i in ExecuteResDB(True,1,'2023-10-24','2023-11-01'):
    print(i)

# for i in ExecuteDirDB(False,12,'2023-10-24','2023-11-01'):
#     print(i)
# for i in ExecuteJurnDB(True, 1,'2023-10-24','2023-11-01'):
#     print(i)

if __name__ == '__main__':
    print("run")
