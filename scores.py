
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
from PIL import ImageTk, Image
import tkinter
import tkinter as Tk
from tkinter import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clear_widgets(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

def scorecards_(frame, font):

    clear_widgets(frame)
    frame.configure(bg="black")

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=Path, options=option)

    driver.get("https://www.nba.com/games?date=2023-04-04")
    scorecards = driver.find_element(By.XPATH, value="""//*[@id="__next"]/div[2]/div[2]/main/div[2]/div/div[1]/div[1]""")
    points = scorecards.find_elements(By.TAG_NAME, value="a")

    team_logos = []
    teamlogos = scorecards.find_elements(By.TAG_NAME, value="a")
    for logo in teamlogos:
        team_logos.append(logo)

    data = []

    for scores in points:
        data.append(scores.text)

    ff = []

    for a in range(0, len(data),8):
        ff.append(data[a])
        a += a

    dd = []

    for f in ff:
        n = f.split("\n")
        dd.append(n)

    rows = 4 # the amount of rows that i want to display for each column

    x = 100 # initial x value
    y = 70 # initial y value


    Label(frame, text="LATEST SCORES: ", font=(font,20), fg="white", bg="black").place(x=50, y=12) # label for the frame

    for i in range(0, len(dd), rows): #for loop that cycles through the length of the list and the amount of rows
        row = dd[i:i + rows] # defines the rows by the set amount of rows that i wanted to make by the index
        for team1, team1record, team1_score, final, team2_score, team2, team2record in row:
        # collects each item within the cycle for the item in the first dimension
            Label(frame, text=f"{team1} \n"f"{team2} ", fg="black", bg="#E65C06", font=(font,15)).place(x=x,y=y) # creates the label displaying the teams
            Label(frame, text=f"{team1_score}\n"f"{team2_score}", bg="black", fg="white",font=(font, 15)).place(x=x+140,y=y)# creates the label displaying the scores
            Label(frame, text=""
                              "\n"
                              "\n"
                              "\n", bg="grey").place(x=x + 200, y=y) # label made foe design
            y+=100 # makes a space for the next labels to be displayed 100 piels away on the y-axis on the column
        x+=220 # creates the space for the next coln 220 pixels away
        y=70  #when the new column is created y is reset to 70, the orginal value on  the y axis

    def nextday_schedule(frame,font):

        clear_widgets(frame)
        frame.configure(bg="black")

        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        Path = Service(executable_path=r"C:\Users\user\Desktop\chromedriver\chromedriver.exe")
        driver = webdriver.Chrome(service=Path, options=option)

        driver.get("""https://www.nba.com/schedule""")
        scorecards = driver.find_element(By.XPATH,
                                         value="""//*[@id="__next"]/div[2]/div[2]/main/div[2]/section/div/div[3]/div/div[2]/div[2]""")

        teamslist = []

        teams = scorecards.find_elements(By.TAG_NAME, value="a")
        for team in teams:
            teamslist.append(team.text)

        ee = []

        timesloc = scorecards.find_elements(By.TAG_NAME, value="div")
        for tl in timesloc:
            ee.append(tl.text)

        timeslist = []
        for t in ee:
            if t[5:] == "PM ET":
                timeslist.append(t)

        for e in teamslist:
            if e == "TICKETS":
                teamslist.remove(e)

        for e in teamslist:
            if e == "":
                teamslist.remove(e)

        for e in teamslist:
            if e == "PREVIEW":
                teamslist.remove(e)

        teams1 = []
        teams2 = []

        for t in range(0, len(teamslist), 2):
            teams1.append(teamslist[t])
            teams2.append(teamslist[t + 1])

        scorecards__ = list(zip(teams1, teams2, timeslist))

        print(scorecards__)

        for x, y, z in scorecards__:
            print(f"{x} V {y} @ {z}")

        chunk_size = 4

        x = 50
        y = 70

        date = driver.find_element(By.XPATH,
                                   value="""//*[@id="__next"]/div[2]/div[2]/main/div[2]/section/div/div[3]/div/div[2]/div[1]/h4""")
        Label(frame, text=f"Tomorrow's Schedule: {date.text}", bg="black", fg="grey", font=(font, 20)).place(x=20, y=0)

        for i in range(0, len(scorecards__), chunk_size):
            chunk = scorecards__[i:i + chunk_size]
            for team1, team2, date in chunk:
                Label(frame, text=f"{team1}  v {team2} \n {date}", bg="black", fg="#E65C06", font=(font, 12)).place(x=x,
                                                                                                                    y=y)
                y += 120
            x += 300
            y = 70

        Button(frame, text="Today's Schedule", bg="black", fg="grey", borderwidth=0, font=(font, 14),
               command=lambda: scorecards_(frame, font)).place(x=400, y=500)

    Button(frame, text = "Tomorrow's Schedule", bg="black", fg="grey", borderwidth=0, font=(font,14), command=lambda : nextday_schedule(frame,font)).place(x=400,y=500)


