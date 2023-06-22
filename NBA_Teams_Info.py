from selenium import webdriver

from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk, Frame, Button, Label
from tkinter import messagebox

import tkfontchooser
import tkinter
import tkinter as tk
import re
import sqlite3
import tkinter.ttk as ttk

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def clear_widgets(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def LoadTeam_page(frame, font, tablename, logoimage, link1, link2):

    # deletes the widgets in the frame

    clear_widgets(frame)
    frame.configure(bg="black")

    # change
    icon = tkinter.PhotoImage(file=f"{logoimage}")
    logo = Label(frame, image=icon, borderwidth=0, bg="black")
    logo.place(x=10, y=0)
    logo.image = icon

    def loadroster():

        con = sqlite3.connect('NBA teams.db')
        c = con.cursor()

        # change
        c.execute(f'SELECT * FROM {tablename}')
        roster = c.fetchall()

        rosterlist = ttk.Treeview(frame)

        rosterlist["columns"] = ('NO', 'Player', 'POS', 'HT', 'WT', 'DOB', 'EX', 'College')

        rosterlist.column('#0', width=0)
        rosterlist.column('NO', width=50)
        rosterlist.column('Player', width=100)
        rosterlist.column('POS', width=50)
        rosterlist.column('HT', width=50)
        rosterlist.column('WT', width=50)
        rosterlist.column('DOB', width=90)
        rosterlist.column('EX', width=50)
        rosterlist.column('College', width=90)

        rosterlist.heading('#0', text='')
        rosterlist.heading('NO', text="NO")
        rosterlist.heading('Player', text="Player")
        rosterlist.heading('POS', text="POS")
        rosterlist.heading('HT', text="HT")
        rosterlist.heading('WT', text="WT")
        rosterlist.heading('DOB', text="DOB")
        rosterlist.heading('EX', text="EX")
        rosterlist.heading('College', text="College")

        for rows in roster:
            rosterlist.insert('', 'end', values=rows)

        rosterlist.place(x=450, y=270)

        loadrosterbutton2 = Button(frame, text="Roster",
                                   font=(font, 20),
                                   cursor="hand2",
                                   fg="#E65C06",
                                   bg="black",
                                   borderwidth=0,
                                   command=lambda: [rosterlist.destroy(), loadrosterbutton2.destroy()])

        loadrosterbutton2.place(x=60, y=200)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

    # change
    driver.get(link1)

    teamname = driver.find_element(By.ID, 'PageTitle-header')
    teamdescription = driver.find_element(By.CLASS_NAME, 'PageTitle-description')

    teamnameLabel = Label(frame,
                          text=teamname.text,
                          font=(font, 30),
                          bg="black",
                          fg="white")

    teamDescipLabel = Label(frame,
                            text=teamdescription.text,
                            font=(font, 10),
                            bg="black",
                            fg="grey")

    teamnameLabel.place(x=200, y=30)
    teamDescipLabel.place(x=200, y=80)

    loadrosterbutton = Button(frame, text="Roster",
                              font=(font, 20),
                              cursor="hand2",
                              fg="#E65C06",
                              bg="black",
                              borderwidth=0,
                              command=lambda: loadroster())

    loadrosterbutton.place(x=60, y=200)

    hds = Label(frame, text="Top Headlines:", fg="grey", bg="black", font=(font, 20))
    hds.place(x=550, y=270)

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

    # change
    driver.get(link1)

    table = driver.find_element(By.XPATH, value="""/html/body/div[4]/div/main/div[2]/section[2]/ul""")
    headlines = table.find_elements(By.TAG_NAME, value='h3')

    data = []

    for headline in headlines:
        data.append(headline.text)

    t = 320

    for d in data:
        feed = tk.Button(frame, text=f"⦿ {d} ", fg="#E65C06", bg="black", font=(font, 12), borderwidth=0)
        feed.place(x=555, y=t)
        t = t + 30

    backgroundframe = Frame(frame, bg="black", width=410, height=210, highlightbackground="#E65C06",
                            highlightthickness=5)
    nextgameframe = Frame(frame, bg="black", width=400, height=200, borderwidth=5)

    backgroundframe.place(x=570, y=20)
    nextgameframe.place(x=575, y=25)

    nextmatchup = driver.find_element(By.XPATH, value="/html/body/div[4]/div/main/div[1]/section")
    date = nextmatchup.find_element(By.CLASS_NAME, value="TeamMatchup-date")
    opp = nextmatchup.find_element(By.CLASS_NAME, value="TeamMatchup-vsInfo")
    # arena = nextmatchup.find_element(By.CLASS_NAME, value="TeamMatchup-secondaryInfo")

    nextgamelabel = Label(nextgameframe, text="Next Matchup:", fg="#E65C06", bg="black", font=(font, 20))

    datelabel = Label(nextgameframe, text=date.text, fg="black", bg="#E65C06", font=(font, 12))
    opplabel = Label(nextgameframe, text=f"{teamname.text} {opp.text}", fg="black", bg="#E65C06", font=(font, 12))
    # arenalabel = Label(nextgameframe, text=arena.text, fg="black", bg="#E65C06", font=(font, 12))

    nextgamelabel.place(x=20, y=0)
    datelabel.place(x=105, y=70)
    opplabel.place(x=50, y=100)
    # arenalabel.place(x=150,y=130)

    # change
    driver.get(link2)

    background_info_table = driver.find_element(By.XPATH,value="""//*[@id="__next"]/div[2]/div[2]/main/div[3]/div[5]/div/div[3]/section/div/div[2]/dl""")
    headings = background_info_table.find_elements(By.TAG_NAME, value="dt")
    tabledata = []

    for heading in headings:
        tabledata.append(heading.text)

    background_info_table = driver.find_element(By.XPATH,value="""//*[@id="__next"]/div[2]/div[2]/main/div[3]/div[5]/div/div[3]/section/div/div[2]/dl""")
    headings = background_info_table.find_elements(By.TAG_NAME, value="dd")
    tabledata2 = []

    for heading in headings:
        tabledata2.append(heading.text)

    BTD = {h: i for h, i in zip(tabledata, tabledata2)}
    # for x in BTD:
    #     print(x)

    r = 110
    
    for h, i in BTD.items():
        feed = tk.Button(frame, text=f"{h} : {i} ", fg="#E65C06", bg="black", font=(font, 11), borderwidth=0)
        feed.place(x=220, y=r)
        r = r + 23

    ppg_rank = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[1]/div[2]""")
    ppg = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[1]/div[3]""")

    rpg_rank = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[2]/div[2]""")
    rpg = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[2]/div[3]""")

    apg_rank = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[3]/div[2]""")
    apg = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/section/div/div/div[4]/div[3]/div[3]""")

    # print(f"{ppg_rank.text}, {ppg.text}")
    # print(f"{rpg_rank.text}, {rpg.text}")
    # print(f"{apg_rank.text}, {apg.text}")

    ranks = [ppg_rank, rpg_rank, apg_rank]
    stats = [ppg, rpg, apg]

    statisitcs = {s: r for s, r in zip(stats, ranks)}

    statslabel = Label(frame, text="Team Stats: ", bg="black", fg="grey", font=(font, 20))

    ppglabel = Label(frame, text=f"PPG", bg="black", fg="white", font=(font, 15))
    rpglabel = Label(frame, text=f"RPG", bg="black", fg="white", font=(font, 15))
    apglabel = Label(frame, text=f"APG", bg="black", fg="white", font=(font, 15))

    statslabel.place(x=100, y=293)

    ppglabel.place(x=100, y=350)
    rpglabel.place(x=175, y=350)
    apglabel.place(x=250, y=350)

    ppgstatlabel = Label(frame, text=f"{ppg.text} \n{ppg_rank.text}", bg="black", fg="#E65C06", font=(font, 11))
    rpgstatlabel = Label(frame, text=f" {rpg.text} \n{rpg_rank.text}", bg="black", fg="#E65C06", font=(font, 11))
    apgstatlabel = Label(frame, text=f" {apg.text} \n{apg_rank.text}", bg="black", fg="#E65C06", font=(font, 11))

    ppgstatlabel.place(x=100, y=400)
    rpgstatlabel.place(x=175, y=400)
    apgstatlabel.place(x=250, y=400)
