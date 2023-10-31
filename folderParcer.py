import os
import sqlite3
# path = '/Users/mikita/Work/Продакшн/END/'
Nikita = '/volume2/NAS_1/Готовые_сюжети/Никита/'
Igor = '/volume2/NAS_1/Готовые_сюжети/Игорь/'
Jenya = '/volume2/NAS_1/Готовые_сюжети/Євген/'
Kostya = '/volume2/NAS_1/Готовые_сюжети/Костя/'
Taylor = '/volume2/NAS_1/Готовые_сюжети/Taylor'
l =[]
def WalkFiles(path):
    # l = []
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            WalkFiles(path+'/'+i)
        else: l.append(i)
    return l

def getListFiles(path):
    l = []
    for i in WalkFiles(path):
        s = i.replace(".mp4","")
        s = s.split('_', 4)
        t = len(s)
        if t == 5:
            l.append(s)
    return l
db = sqlite3.connect("/volume1/scripts/Youtube_raports/Youtube.db")
# db = sqlite3.connect("/Users/mikita/Main/PythonProjects/folderParcer/Youtube.db")
c = db.cursor()
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
        
        s = i[1]
        key = i[4].replace(" ","")
        key = key.replace("@SynoEAStream","")
        key = key.replace("@SynoResource","")

        if nameDir == "Скрипниченко" or nameDir == "cкрипниченко" or nameDir == "cкрипніченко":
            nameDir = "Скрипніченко"
            
        if nameJurn == "Табацкая" or nameJurn == "Сухонис" or nameJurn == "сухоніс" or nameJurn == "сухонис" or nameJurn == "Табацька"or nameJurn == "Дарина":
            nameJurn = "Сухоніс"
            
        if nameDir == "Ігор":
            nameDir = "Бездільний"
            
        if nameDir == "Костя":
            nameDir = "Фурдуй"
            
        if s == "НМ" or s == "ДО" or s == "ДП":
        	s = "СЮЖ"


        c.execute(f"SELECT key FROM VideoStorage WHERE key = '{key}'")
        if c.fetchone() is None:
            c.execute(f"INSERT INTO VideoStorage VALUES (?, ?, ?, ?, ?)", (i[0], s, nameJurn, nameDir, key))
        db.commit()

# writheBdList(path)
writheBdList(Nikita)
writheBdList(Igor)
writheBdList(Jenya)
writheBdList(Kostya)
writheBdList(Taylor)

db.close()

print("folders Updates!!!")
