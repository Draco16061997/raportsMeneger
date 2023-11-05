import os
import sqlite3
import users
import paths

path = paths.scan_path

db = sqlite3.connect(paths.pathDb)
c = db.cursor()

l = []

def WalkFiles(path):
    # l = []
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            WalkFiles(path + '/' + i)
        else:
            l.append(i)
    return l


def getListFiles(path):
    l = []
    for i in WalkFiles(path):
        s = i.replace(".mp4", "")
        s = s.split('_', 4)
        t = len(s)
        if t == 5:
            l.append(s)
    return l


def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS VideoStorage
    (
    NameFile TEXT,
    TypeClip TEXT,
    NameJurn TEXT,
    NameDirector TEXT,
    key TEXT,
    FOREIGN KEY (key) REFERENCES YoutubeVideo(key)

    )''')

    db.commit()


def writheBdList(path):
    createTable()
    for i in getListFiles(path):

        nameDir = i[3]
        nameJurn = i[2]

        typVideo = i[1]

        key = i[4].replace(" ", "")
        key = key.replace("@SynoEAStream", "")
        key = key.replace("@SynoResource", "")

        if users.getId(nameJurn) != None:
            nameJurn = users.getId(nameJurn)
        if users.getId(nameDir) != None:
            nameDir = users.getId(nameDir)
        if users.getIdType(typVideo) != None:
            typVideo = users.getIdType(typVideo)


        if typVideo == "НМ" or typVideo == "ДО" or typVideo == "ДП":
            typVideo = "СЮЖ"

        c.execute(f"SELECT key FROM VideoStorage WHERE key = '{key}'")
        if c.fetchone() is None:
            c.execute(f"INSERT INTO VideoStorage VALUES (?, ?, ?, ?, ?)", (i[0], typVideo, nameJurn, nameDir, key))
        db.commit()

for i in paths.scan_path:
    writheBdList(i)
    print(i + " ========== OK!")


db.close()
if __name__ == '__main__':
    print("folder Updates!!!")