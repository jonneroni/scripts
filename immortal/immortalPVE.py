from pyautogui import click, moveTo, move, press, drag, mouseDown, mouseUp, keyDown, keyUp
from time import sleep
import sys

skillsMenu = [2364, 290]
menuPos = [2522, 62]
skillmenuexit = [2493, 107]
center = [1280, 720]

explodingPalm = [485, 988]
fist = [489, 1109]
innersanc = [476, 1122]
equip = [1303, 1188]
abil1 = [2037, 1221]
abil2 = [2019, 1012]
abil3 = [2181, 861]
abil4 = [2396, 858]


def moveClick(poslist):
    moveTo(poslist[0], poslist[1])
    sleep(0.1)
    click()


def liiku(pos):
    moveTo(pos[0], pos[1])


def scroll(amount):
    mouseDown()
    move(0, amount)
    mouseUp()


def nappi(nappi):
    keyDown(nappi)
    press("enter")
    keyUp(nappi)


moveClick(menuPos)
sleep(0.1)
moveClick(skillsMenu)
sleep(0.1)
moveClick(explodingPalm)
sleep(0.1)
moveClick(equip)
sleep(0.1)
moveClick(abil4)
sleep(0.1)
liiku(explodingPalm)
sleep(0.1)
scroll(-400)
sleep(0.1)
moveClick(fist)
sleep(0.1)
moveClick(equip)
sleep(0.1)
moveClick(abil3)
sleep(0.1)
liiku(fist)
sleep(0.1)
moveClick(skillmenuexit)
sleep(0.1)
liiku(center)


sys.exit()
