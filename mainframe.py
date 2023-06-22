from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk, Frame, Button, Label
from tkinter import messagebox

import tkfontchooser
import tkinter
import re
import sqlite3
import tkinter.ttk as ttk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from NBA_Teams_Info import LoadTeam_page
from home_page import homepage
#from playersframe import search_player
from playersframe import league_leaders
from scores import scorecards_



root = Tk()
root.geometry("1040x800")
root.config(bg="black")
root.eval("tk::PlaceWindow . center")

font = tkfontchooser.Font(family="Mesquite Std")

backgroundpic = Image.open("mainframe background.png")
resized = backgroundpic.resize((1040, 820), Image.Resampling.LANCZOS)
newbkpic = ImageTk.PhotoImage(resized)

bklable = Label(root, image=newbkpic)
#bklable.place(x=0, y=0, relwidth=1, relheight=1)
bklable.pack(fill=BOTH, expand=1)
menuimg = PhotoImage(file="menubutton.png")
settingicon = PhotoImage(file="settingsbutton.png")
iconimg = PhotoImage(file="logo2.png")
iconimg2 = PhotoImage(file="logo.png")
root.iconphoto(False,iconimg)
root.title("NBA NEWS")

font = tkfontchooser.Font(family="Mesquite Std")

lmb = PhotoImage(file="lightmodebutton.png")
dmb = PhotoImage(file="darkmodebutton.png")

# atlantic division teams logos
celticsicon = PhotoImage(file="celticslogo.png")
netsicon = PhotoImage(file="netslogo.png")
knickssicon = PhotoImage(file="knickslogo.png")
philisicon = PhotoImage(file="phililogo.png")
raptorsicon = PhotoImage(file="raptorslogo.png")


# central division teams logos
bullsicon = PhotoImage(file="bullslogo.png")
cavsicon = PhotoImage(file="cavslogo.png")
pistonsicon = PhotoImage(file="pistonslogo.png")
pacersicon = PhotoImage(file="pacerslogo.png")
bucksicon = PhotoImage(file="buckslogo.png")


#southeast division teams logos
hawksicon = PhotoImage(file="hawkslogo.png")
hornetsicon = PhotoImage(file="hornetslogo.png")
heaticon = PhotoImage(file="heatlogo.png")
magicicon = PhotoImage(file="magiclogo.png")
wizardsicon = PhotoImage(file="wizardslogo.png")

#northwest division teams logo
nuggetsicon = PhotoImage(file="nuggetslogo.png")
timberwolvesicon = PhotoImage(file="timberwolveslogo.png")
okcicon = PhotoImage(file="okclogo.png")
blazersicon = PhotoImage(file="blazerlogo.png")
jazzicon = PhotoImage(file="jazzlogo.png")

#pacific division teams logo
warriorsicon = PhotoImage(file="warriorslogo.png")
clippersicon = PhotoImage(file="clipperslogo.png")
lakersicon = PhotoImage(file="lakerslogo.png")
sunsicon = PhotoImage(file="sunslogo.png")
kingsicon = PhotoImage(file="kingslogo.png")

#southwest division teams logos
mavericksicon = PhotoImage(file="magiclogo.png")
rocketsicon = PhotoImage(file="rocketslogo.png")
grizzliesicon = PhotoImage(file="grizzlieslogo.png")
pelicansicon = PhotoImage(file="pelicanslogo.png")
spursicon = PhotoImage(file="spurslogo.png")

abl = PhotoImage(file="arrowbuttonleft.png")
abr = PhotoImage(file="arrowbuttonright.png")


def clear_widgets(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

global light_mode
light_mode = False

def lightmode(frame):
    for widgets in frame.winfo_children():
        widgets.config(bg="white")
    frame.configure(bg="white")


global optionsframe
global mainframe


optionsframe = Frame(root, bg="black", width=1040, height=120)
logoframe = Frame(root, bg="black", width=1040, height=100)
mainframe = Frame(root, bg="red", width=1000, height=700)
mainframe.place(x=20, y=220)


def loadteamspage():

    if light_mode == True:
        lightmode(mainframe)

    clear_widgets(mainframe)
    mainframe.configure(bg="black")

    teamslabel = Label(mainframe, text="NBA TEAMS", font=(font, 30), bg="black", fg="#E65C06")
    teamslabel.place(x=0, y=0)



    def load_atlantic_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="ATLANTIC DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_southwest_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command=lambda : load_central_divisionframe())

        celtics_button = Button(mainframe, image=celticsicon, bg="#E65C06", borderwidth=0,
                                activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "BostonCelticsRoster" ,
                                                                                          "celticslogo.png",
                                                                                          "https://www.cbssports.com/nba/teams/BOS/boston-celtics/",
                                                                                          "https://www.nba.com/team/1610612738/celtics"))
        nets_button = Button(mainframe, image=netsicon, bg="#E65C06", borderwidth=0,
                             activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "BrooklynNetsRoster", "netslogo.png", 'https://www.cbssports.com/nba/teams/BKN/brooklyn-nets/', "https://www.nba.com/team/1610612751/nets"))
        knicks_button = Button(mainframe, image=knickssicon, bg="#E65C06", borderwidth=0,
                               activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "NewYorkKnicksRoster",
                                                                                         "knickslogo.png",
                                                                                         'https://www.cbssports.com/nba/teams/NY/new-york-knicks/',
                                                                                         "https://www.nba.com/team/1610612752/knicks"))
        philis_button = Button(mainframe, image=philisicon, bg="#E65C06", borderwidth=0,
                               activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "Philadelphia76ersRoster", "phililogo.png", 'https://www.cbssports.com/nba/teams/PHI/philadelphia-76ers/', "https://www.nba.com/team/1610612755/sixers"))
        raptors_button = Button(mainframe, image=raptorsicon, bg="#E65C06", borderwidth=0,
                                activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "TorontoRaptorsRoster", "raptorslogo.png", 'https://www.cbssports.com/nba/teams/TOR/toronto-raptors/', "https://www.nba.com/team/1610612761/raptors"))



        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=380,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        celtics_button.place(x=0, y=180)
        nets_button.place(x=200, y=180)
        knicks_button.place(x=400, y=180)
        philis_button.place(x=600, y=180)
        raptors_button.place(x=800, y=180)


    def load_central_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="CENTRAL DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_atlantic_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command= lambda : load_southeast_divisionframe())

        bulls_button = Button(mainframe, image=bullsicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "ChicagoBullsRoster" , "bullslogo.png", "https://www.cbssports.com/nba/teams/CHI/chicago-bulls/","https://www.nba.com/team/1610612741/bulls"))
        cavs_button = Button(mainframe, image=cavsicon, bg="#E65C06", borderwidth=0,
                             activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "ClevelandCavaliersRoster", 'cavslogo.png', "https://www.cbssports.com/nba/teams/CLE/cleveland-cavaliers/","https://www.nba.com/team/1610612739/cavaliers"))
        pistons_button = Button(mainframe, image=pistonsicon, bg="#E65C06", borderwidth=0,
                                activebackground="black", command = lambda : LoadTeam_page(mainframe, font, "DetroitPistonsRoster", "pistonslogo.png", "https://www.cbssports.com/nba/teams/DET/detroit-pistons/", "https://www.nba.com/team/1610612765/pistons"))
        pacers_button = Button(mainframe, image=pacersicon, bg="#E65C06", borderwidth=0,
                               activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "IndianaPacersRoster", "pacerslogo.png", "https://www.cbssports.com/nba/teams/IND/indiana-pacers/", "https://www.nba.com/team/1610612754/pacers"))
        bucks_button = Button(mainframe, image=bucksicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command = lambda : LoadTeam_page(mainframe, font, "MilwaukeeBucksRoster", "buckslogo.png", "https://www.cbssports.com/nba/teams/MIL/milwaukee-bucks/", "https://www.nba.com/team/1610612749/bucks"))



        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=380,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        bulls_button.place(x=0, y=180)
        cavs_button.place(x=200, y=180)
        pistons_button.place(x=400, y=180)
        pacers_button.place(x=600, y=180)
        bucks_button.place(x=800, y=180)


    def load_southeast_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="SOUTHEAST DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_central_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command= lambda : load_northwest_divisionframe())

        hawks_button = Button(mainframe, image=hawksicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "AtlantaHawksRoster", "hawkslogo.png", "https://www.cbssports.com/nba/teams/ATL/atlanta-hawks/", "https://www.nba.com/team/1610612737/hawks"))
        hornets_button = Button(mainframe, image=hornetsicon, bg="#E65C06", borderwidth=0,
                                activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "CharlotteHornetsRoster", "hornetslogo.png", "https://www.cbssports.com/nba/teams/CHA/charlotte-hornets/","https://www.nba.com/team/1610612766/hornets"))
        heat_button = Button(mainframe, image=heaticon, bg="#E65C06", borderwidth=0,
                             activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "MiamiHeatRoster", "heatlogo.png", "https://www.cbssports.com/nba/teams/MIA/miami-heat/", "https://www.nba.com/team/1610612748/heat"))
        magic_button = Button(mainframe, image=magicicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "OrlandoMagicRoster", "magiclogo.png", "https://www.cbssports.com/nba/teams/ORL/orlando-magic/stats/", "https://www.nba.com/team/1610612753/magic"))
        wizards_button = Button(mainframe, image=wizardsicon, bg="#E65C06", borderwidth=0,
                                activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "WashingtonWizardsRoster", "wizardslogo.png", "https://www.cbssports.com/nba/teams/WAS/washington-wizards/", "https://www.nba.com/team/1610612764/wizards"))



        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=365,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        hawks_button.place(x=0, y=180)
        hornets_button.place(x=200, y=180)
        heat_button.place(x=400, y=180)
        magic_button.place(x=600, y=180)
        wizards_button.place(x=800, y=180)


    def load_northwest_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="NORTHWEST DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_southeast_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command= lambda : load_pacific_divisionframe())

        nuggets_button = Button(mainframe, image=nuggetsicon,bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "DenverNuggetsRoster", "nuggetslogo.png", "https://www.cbssports.com/nba/teams/DEN/denver-nuggets/","https://www.nba.com/team/1610612743/nuggets"))
        timberwolves_button = Button(mainframe, image=timberwolvesicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "MinnesotaTimberwolvesRoster", "timberwolveslogo.png", "https://www.cbssports.com/nba/teams/MIN/minnesota-timberwolves/", "https://www.nba.com/team/1610612750/timberwolves"))
        thunder_button = Button(mainframe, image=okcicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "OklahomaCityThunderRoster", "thunderlogo.png", "https://www.cbssports.com/nba/teams/OKC/oklahoma-city-thunder/", "https://www.nba.com/team/1610612760/thunder"))
        blazers_button = Button(mainframe, image=blazersicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "PortlandTrailBlazersRoster", "blazers.png", "https://www.cbssports.com/nba/teams/POR/portland-trail-blazers/", "https://www.nba.com/team/1610612757/blazers"))
        jazz_button = Button(mainframe, image=jazzicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "UtahJazzRoster", "jazzlogo.png", "https://www.cbssports.com/nba/teams/UTA/utah-jazz/", "https://www.nba.com/team/1610612762/jazz"))




        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=365,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        nuggets_button.place(x=0, y=180)
        timberwolves_button.place(x=200, y=180)
        thunder_button.place(x=400, y=180)
        blazers_button.place(x=600, y=180)
        jazz_button.place(x=800, y=180)


    def load_pacific_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="PACIFIC DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_northwest_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command= lambda : load_southwest_divisionframe())

        warriors_button = Button(mainframe, image=warriorsicon, bg="#E65C06", borderwidth=0,
                                 activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "GoldenStateWarriorsRoster", "warriorslogo.png", "https://www.cbssports.com/nba/teams/GS/golden-state-warriors/", "https://www.nba.com/team/1610612744/warriors"))
        clippers_button = Button(mainframe, image=clippersicon, bg="#E65C06", borderwidth=0,
                                 activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "LosAngelesClippersRoster", "clipperslogo.png", "https://www.cbssports.com/nba/teams/LAC/los-angeles-clippers/", "https://www.nba.com/team/1610612746/clippers"))
        lakers_button = Button(mainframe, image=lakersicon, bg="#E65C06", borderwidth=0,
                               activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "LosAngelesLakersRoster", "lakerslogo.png", "https://www.cbssports.com/nba/teams/LAL/los-angeles-lakers/", "https://www.nba.com/team/1610612747/lakers"))
        suns_button = Button(mainframe, image=sunsicon, bg="#E65C06", borderwidth=0,
                             activebackground="black", command= lambda : LoadTeam_page(mainframe, font, "PhoenixSunsRoster", "sunslogo.png", "https://www.cbssports.com/nba/teams/PHO/phoenix-suns/", "https://www.nba.com/team/1610612756/suns"))
        kings_button = Button(mainframe, image=kingsicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "SacramentoKingsRoster", "kingslogo.png","https://www.cbssports.com/nba/teams/SAC/sacramento-kings/", "https://www.nba.com/team/1610612758/kings"))



        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=380,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        warriors_button.place(x=0, y=180)
        clippers_button.place(x=200, y=180)
        lakers_button.place(x=400, y=180)
        suns_button.place(x=600, y=180)
        kings_button.place(x=800, y=180)


    def load_southwest_divisionframe():
        clear_widgets(mainframe)


        division_name = Label(mainframe, text="SOUTHWEST DIVISION", font=(font, 20), fg="#E65C06", bg="black")

        arrowbuttonleft = Button(mainframe,
                                 image=abl,
                                 bg="black",
                                 activebackground="black",
                                 borderwidth=0,
                                 command= lambda : load_pacific_divisionframe())

        arrowbuttonright = Button(mainframe,
                                  image=abr,
                                  bg="black",
                                  activebackground="black",
                                  borderwidth=0,
                                  command= lambda : load_atlantic_divisionframe())

        mavericks_button = Button(mainframe, image=mavericksicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "DallasMavericksRoster", "maverickslogo.png", "https://www.cbssports.com/nba/teams/DAL/dallas-mavericks/","https://www.nba.com/team/1610612742/mavericks"))
        rockets_button = Button(mainframe, image=rocketsicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "HoustonRocketsRoster", "rocketslogo.png", "https://www.cbssports.com/nba/teams/HOU/houston-rockets/", "https://www.nba.com/team/1610612745/rockets"))
        grizzlies_button = Button(mainframe, image=grizzliesicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda :LoadTeam_page(mainframe, font, "MemphisGrizzliesRoster", "grizzlieslogo.png", "https://www.cbssports.com/nba/teams/MEM/memphis-grizzlies/", "https://www.nba.com/team/1610612763/grizzlies"))
        pelicans_button = Button(mainframe, image=pelicansicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "NewOrleansPelicansRoster", "pelicanslogo.png", "https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/", "https://www.nba.com/team/1610612740/pelicans"))
        spurs_button = Button(mainframe, image=spursicon, bg="#E65C06", borderwidth=0,
                              activebackground="black", command=lambda : LoadTeam_page(mainframe, font, "SanAntonioSpursRoster", "spurslogo.png", "https://www.cbssports.com/nba/teams/SA/san-antonio-spurs/", "https://www.nba.com/team/1610612759/spurs"))




        arrowbuttonright.place(x=680,y=90)
        arrowbuttonleft.place(x=250,y=90)

        division_name.place(x=365,y=100)


       # arrowbuttonleft.place(x=200, y=200)
       # arrowbuttonright.place(x=800, y=200)

        mavericks_button.place(x=0, y=180)
        rockets_button.place(x=200, y=180)
        grizzlies_button.place(x=400, y=180)
        pelicans_button.place(x=600, y=180)
        spurs_button.place(x=800, y=180)

    load_atlantic_divisionframe()


def loadplayerspage():

    clear_widgets(mainframe)
    mainframe.configure(bg="#E65C06")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    fllwpagelabel = Label(mainframe, text="PLAYERS \n PAGE", font=(font, 30), bg="white", fg="black")
    fllwpagelabel.place(x=200, y=200)

def loadscorespage():

    clear_widgets(mainframe)
    mainframe.configure(bg="black")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    fllwpagelabel = Label(mainframe, text="GAMES", font=(font, 30), bg="black", fg="#E65C06")
    fllwpagelabel.place(x=0, y=0)

def loadstandingtable():

    clear_widgets(mainframe)
    mainframe.configure(bg="black")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

# Eastern Conference Table

    EastConlabel = Label(mainframe, text="Eastern Conference Standings", font=(font, 20), fg="#E65C06", bg="black")
    EastConlabel.place(x=0,y=0)


    driver.get("https://www.cbssports.com/nba/standings/")
    table = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="TableBase-1"]/div/div/table/tbody""")))

    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_data = [cell.text for cell in cells]

        data.append(cell_data)


    tablelist = ttk.Treeview(mainframe)
    tablelist["columns"] = ('Position', "Team", "W", "L", "PCT", "GB", "PPG", "OPPG", "DIFF", "Home", "Road", "DIV", "CONF", "STREAK", "L10", "WP", "DIVP", "POST")

    tablelist.column('#0', width=0)
    tablelist.column('Position', width=50)
    tablelist.column('Team', width=100)
    tablelist.column('W', width=50)
    tablelist.column('L', width=50)
    tablelist.column('PCT', width=50)
    tablelist.column('GB', width=50)
    tablelist.column('PPG', width=50)
    tablelist.column('OPPG', width=50)
    tablelist.column('DIFF', width=50)
    tablelist.column('Home', width=50)
    tablelist.column('Road', width=50)
    tablelist.column('DIV', width=50)
    tablelist.column('CONF', width=50)
    tablelist.column('STREAK', width=50)
    tablelist.column('L10', width=50)
    tablelist.column('WP', width=50)
    tablelist.column('DIVP', width=50)
    tablelist.column('POST', width=70)

    tablelist.heading('#0', text="")
    tablelist.heading('Position', text='Position')
    tablelist.heading('Team', text="Team")
    tablelist.heading('W', text='W')
    tablelist.heading('L', text='L')
    tablelist.heading('PCT', text='PCT')
    tablelist.heading('GB', text='GB')
    tablelist.heading('PPG', text='PPG')
    tablelist.heading('OPPG', text='OPPG')
    tablelist.heading('DIFF', text='DIFF')
    tablelist.heading('Home', text='HOME')
    tablelist.heading('Road', text='ROAD')
    tablelist.heading('DIV', text='DIV')
    tablelist.heading('CONF', text='CONF')
    tablelist.heading('STREAK', text='STREAK')
    tablelist.heading('L10', text='L10')
    tablelist.heading('WP', text='WP')
    tablelist.heading('DIVP', text='DIVP')
    tablelist.heading('POST', text='POST')


    for r in data:
        tablelist.insert('','end', values=r)

    tablelist.place(x=0, y=40)
    #tablelist.pack(fill='both', expand=True)

# Western Conference Table

    WestConlabel = Label(mainframe, text="Western Conference Standings", font=(font, 20), fg="#E65C06", bg="black")
    WestConlabel.place(x=0, y=270)

    driver.get("https://www.cbssports.com/nba/standings/")
    table2 = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="TableBase-2"]/div/div/table/tbody""")))

    rows = table2.find_elements(By.TAG_NAME, "tr")
    data = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_data = [cell.text for cell in cells]

        data.append(cell_data)

    tablelist2 = ttk.Treeview(mainframe)
    tablelist2["columns"] = (
    'Position', "Team", "W", "L", "PCT", "GB", "PPG", "OPPG", "DIFF", "Home", "Road", "DIV", "CONF", "STREAK", "L10",
    "WP", "DIVP", "POST")

    tablelist2.column('#0', width=0)
    tablelist2.column('Position', width=50)
    tablelist2.column('Team', width=100)
    tablelist2.column('W', width=50)
    tablelist2.column('L', width=50)
    tablelist2.column('PCT', width=50)
    tablelist2.column('GB', width=50)
    tablelist2.column('PPG', width=50)
    tablelist2.column('OPPG', width=50)
    tablelist2.column('DIFF', width=50)
    tablelist2.column('Home', width=50)
    tablelist2.column('Road', width=50)
    tablelist2.column('DIV', width=50)
    tablelist2.column('CONF', width=50)
    tablelist2.column('STREAK', width=50)
    tablelist2.column('L10', width=50)
    tablelist2.column('WP', width=50)
    tablelist2.column('DIVP', width=50)
    tablelist2.column('POST', width=70)

    tablelist2.heading('#0', text="")
    tablelist2.heading('Position', text='Position')
    tablelist2.heading('Team', text="Team")
    tablelist2.heading('W', text='W')
    tablelist2.heading('L', text='L')
    tablelist2.heading('PCT', text='PCT')
    tablelist2.heading('GB', text='GB')
    tablelist2.heading('PPG', text='PPG')
    tablelist2.heading('OPPG', text='OPPG')
    tablelist2.heading('DIFF', text='DIFF')
    tablelist2.heading('Home', text='HOME')
    tablelist2.heading('Road', text='ROAD')
    tablelist2.heading('DIV', text='DIV')
    tablelist2.heading('CONF', text='CONF')
    tablelist2.heading('STREAK', text='STREAK')
    tablelist2.heading('L10', text='L10')
    tablelist2.heading('WP', text='WP')
    tablelist2.heading('DIVP', text='DIVP')
    tablelist2.heading('POST', text='POST')

    for r in data:
        tablelist2.insert('', 'end', values=r)

    tablelist2.place(x=0, y=310)




def loadhomepage():

    clear_widgets(mainframe)
    mainframe.configure(bg="white")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    fllwpagelabel = Label(mainframe, text="HOME \n PAGE", font=(font, 30), bg="white", fg="black")
    #fllwpagelabel.place(x=200, y=200)


def loadloginpage():

    clear_widgets(mainframe)
    mainframe.config(bg="black")

    loginframe = Frame(mainframe, bg="black")
    loginframe.place(x=327,y=30)

    logo = Label(loginframe, image=iconimg2, borderwidth=0)

    usernamelabel = Label(loginframe, text="Enter Username: ", bg="black", fg="#E65C06", font=(font, 15))
    username_entry = Entry(loginframe, width=40, borderwidth=0)

    passwordlabel = Label(loginframe, text="Enter Password: ", bg="black", fg="#E65C06", font=(font, 15))
    password_entry = Entry(loginframe, width=40, borderwidth=0)

    loginbutton = Button(
        loginframe,
        text="⚫ Log In ⚫",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0)

  #  backbutton = Button(
  #      loginframe,
  #      text="Back",
  #      font=(font, 15),
  #      cursor="hand2",
  #      bg="black",
  #      fg="#E65C06",
  #      borderwidth=0,
  #  )

    logo.grid(row=0,columnspan=3, pady=20)

    usernamelabel.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)

    passwordlabel.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)

    loginbutton.grid(row=3, columnspan=3, pady=10)
    #backbutton.grid(row=4, columnspan=3, pady=0)

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

def password_email_validator(pw, rpw, email, name, username):

    if len(pw) < 5:
        tkinter.messagebox.showinfo(title=f" '{pw}' Too short", message="Password too short, password must be more that 6 characters long")
        password_email_validator(pw, rpw, email, name, username)

    elif not re.search('[!"£$%^&*()<>,._¬-]', pw):
        tkinter.messagebox.showinfo(title="Password to weak", message="Password too weak, add symbol to password")
        password_email_validator(pw, rpw, email, name, username)

    elif not re.search('[1234567890]', pw):
        tkinter.messagebox.showinfo(title="Password to weak", message="Password too weak, add numbers to password")
        password_email_validator(pw, rpw, email, name, username)

    elif not re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', pw):
        tkinter.messagebox.showinfo(title="Password too weak", message="Password too weak, add upper case letters to your password")
        password_email_validator(pw, rpw, email, name, username)

    elif rpw != pw:
        tkinter.messagebox.showinfo(title="Passwords dont match", message="The passwords you have entered do not match")
        password_email_validator(pw, rpw, email, name, username)

    elif not re.search('@', email):
        tkinter.messagebox.showinfo(title="Invalid Email", message="Email address is invalid")
        password_email_validator(pw, rpw, email, name, username)

    elif not re.search('.com' or '.co.uk', email):
        tkinter.messagebox.showinfo(title="Invalid Email", message="Email address is invalid")
        password_email_validator(pw, rpw, email, name, username)

    else:

        tkinter.messagebox.showinfo(title="Password Created", message="Password Valid")

        con = sqlite3.connect('classes.db')
        c = con.cursor()

        name = str(name)
        email = str(email)
        username = str(username)
        password = str(pw)


        def insert_user(n,e,u,p):
            with con:
                c.execute("INSERT INTO Users VALUES (:first, :email, :username, :password )",
                          {'first': name, 'email': email, 'username': username,
                           'password': password})
                con.commit()

        insert_user(name,email,username,password)

def loadsignuppage():

    clear_widgets(mainframe)

    signupframe = Frame(mainframe, bg="black")
    signupframe.place(x=300,y=5)

    mainframe.tkraise()
    mainframe.config(bg="black")


    scrollbar = Scrollbar(mainframe, orient="vertical")
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')


    mylist = Listbox(signupframe, yscrollcommand=scrollbar.set)

    for i in range(100):
        mylist.insert(END, f"this is some text\n {i}")

    scrollbar.config(command=mylist.yview())
    mylist.grid

    logo = Label(signupframe, image=iconimg2, borderwidth=0)

    namelabel = Label(signupframe, text="Name: ", bg="black", fg="#E65C06", font=(font, 15))
    user_name = Entry(signupframe, width=40, borderwidth=0)

    emaillabel = Label(signupframe, text="Enter email: ", bg="black", fg="#E65C06", font=(font, 15))
    user_email = Entry(signupframe, width=40, borderwidth=0)

    usernamelabel = Label(signupframe, text="Create your username: ", bg="black", fg="#E65C06", font=(font, 15))
    username = Entry(signupframe, width=40, borderwidth=0)

    passwordlabel = Label(signupframe, text="Create password: ", bg="black", fg="#E65C06", font=(font, 15))
    password_entry = Entry(signupframe, width=40, borderwidth=0)

    repasswordlabel = Label(signupframe, text="Re-enter password: ", bg="black", fg="#E65C06", font=(font, 15))
    repassword_entry = Entry(signupframe, width=40, borderwidth=0)



    createuserbutton =Button(
        signupframe,
        text="⚫ Create Account ⚫",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0,
        command=lambda: [password_email_validator(password_entry.get(),
                                                  repassword_entry.get(),
                                                  user_email.get(),
                                                  user_name.get(),
                                                  username.get())])

    
    logo.grid(row=0, columnspan=3, pady=10)

    namelabel.grid(row=1, column=0)
    user_name.grid(row=1, column=1)

    emaillabel.grid(row=2, column=0)
    user_email.grid(row=2, column=1)

    usernamelabel.grid(row=3, column=0)
    username.grid(row=3, column=1)

    passwordlabel.grid(row=4, column=0)
    password_entry.grid(row=4, column=1)

    repasswordlabel.grid(row=5, column=0)
    repassword_entry.grid(row=5, column=1)

    createuserbutton.grid(row=6, columnspan=3, pady=20)
    #backbutton.grid(row=7, columnspan=3)



def loadfollowingpage():

    clear_widgets(mainframe)
    mainframe.config(bg="orange")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    fllwpagelabel = Label(mainframe, text="FOLLOWING \n PAGE", font=(font, 30), bg="white", fg="black")
    fllwpagelabel.place(x=200, y=200)


def ACC():




    clear_widgets(mainframe)
    mainframe.config(bg="black")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    settingslabel = Label(mainframe, text="Account Customisation", font=(font, 30), bg="black", fg="white")
    settingslabel.place(x=200, y=50)

    changethemelabel = Label(mainframe, text="Change App Theme", font=(font, 18), bg="black", fg="#E65C06")
    changethemelabel.place(x=300, y=150)

    lightmodebutton = Button(mainframe,
                             image=lmb,
                             bg="black",
                             borderwidth=0,
                             activebackground="black",
                             command=lambda : [lightmode(mainframe), light_mode == True])
    lightmodebutton.place(x=400, y=200)

    darkmodebutton = Button(mainframe, image=dmb, bg="black", borderwidth=0, activebackground="black")
    darkmodebutton.place(x=400, y=250)


def loadsettings():

    clear_widgets(mainframe)
    mainframe.config(bg="black")

    scrollbar = Scrollbar(mainframe)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    mylist = Listbox(mainframe, yscrollcommand=scrollbar.set)
    scrollbar.config(command=mylist.yview)

    settingslabel = Label(mainframe, text="SETTINGS", font=(font, 30), bg="black", fg="white")
    settingslabel.place(x=200, y=50)

    as_settingslabel = Button(mainframe,
                              text="Account Settings",
                              font=(font, 18),
                              bg="black",
                              fg="#E65C06",
                              borderwidth=0,
                              activebackground="#E65C06"
                              )

    as_settingslabel.place(x=320, y=150)

    ac_settingslabel = Button(mainframe,
                              text="Account customisation",
                              font=(font, 18),
                              bg="black",
                              fg="#E65C06",
                              borderwidth=0,
                              activebackground="#E65C06",
                              command= lambda : ACC()
                              )
    ac_settingslabel.place(x=320, y=200)


def menu():

    global menuframe
    menuframe = Frame(root, bg="black", width=210, height=800)
    menuframe.place(x=0, y=100)
    menuframe.tkraise()

    def hide_indicators():
        homeindicator.config(bg="black")
        loginindicator.config(bg="black")
        signupindicator.config(bg="black")
        followingindicator.config(bg="black")
        settingsindicator.config(bg="black")

        home_button.config(fg="#E65C06")
        login_button.config(fg="#E65C06")
        signup_button.config(fg="#E65C06")
        following_button.config(fg="#E65C06")
        settings_button.config(fg="#E65C06")

    def indicate(idc, button):
        hide_indicators()
        idc.config(bg="#E65C06")
        button.config(fg="white")

    menulabel = Label(menuframe, bg="black",
                      text="MENU",
                      fg="white",
                      font=(font, 30))
    menulabel.place(x=20, y=120)

    menubutton = Button(menuframe,
                        image=menuimg,
                        bg="black",
                        borderwidth=0,
                        activebackground="black",
                        command=lambda : [menuframe.destroy()]

                        )
    menubutton.place(x=70, y=18)

    home_button = Button(menuframe,
                         text="HOME",
                         fg="#E65C06",
                         bg="black",
                         borderwidth=0,
                         activebackground="#E65C06",
                         activeforeground="black",
                         font=(font, 22),
                         command=lambda:  [indicate(homeindicator, home_button), homepage(mainframe, font), menuframe.tkraise()])

    homeindicator = Label(menuframe, text="", bg="black")
    homeindicator.place(x=7, y=207, width=5, height=40)

    home_button.place(x=10, y=200)

    lgb = PhotoImage(file="login button.png")
    sub = PhotoImage(file="signupbutton2.png")

    login_button = Button(menuframe,
                          text="LOG IN",
                          fg="#E65C06",
                          bg="black",
                          borderwidth=0,
                          activebackground="#E65C06",
                          activeforeground="black",
                          font=(font, 22),
                          command=lambda: [indicate(loginindicator, login_button), loadloginpage(), menuframe.tkraise()])

    loginindicator = Label(menuframe, text="", bg="black")
    loginindicator.place(x=7, y=267, width=5, height=40)

    login_button.place(x=12, y=260)

    signup_button = Button(menuframe,
                           text="SIGN UP",
                           fg="#E65C06",
                           bg="black",
                           borderwidth=0,
                           activebackground="#E65C06",
                           activeforeground="black",
                           font=(font, 22),
                           command=lambda: [indicate(signupindicator, signup_button), loadsignuppage(), menuframe.tkraise()])

    signupindicator = Label(menuframe, text="", bg="black")
    signupindicator.place(x=7, y=327, width=5, height=40)

    signup_button.place(x=10, y=320)

    following_button = Button(menuframe,
                              text="FOLLOWING",
                              fg="#E65C06",
                              bg="black",
                              borderwidth=0,
                              activebackground="#E65C06",
                              activeforeground="black",
                              font=(font, 22),
                              command=lambda: [indicate(followingindicator, following_button), loadfollowingpage(), menuframe.tkraise()])

    followingindicator = Label(menuframe, text="", bg="black")
    followingindicator.place(x=7, y=387, width=5, height=40)

    following_button.place(x=10, y=380)

    settings_button = Button(menuframe,
                             text="SETTINGS",
                             fg="#E65C06",
                             bg="black",
                             borderwidth=0,
                             activebackground="#E65C06",
                             activeforeground="black",
                             font=(font, 22),
                             command=lambda: [indicate(settingsindicator, settings_button),loadsettings(), menuframe.tkraise()])

    settingsindicator = Label(menuframe, text="", bg="black")
    settingsindicator.place(x=7, y=447, width=5, height=40)

    settings_button.place(x=10, y=440)


labelline = Label(logoframe, text="", bg="#E65C06", height=0, width=60)
labelline.place(x=0,y=50)

labelline2 = Label(logoframe, text="", bg="#E65C06", height=0, width=100)
labelline2.place(x=700,y=50)

menubutton = Button(optionsframe, borderwidth=0, image=menuimg, bg="black", activebackground="black", command= lambda : menu())
menubutton.place(x=70, y=18)

settingsbutton = Button(optionsframe, borderwidth=0, image=settingicon,activebackground="black", bg="black", command= lambda : loadsettings())
settingsbutton.place(x=900,y=18)

logo = Label(logoframe, image=iconimg, borderwidth=0)
apptitle = Label(logoframe, text="NBA NEWS", borderwidth=0, font=(font,25), fg="white", bg="black")
apptitle.place(x=500, y=40)
logo.place(x=400, y=20)



def hide_indicators():
    teamsindicator.config(bg="black")
    playersindicator.config(bg="black")
    scoresindicator.config(bg="black")
    standingsindicator.config(bg="black")

    teams_button.config(fg="#E65C06")
    players_button.config(fg="#E65C06")
    scores_button.config(fg="#E65C06")
    standings_button.config(fg="#E65C06")


def indicate(idc, button):
    hide_indicators()
    idc.config(bg="#E65C06")
    button.config(fg="white")


lgb = PhotoImage(file="login button.png")
sub = PhotoImage(file="signupbutton2.png")

teams_button = Button(optionsframe,
                      text="TEAMS",
                      fg="#E65C06",
                      bg="black",
                      borderwidth=0,
                      activebackground="#E65C06",
                      activeforeground="black",
                      font=(font, 20),
                      command=lambda: [indicate(teamsindicator,teams_button), loadteamspage()])

teamsindicator = Label(optionsframe, text="", bg="black")
teamsindicator.place(x=210, y=27, width=5, height=40)

teams_button.place(x=220, y=20)



players_button = Button(optionsframe,
                       text="PLAYERS",
                       fg="#E65C06",
                       bg="black",
                       borderwidth=0,
                       activebackground="#E65C06",
                       activeforeground="black",
                       font=(font, 20),
                       command=lambda: [indicate(playersindicator, players_button), league_leaders(mainframe, font)])

playersindicator = Label(optionsframe, text="", bg="black")
playersindicator.place(x=350, y=27, width=5, height=40)
players_button.place(x=360, y=20)

scores_button = Button(optionsframe,
                          text="SCORES",
                          fg="#E65C06",
                          bg="black",
                          borderwidth=0,
                          activebackground="#E65C06",
                          activeforeground="black",
                          font=(font, 20),
                          command=lambda: [indicate(scoresindicator, scores_button), scorecards_(mainframe, font)])

scoresindicator = Label(optionsframe, text="", bg="black")
scoresindicator.place(x=520, y=27, width=5, height=40)

scores_button.place(x=530, y=20)

standings_button = Button(optionsframe,
                         text="STANDINGS",
                         fg="#E65C06",
                         bg="black",
                         borderwidth=0,
                         activebackground="#E65C06",
                         activeforeground="black",
                         font=(font, 20),
                         command=lambda: [indicate(standingsindicator, standings_button), loadstandingtable()])

standingsindicator = Label(optionsframe, text="", bg="black")
standingsindicator.place(x=680, y=27, width=5, height=40)
standings_button.place(x=690, y=20)



homepageframe = Frame(root, bg="#E65C06")
followingframe = Frame(root, bg="#E65C06")
settingsframe = Frame(root, bg="#E65C06")

logoframe.place(x=0,y=0)



optionsframe.place(x=0,y=100)
optionsframe.propagate(False)

loadhomepage()
root.mainloop()