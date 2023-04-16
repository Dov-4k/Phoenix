# Program: Phoenix 3
# Authors: Dov Abrahim Kanner and Jack Xu

from cmu_graphics.cmu_graphics import *
import os
import random

#forced reset use:git reset --hard origin/main

##################################
# App 
##################################

def onAppStart(app):
    print('In onAppStart')
    script_dir = os.path.dirname(__file__)
    rel_path = "./pictures/Real Phoenix.png"
    app.character = os.path.join(script_dir, rel_path)
    rel_path = "./pictures/Phoenix enemySparrow.png"
    app.alien = os.path.join(script_dir, rel_path)

def onAppStop(app):
    print('In onAppStop')

##################################
# StartScreen
##################################

def startScreen_onAppStart(app):
    print('In startScreen_onAppStart')

def startScreen_onScreenActivate(app):
    print('In startScreen_onScreenActivate')

def startScreen_onKeyPress(app, key):
    setActiveScreen('game')

def startScreen_onMousePress(app, x, y):
    setActiveScreen('game')

def startScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Welcome to Phoenix 3', app.width/2, 30, size=16, fill='white')
    drawLabel('Press any key to begin the game', app.width/2, 50, size=16, fill='white')

##################################
# Game
##################################

class Aliens:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 10)
        self.speed = random.randint(2, 7)

class Bullets:
    def __init__(self, CharX, CharY):
        self.x = CharX
        self.y = CharY

def game_onAppStart(app):
    print('In game')
    app.CharacterX = app.width/2
    app.CharacterY = 650
    app.bullets2 = []
    app.bullets = []
    app.aliens = []
    app.stepsPerSecond = 100

def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onKeyPress(app, key):
    if key == 'p': setActiveScreen('pause')
    if key == 'space':
        app.bullets.append(Bullets(app.CharacterX - 12, app.CharacterY))
        app.bullets2.append(Bullets(app.CharacterX + 17, app.CharacterY))

def game_onMousePress(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_onMouseDrag(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_redrawAll(app):
    if len(app.aliens) == 0:
        for i in range(0, random.randint(2, 14)):
            alien = Aliens()
            app.aliens.append(alien)
    else:
        for alien in app.aliens:
            x = app.CharacterX - alien.x
            y = app.CharacterY - alien.y
            distance = (x ** 2 + y ** 2) ** 0.5
            if distance != 0:
                alien.x += x / distance * alien.speed
                alien.y += y / distance * alien.speed
        for i in range(0, len(app.bullets)):
            for j in range(0, len(app.aliens)):
                if i >= 0 and j >= 0 and i < len(app.bullets) and j < len(app.aliens):
                    distanceX = app.bullets[i].x - app.aliens[j].x
                    distanceY = app.bullets[i].y - app.aliens[j].y
                    if len(app.aliens) != 0 and len(app.bullets) != 0 and distanceX <= 5 and distanceY <= 5:
                        del app.aliens[j]
                        del app.bullets[i]
                        i -= 1
                        j -= 1
        for i in range(0, len(app.bullets2)):
            for j in range(0, len(app.aliens)):
                if i >= 0 and j >= 0 and i < len(app.bullets) and j < len(app.aliens):
                    distanceX = app.bullets2[i].x - app.aliens[j].x
                    distanceY = app.bullets2[i].y - app.aliens[j].y
                    if len(app.aliens) != 0 and len(app.bullets2) != 0 and distanceX <= 5 and distanceY <= 5:
                        del app.aliens[j]
                        del app.bullets2[i]
                        i -= 1
                        j -= 1
    drawRect(0, 0, app.width, app.height, fill='black')  
    characterWidth, characterHeight = getImageSize(app.character)
    drawImage(app.character, app.CharacterX+2.5, app.CharacterY+2.5, align = 'center', width = characterWidth/6, height = characterHeight/6)
    for i in range(0, len(app.bullets)):
        drawCircle(app.bullets[i].x, app.bullets[i].y, 5, fill='cyan')
    for i in range(0, len(app.bullets2)):
        drawCircle(app.bullets2[i].x, app.bullets2[i].y, 5, fill='cyan')
    if len(app.aliens) >= 2:
        for i in range(0, len(app.aliens)):
            alienWidth, alienHeight = getImageSize(app.alien)
            drawImage(app.alien, app.aliens[i].x, app.aliens[i].y, width = 40, height = 40)

def game_onStep(app):
    if len(app.bullets) >= 0 and len(app.bullets2) >= 0:
        for i in range(0, len(app.bullets)):
            if app.bullets[i].y < -5:
                del app.bullets[i]
                i -= 1
            else:
                app.bullets[i].y -= 10
        for i in range(0, len(app.bullets2)):
            if app.bullets2[i].y < -5:
                del app.bullets2[i]
                i -= 1
            else:
                app.bullets2[i].y -= 10

##################################
# Pause
##################################

def pause_onAppStart(app):
    print('In pause menu')

def pause_onScreenActivate(app):
    print('In pause_onScreenActivate')

def pause_onKeyPress(app, key):
    if key == 'p': setActiveScreen('game')
    elif key == 'escape': setActiveScreen('startScreen')

def pause_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Pause', app.width/2, 30, size=25, fill='white')
    drawLabel('Press p to resume the game', app.width/2, 50, size=16, fill='white')
    drawLabel('Press escape to exit the game', app.width/2, 70, size=16, fill='white')

##################################
# main
##################################

def main():
    runAppWithScreens(initialScreen='startScreen', height=700)

main()