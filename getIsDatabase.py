import sqlite3

incorect = "Інформація відсунтя"
noneType = "ХЗ"


pathDb = "/volume1/scripts/Youtube_raports/Youtube.db"
def getRecurceList(name, end, start):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l=[]
    c.execute(f'''SELECT *
            FROM YoutubeVideo
            LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
            WHERE chanel = '{name}' AND data BETWEEN '{start}' AND '{end}'
            ORDER BY data DESC''')

    rows = c.fetchall()

    for i in rows:
        jurn = i[-3]
        director = i[-2]
        type = i[6]
        if jurn == None:
            jurn = incorect
        if director == None:
            director = incorect

        if type == 'ДО' or type == 'НМ' or type == 'ДП' or type == None:
            type = noneType

        t = (i[0], type, i[1], i[3], jurn, director, i[2])
        l.append(t)
    db.close()
    return l

def getJurnForPeriod(name, end, start):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l=[]
    c.execute(f'''SELECT *
            FROM YoutubeVideo
            LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
            WHERE NameJurn = '{name}' OR NameDirector = '{name}' AND data BETWEEN '{start}' AND '{end}'
            ORDER BY data DESC''')

    rows = c.fetchall()

    for i in rows:
        jurn = i[-3]
        director = i[-2]
        type = i[6]
        if jurn == None:
            jurn = incorect
        if director == None:
            director = incorect

        if type == 'ДО' or type == 'НМ' or type == 'ДП' or type == None:
            type = noneType

        t = (i[0], type, i[1], i[3], jurn, director, i[2])
        l.append(t)
    db.close()
    return l

def getPeriod(end, start):
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l = []
    c.execute(f'''SELECT *
                     FROM YoutubeVideo
                     LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
                     WHERE data BETWEEN '{start}' AND '{end}'
                     ORDER BY data DESC''')

    rows = c.fetchall()

    for i in rows:
        jurn = i[-3]
        director = i[-2]
        type = i[6]
        if jurn == None:
            jurn = incorect
        if director == None:
            director = incorect

        if type == 'ДО' or type == 'НМ' or type == 'ДП'or type == None:
            type = noneType

        t = (i[0],type, i[1], i[3], jurn, director, i[2] )
        l.append(t)
    db.close()
    return l

def getNameJurn():
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l = []
    c.execute(f'''SELECT *
                FROM YoutubeVideo
                LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
                ''')

    rows = c.fetchall()

    for i in rows:
        name = i[-3]
        if name != None:
            l.append(name)

    db.close()
    l = set(l)
    return l

def getNameDir():
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l = []
    c.execute(f'''SELECT *
                FROM YoutubeVideo
                LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
                ''')

    rows = c.fetchall()

    for i in rows:
        name = i[-2]
        if name != None:
            l.append(name)

    db.close()
    l = set(l)
    return l

def getResurce():
    db = sqlite3.connect(pathDb)
    c = db.cursor()
    l = []
    c.execute(f'''SELECT *
                FROM YoutubeVideo
                LEFT JOIN VideoStorage ON YoutubeVideo.key = VideoStorage.key
                ''')

    rows = c.fetchall()

    for i in rows:
        name = i[3]
        if name != None:
            l.append(name)

    db.close()
    l = set(l)
    return l


if __name__ == "__main__":
    print("start ")
    print(getNameDir())
    print(getNameJurn())