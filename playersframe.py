import sqlite3

import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import Tk, Frame, Button, Label

import time

import urllib.request
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clear_widgets(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def league_leaders(frame, font):

    clear_widgets(frame)


    frame.configure(bg="black")
    Heading = Label(frame, text="League Leaders", bg="black", fg="white", borderwidth=0, font=(font,25))
    Heading.place(x=20, y=30)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

    driver.get("https://www.nba.com/stats/players")


    # ppg leaders table
    ppgtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[1]/div""")
    ppgleaders = ppgtable.find_elements(By.TAG_NAME, value="a")
    ppgdata = []



    for leader in ppgleaders:
        ppgdata.append(leader.text)

    ppgheading = Label(frame, text="Points Per Game", bg="black", fg="grey", font=(font,17), borderwidth=0)
    ppgheading.place(x=130, y=80)


    p = 110

    for player in ppgdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=150, y=p)
        p = p + 30



    # rpg leaders table
    rpgtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[2]/div""")
    rpgleaders = rpgtable.find_elements(By.TAG_NAME, value="tr")
    rpgdata = []

    rpgheading = Label(frame, text="Rebounds Per Game", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    rpgheading.place(x=580, y=80)

    for leader in rpgleaders:
        rpgdata.append(leader.text)

    r = 110

    for player in rpgdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=600, y=r)
        r = r + 30


    # apg leaders table
    apgtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[3]/div""")
    apgleaders = apgtable.find_elements(By.TAG_NAME, value="tr")
    apgdata = []



    for leader in apgleaders:
        apgdata.append(leader.text)

    apgheading = Label(frame, text="Assists Per Game", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    apgheading.place(x=130, y=280)

    a = 310

    for player in apgdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=150, y=a)
        a = a + 30



    # bpg leaders table
    bpgtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[4]/div/table""")
    bpgleaders = bpgtable.find_elements(By.TAG_NAME, value="tr")
    bpgdata = []

    bpgheading = Label(frame, text="Blocks Per Game", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    bpgheading.place(x=580, y=280)

    for leader in bpgleaders:
        bpgdata.append(leader.text)


    b = 310


    for player in bpgdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=600, y=b)
        b = b + 30

    page2 = Button(frame, text="⦿ page 2 ⦿", bg="black", fg="#E65C06", font=(font,12), borderwidth=0, command=lambda : league_leaders2(frame, font))
    page2.place(x=470, y=500)
    ########################################################################
    spl = Label(frame, text="Search Player:", font=(font,15), bg="black",  fg="grey")
    spl.place(x=350, y= 10)

    search_query = tk.StringVar()

    searchbar = ttk.Entry(frame, textvariable=search_query)
    searchbar.place(x=500, y=10, width=400, height=20)


    def perform_search(frame, root):


        clear_widgets(frame)
        player = search_query.get()
        fs_name = player.split()

        print(fs_name)

        backgroundframe = Frame(frame, bg="black", width=810, height=260, highlightbackground="#E65C06",highlightthickness=5)
        backgroundframe2 = Frame(frame, bg="black", width=800, height=250, borderwidth=5)

        backgroundframe.place(x=70, y=20)
        backgroundframe2.place(x=75, y=25)

        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
        driver = webdriver.Chrome(service=Path, options=option)

        driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiQnq38xY3-AhWREMAKHYoqDwEQPAgI")
        # the web driver will access the Google website by its url link
        driver.find_element(By.XPATH, value="""//*[@id="L2AGLb"]/div""").click()
        # the driver then locates and clicks the button to agree to the terms and services opf google

        searchbargoogle = driver.find_element(By.XPATH,value="""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""")
        # the web driver will then locate the search bar in google by its XPATH
        searchbargoogle.send_keys(f"cbs sports {player}")
        # the automation bots will then send keys/characters to google's search bar
        searchbargoogle.send_keys(Keys.RETURN)
        # after sending the keys it will then send the enter key to submit its input


        #the first result of the search being accessed
        search_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g')))
        # line of code used to locate all the results currently on the web page and thier links
        first_result = search_results[0] # finds the first results from the search as it will find it by index 0

        first_link = first_result.find_element(By.TAG_NAME, value='a')
        # finds the web link of the website that has the information on the plater
        first_link_url = first_link.get_attribute('href')
        # the driver then locates and fetches the attribute of the link, being the hyperlink
        # which comes under the class of 'href'

        driver.get(first_link_url) # once the hyperlink is found the bots will then access this web page

        driver.get(first_link_url)
        playerimg = driver.find_element(By.XPATH,value="""/html/body/div[4]/aside/div/div[3]/div[1]/div/a/div/div/figure/img""")
        # finds the profile image of the player in the website
        image_url = playerimg.get_attribute("src")
        # fetches the source link of the image
        print(image_url) # printing the src link in the python console to test if it actually did collect it
        urllib.request.urlretrieve(image_url, "image.jpg")
        # this line of code will then retrieve the source link and create a new file being 'image.jpg' that contains the image

        playerphoto = PhotoImage(file="image.jpg")
        # a photo image is created under the photoimage class by tkinter of the image file
        label = Label(frame, image=playerphoto)
        # a label is created containing the player's proflie image from the 'image.jpg' file
        label.image = playerphoto


        label.place(x=0, y=50)

        firstname = fs_name[0]
        surname = fs_name[1]

        driver.get(f"https://www.landofbasketball.com/nba_players/{firstname.lower()}_{surname.lower()}.htm")

        name = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]""")
        team = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]""")
        position = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]""")
        jerseynumber = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]""")

        height = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]""")
        weight = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[6]/td[2]""")
        born = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[7]/td[2]""")
        highschool = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[8]/td[2]""")
        college = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[9]/td[2]""")

        drafted = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[10]/td[2]""")
        seasons = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[11]/td[2]""")
        playoffs = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[12]/td[2]""")
        titles = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[13]/td[2]""")
        all_star = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[14]/td[2]""")

        sznslabel = Label(backgroundframe2, text="SEASON STATS:", bg="black", fg="grey", borderwidth=0, font=(font, 15))
        sznslabel.place(x=550, y=10)

        sttable = []
        statstable = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/div[8]/div[2]/table/tbody/tr[2]""")
        #locates the table of the player's stats
        stats = statstable.find_elements(By.TAG_NAME, value="td")
        # locates each row in the bale
        for x in stats:
            sttable.append(x.text)
            # loops through the rows and adds the values into the stttable list in text format

        sttable.pop(0)
        # deletes the first row with is the headings of the table

        t = 40

        for x in sttable:
            stat = tk.Button(backgroundframe2, text=f"{x}", fg="#E65C06", bg="black", font=(font, 12), borderwidth=0)
            stat.place(x=700, y=t)
            t = t + 27

        recordingstable = []
        recordings = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/div[8]/div[2]/table/tbody/tr[1]""")
        record = recordings.find_elements(By.TAG_NAME, value="td")
        for y in record:
            recordingstable.append(y.text)

        recordingstable.pop(0)

        t = 40

        for y in recordingstable:
            stat = tk.Button(backgroundframe2, text=f"{y.upper()}: ", fg="white", bg="black", font=(font, 12), borderwidth=0)
            stat.place(x=570, y=t)
            t = t + 27

        print(name.text)
        print(team.text)
        print(position.text)
        print(jerseynumber.text[:2])

        nlabel = Label(backgroundframe2, text=f"NAME:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        tlabel = Label(backgroundframe2, text=f"TEAM:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        plabel = Label(backgroundframe2, text=f"POSITION:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        Nlabel = Label(backgroundframe2, text=f"JERSEY NO:", borderwidth=0, fg="white", bg="black", font=(font, 12))

        namelabel = Label(backgroundframe2, text=f"{name.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        teamlabel = Label(backgroundframe2, text=f"{team.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        poslabel = Label(backgroundframe2, text=f"{position.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        NOlabel = Label(backgroundframe2, text=f"#{jerseynumber.text[:2]} ({team.text})", borderwidth=0, fg="#E65C06", bg="black",
                        font=(font, 12))

        nlabel.place(x=100, y=20)
        tlabel.place(x=100, y=40)
        plabel.place(x=100, y=60)
        Nlabel.place(x=100, y=80)

        namelabel.place(x=210, y=20)
        teamlabel.place(x=210, y=40)
        poslabel.place(x=210, y=60)
        NOlabel.place(x=210, y=80)

        hlabel = Label(backgroundframe2, text=f"HEIGHT:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        wlabel = Label(backgroundframe2, text=f"WEIGHT:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        blabel = Label(backgroundframe2, text=f"BORN:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        hslabel = Label(backgroundframe2, text=f"HISCHOOL:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        collabel = Label(backgroundframe2, text=f"COLLEGE:", borderwidth=0, fg="white", bg="black", font=(font, 12))

        heightlabel = Label(backgroundframe2, text=f"{height.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        weightlabel = Label(backgroundframe2, text=f"{weight.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        bornlabel = Label(backgroundframe2, text=f"{born.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        highschoollabel = Label(backgroundframe2, text=f"{highschool.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
        collegelabel = Label(backgroundframe2, text=f"{college.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))

        hlabel.place(x=100, y=120)
        wlabel.place(x=100, y=140)
        blabel.place(x=100, y=160)
        hslabel.place(x=100, y=180)
        collabel.place(x=100, y=200)

        heightlabel.place(x=210, y=120)
        weightlabel.place(x=210, y=140)
        bornlabel.place(x=210, y=160)
        highschoollabel.place(x=210, y=180)
        collegelabel.place(x=210, y=200)

        drafted = drafted.text.split()
        print(drafted)

        if len(drafted) == 17:
            drafted0 = drafted[0]
            drafted1 = drafted[1]
            drafted2 = drafted[2]
            drafted3 = drafted[3]
            drafted5 = drafted[5]
            drafted6 = drafted[6]

            drafted10 = drafted[10]
            drafted11 = drafted[11]

            drafted14 = drafted[14]
            drafted15 = drafted[15]
            drafted16 = drafted[16]

            draftedlabel = Label(frame,
                                 text=f"Drafted {drafted0} {drafted1} {drafted2} {drafted3},\n {drafted5} {drafted6},"
                                      f" {drafted10} {drafted11}, {drafted14} {drafted15} {drafted16} ", borderwidth=0,
                                 fg="#E65C06", bg="black", font=(font, 12))

        elif len(drafted) == 18:

            drafted0 = drafted[0]
            drafted1 = drafted[1]
            drafted2 = drafted[2]
            drafted3 = drafted[3]
            drafted4 = drafted[4]
            drafted6 = drafted[6]
            drafted7 = drafted[7]

            drafted11 = drafted[11]
            drafted12 = drafted[12]

            drafted15 = drafted[15]
            drafted16 = drafted[16]
            drafted17 = drafted[17]

            draftedlabel = Label(frame,
                                 text=f"Drafted {drafted0} {drafted1} {drafted2} {drafted3} {drafted4}"
                                      f" \n {drafted6} {drafted7}, {drafted11} {drafted12}, {drafted15} {drafted16} {drafted17} ", borderwidth=0,
                                 fg="#E65C06", bg="black", font=(font, 12))


        dralabel = Label(frame, text=f"DRAFTED:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        slabel = Label(frame, text=f"SEASONS:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        plolabel = Label(frame, text=f"PLAYOFFS:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        ttlabel = Label(frame, text=f"TITLES:", borderwidth=0, fg="white", bg="black", font=(font, 12))
        aslabel = Label(frame, text=f"ALL-STAR:", borderwidth=0, fg="white", bg="black", font=(font, 12))

       # draftedlabel = Label(frame, text=f"Drafted {drafted0} {drafted1} {drafted2} {drafted3},\n {drafted5} {drafted6},"
       #                                  f" {drafted10} {drafted11}, {drafted14} {drafted15} {drafted16} ", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        seasonslabel = Label(frame, text=f"{seasons.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        playoffslabel = Label(frame, text=f"{playoffs.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        titleslabel = Label(frame, text=f"{titles.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
        allstarslabel = Label(frame, text=f"{all_star.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))

        statstable = driver.find_element(By.XPATH, value="""/html/body/div/div[2]/main/div[9]/div/table/tbody""")
        rows = statstable.find_elements(By.TAG_NAME, value="tr")
        # locates the table of career stats and locates each row in the table
        statsdata = []

        for row in rows:
            cs = row.find_elements(By.TAG_NAME, value="td")
            c_data = [c.text for c in cs]
            statsdata.append(c_data)

        # loops through all the rows in the table, converts it to text and adds it to the 'statsdata' table

        careerstats = ttk.Treeview(frame)
        careerstats["columns"] = ("Season", "Team", "Games", "Points", "Rebounds", "Assists", "Steals", "Blocks")
        # creates the columns for the treeview table


        # adjusting the width of each column
        careerstats.column('#0', width=0)
        careerstats.column('Season', width=70)
        careerstats.column('Team', width=80)
        careerstats.column('Games', width=50)
        careerstats.column('Points', width=50)
        careerstats.column('Rebounds', width=50)
        careerstats.column('Assists', width=50)
        careerstats.column('Steals', width=50)
        careerstats.column('Blocks', width=70)

        # assigning headings to each column in the table
        careerstats.heading("#0", text="")
        careerstats.heading("Season", text="Season")
        careerstats.heading("Team", text="Team")
        careerstats.heading("Games", text="Games")
        careerstats.heading("Points", text="Points")
        careerstats.heading("Rebounds", text="Rebounds")
        careerstats.heading("Assists", text="Assists")
        careerstats.heading("Steals", text="Steals")
        careerstats.heading("Blocks", text="Blocks")

        statsdata.pop(0)

        for d in statsdata:
            careerstats.insert('', 'end', values=d)
            # sing a for loop, the data from th table of the player's career stats is inserted into the table

        careerstatslabel = Label(frame, text="CAREER STATS:", font=(font,15), bg="black", fg="grey")
        careerstatslabel.place(x=20, y=315)
        # heading/label for the table

        careerstats.place(x=20, y=340)

        dralabel.place(x=550, y=350)
        slabel.place(x=550, y=390)
        plolabel.place(x=550, y=420)
        ttlabel.place(x=550, y=450)
        aslabel.place(x=550, y=480)

        draftedlabel.place(x=660, y=350)
        seasonslabel.place(x=660, y=390)
        playoffslabel.place(x=660, y=420)
        titleslabel.place(x=660, y=450)
        allstarslabel.place(x=660, y=480)

        # searchbutton = Button(frame, text="search", fg="#E65C06", bg="black", borderwidth=0, command=lambda : perform_search())

    searchbar.bind('<Return>', lambda event: perform_search(frame, font))
    # searchbutton.place(x=500, y=240)


    #     option = webdriver.ChromeOptions()
    #     option.add_argument('headless')
    #
    #     Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    #     driver = webdriver.Chrome(service=Path, options=option)
    #
    #     driver.get("https://www.cbssports.com/nba/players/2892772/ja-morant/")
    #     playerimg = driver.find_element(By.XPATH,value="""/html/body/div[4]/aside/div/div[3]/div[1]/div/a/div/div/figure/img""")
    #     image_url = playerimg.get_attribute("src")
    #     print(image_url)
    #     urllib.request.urlretrieve(image_url, "image.jpg")
    #
    #     playerphoto = PhotoImage(file="image.jpg")
    #     label = Label(frame, image=playerphoto)
    #     label.image = playerphoto
    #
    #     label.place(x=0, y=0)
    #
    #     firstname = fs_name[0]
    #     surname = fs_name[1]
    #
    #     driver.get(f"https://www.landofbasketball.com/nba_players/{firstname.lower()}_{surname.lower()}.htm")
    #
    #     name = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]""")
    #     team = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]""")
    #     position = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]""")
    #     jerseynumber = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]""")
    #
    #     height = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]""")
    #     weight = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[6]/td[2]""")
    #     born = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[7]/td[2]""")
    #     highschool = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[8]/td[2]""")
    #     college = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[9]/td[2]""")
    #     drafted = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[10]/td[2]""")
    #
    #     seasons = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[11]/td[2]""")
    #     playoffs = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[12]/td[2]""")
    #     titles = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[13]/td[2]""")
    #     all_star = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/table[1]/tbody/tr[2]/td/div/table/tbody/tr[14]/td[2]""")
    #
    #
    #     sznslabel = Label(frame, text="SEASON STATS:", bg="black", fg="grey",borderwidth=0, font=(font,20))
    #     sznslabel.place(x=680,y=5)
    #
    #     sttable = []
    #     statstable = driver.find_element(By.XPATH,value="""/html/body/div[2]/div[2]/main/div[8]/div[2]/table/tbody/tr[2]""")
    #     stats = statstable.find_elements(By.TAG_NAME, value="td")
    #     for x in stats:
    #         sttable.append(x.text)
    #
    #     sttable.pop(0)
    #
    #     t=40
    #
    #     for x in sttable:
    #         stat = tk.Button(frame, text=f"{x}", fg="#E65C06", bg="black", font=(font, 12), borderwidth=0)
    #         stat.place(x=850, y=t)
    #         t = t + 32
    #
    #     recordingstable = []
    #     recordings = driver.find_element(By.XPATH, value="""/html/body/div[2]/div[2]/main/div[8]/div[2]/table/tbody/tr[1]""")
    #     record = recordings.find_elements(By.TAG_NAME, value="td")
    #     for y in record:
    #         recordingstable.append(y.text)
    #
    #     recordingstable.pop(0)
    #
    #     t = 40
    #
    #     for y in recordingstable:
    #         stat = tk.Button(frame, text=f"{y.upper()}: ", fg="white", bg="black", font=(font, 15), borderwidth=0)
    #         stat.place(x=700, y=t)
    #         t = t + 30
    #
    #     print(name.text)
    #     print(team.text)
    #     print(position.text)
    #     print(jerseynumber.text[:2])
    #
    #     nlabel = Label(frame, text=f"NAME:", borderwidth=0, fg="white", bg="black", font=(font,12))
    #     tlabel = Label(frame, text=f"TEAM:", borderwidth=0, fg="white", bg="black", font=(font,12))
    #     plabel = Label(frame, text=f"POSITION:", borderwidth=0, fg="white", bg="black", font=(font,12))
    #     Nlabel = Label(frame, text=f"JERSEY NO:", borderwidth=0, fg="white", bg="black", font=(font,12))
    #
    #     namelabel = Label(frame, text=f"{name.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     teamlabel = Label(frame, text=f"{team.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     poslabel = Label(frame, text=f"{position.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
    #     NOlabel = Label(frame, text=f"#{jerseynumber.text[:2]} ({team.text})", borderwidth=0,fg="#E65C06", bg="black", font=(font, 12))
    #
    #     nlabel.place(x=200, y=20)
    #     tlabel.place(x=200, y=40)
    #     plabel.place(x=200, y=60)
    #     Nlabel.place(x=200, y=80)
    #
    #     namelabel.place(x=310, y=20)
    #     teamlabel.place(x=310, y=40)
    #     poslabel.place(x=310, y=60)
    #     NOlabel.place(x=310, y=80)
    #
    #     hlabel = Label(frame, text=f"HEIGHT:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     wlabel = Label(frame, text=f"WEIGHT:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     blabel = Label(frame, text=f"BORN:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     hslabel = Label(frame, text=f"HISCHOOL:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     collabel = Label(frame, text=f"COLLEGE:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     dralabel = Label(frame, text=f"DRAFTED:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #
    #     heightlabel = Label(frame, text=f"{height.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     weightlabel = Label(frame, text=f"{weight.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     bornlabel = Label(frame, text=f"{born.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     highschoollabel = Label(frame, text=f"{highschool.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
    #
    #     collegelabel = Label(frame, text=f"{college.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
    #     draftedlabel = Label(frame, text=f"{drafted.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
    #
    #     hlabel.place(x=200, y=120)
    #     wlabel.place(x=200, y=140)
    #     blabel.place(x=200, y=160)
    #     #hslabel.place(x=100, y=180)
    #     collabel.place(x=200, y=180)
    #     # dralabel.place(x=500, y=120)
    #
    #     heightlabel.place(x=310, y=120)
    #     weightlabel.place(x=310, y=140)
    #     bornlabel.place(x=310, y=160)
    #     #highschoollabel.place(x=210, y=180)
    #     collegelabel.place(x=310, y=180)
    #     # draftedlabel.place(x=610, y=120)
    #
    #     slabel = Label(frame, text=f"SEASON:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     plolabel = Label(frame, text=f"PLAYOFFS:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     ttlabel = Label(frame, text=f"TITLES:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #     aslabel = Label(frame, text=f"ALL-STAR:", borderwidth=0, fg="white", bg="black", font=(font, 12))
    #
    #     seasonslabel = Label(frame, text=f"{seasons.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     playoffslabel = Label(frame, text=f"{playoffs.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     titleslabel = Label(frame, text=f"{titles.text}", borderwidth=0, fg="#E65C06", bg="black", font=(font, 12))
    #     allstarslabel = Label(frame, text=f"{all_star.text}", borderwidth=0, fg="#E65C06", bg="black",font=(font, 12))
    #
    #     # slabel.place(x=500, y=140)
    #     # plolabel.place(x=500, y=160)
    #     # ttlabel.place(x=500, y=180)
    #     # aslabel.place(x=500, y=200)
    #     #
    #     # seasonslabel.place(x=610, y=140)
    #     # playoffslabel.place(x=610, y=160)
    #     # titleslabel.place(x=610, y=180)
    #     # allstarslabel.place(x=610, y=200)
    #
    # #searchbutton = Button(frame, text="search", fg="#E65C06", bg="black", borderwidth=0, command=lambda : perform_search())
    # searchbar.bind('<Return>', lambda event: perform_search(frame, font))
    # #searchbutton.place(x=500, y=240)

def league_leaders2(frame, font):

    clear_widgets(frame)

    frame.configure(bg="black")
    Heading = Label(frame, text="League Leaders", bg="black", fg="white", borderwidth=0, font=(font, 25))
    Heading.place(x=20, y=30)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

    driver.get("https://www.nba.com/stats/players")


    # spg leaders table
    spgtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[5]/div""")
    spgleaders = spgtable.find_elements(By.TAG_NAME, value="tr")
    spgdata = []


    for leader in spgleaders:
        spgdata.append(leader.text)

    spgheading = Label(frame, text="Steals Per game", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    spgheading.place(x=130, y=80)

    s = 110

    for player in spgdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=150, y=s)
        s = s + 30


    # fgg leaders table
    fgptable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[6]/div""")
    fgpleaders = fgptable.find_elements(By.TAG_NAME, value="tr")
    fgpdata = []


    for leader in fgpleaders:
        fgpdata.append(leader.text)

    fgpheading = Label(frame, text="Field Goal Percentage", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    fgpheading.place(x=580, y=80)

    f = 110

    for player in fgpdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=600, y=f)
        f = f + 30



    # tpm leaders table
    tpmtable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[7]/div""")
    tpmleaders = tpmtable.find_elements(By.TAG_NAME, value="tr")
    tpmdata = []


    for leader in tpmleaders:
        tpmdata.append(leader.text)

    tpmheading = Label(frame, text="Three Points Made", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    tpmheading.place(x=130, y=280)

    t = 310

    for player in tpmdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=150, y=t)
        t = t + 30



    # tpp leaders table
    tpptable = driver.find_element(By.XPATH, value="""//*[@id="players_traditional"]/div[8]/div""")
    tppleaders = tpptable.find_elements(By.TAG_NAME, value="tr")
    tppdata = []

    tppheading = Label(frame, text="Three Point Percentage", bg="black", fg="grey", font=(font, 17), borderwidth=0)
    tppheading.place(x=580, y=280)

    for leader in tppleaders:
        tppdata.append(leader.text)

    b = 310

    for player in tppdata:
        feed = tk.Button(frame, text=f" {player} ", fg="#E65C06", bg="black", font=(font, 15), borderwidth=0)
        feed.place(x=600, y=b)
        b = b + 30

    page1 = Button(frame, text="⦿ page 1 ⦿", bg="black", fg="#E65C06", font=(font, 12), borderwidth=0,
                   command=lambda: league_leaders(frame, font))
    page1.place(x=470, y=500)

