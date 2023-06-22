import selenium
import sqlite3

import tkinter.ttk as ttk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# atlantic division teams logos
celticsicon = file="celticslogo.png"
netsicon = file="netslogo.png"
knickssicon = file="knickslogo.png"
philisicon = file="phililogo.png"
raptorsicon = file="raptorslogo.png"

# central division teams logos
bullsicon = file="bullslogo.png"
cavsicon = file="cavslogo.png"
pistonsicon = file="pistonslogo.png"
pacersicon = file="pacerslogo.png"
bucksicon = file="buckslogo.png"


#southeast division teams logos
hawksicon = file="hawkslogo.png"
hornetsicon = file="hornetslogo.png"
heaticon = file="heatlogo.png"
magicicon = file="magiclogo.png"
wizardsicon = file="wizardslogo.png"

#northwest division teams logo
nuggetsicon = file="nuggetslogo.png"
timberwolvesicon = file="timberwolveslogo.png"
okcicon = file="okclogo.png"
blazersicon = file="blazerlogo.png"
jazzicon = file="jazzlogo.png"

#pacific division teams logo
warriorsicon = file="warriorslogo.png"
clippersicon = file="clipperslogo.png"
lakersicon = file="lakerslogo.png"
sunsicon = file="sunslogo.png"
kingsicon = file="kingslogo.png"

#southwest division teams logos
mavericksicon = file="magiclogo.png"
rocketsicon = file="rocketslogo.png"
grizzliesicon = file="grizzlieslogo.png"
pelicansicon = file="pelicanslogo.png"
spursicon = file="spurslogo.png"

Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=Path)

driver.get("https://www.cbssports.com/nba/standings/")
table = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, """//*[@id="TableBase-1"]/div/div/table/tbody""")))

rows = table.find_elements(By.TAG_NAME, "tr")
data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = []
    for cell in cells:
        row_data.append(cell.text)
    data.append(row_data)

db = sqlite3.connect('NBA teams.db')
dbcursor = db.cursor()

# dbcursor.execute('''CREATE TABLE StandingTable1
#                     (Position TEXT PRIMARY KEY,
#                      Team TEXT,
#                      W TEXT,
#                      L TEXT,
#                      PCT TEXT,
#                      GB TEXT,
#                      PPG TEXT,
#                      OPPG TEXT,
#                      DIFF TEXT,
#                      Home TEXT,
#                      Road TEXT,
#                      DIV TEXT,
#                      CONF TEXT,
#                      STREAK TEXT,
#                      L10 TEXT,
#                      WP TEXT,
#                      DIVP TEXT,
#                      POST TEXT)''')

dbcursor.execute('INSERT INTO StandingTable (Position, Team, W, L, PCT, GB, PPG, OPPG, DIFF, Home, Road, DIV, CONF, STREAK, L10, WP, DIVP, POST) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row_data)

dbcursor.execute('SELECT * FROM StandingTable')
table = dbcursor.fetchall()

for x in table:
    print(x)

db.commit()

