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
    rel_path = "./pictures/alien-removebg-preview.png"
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

def game_onAppStart(app):
    print('In game')
    app.CharacterX = app.width/2
    app.CharacterY = 650
    app.bullets = [0]
    app.bullets2 = [0]
    app.aliens = [0]
    app.stepsPerSecond = 30

def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onMousePress(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_onMouseDrag(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_onKeyPress(app, key):
    if key == 'p': setActiveScreen('pause')
    if key == 'space':
        list.append(app.bullets, app.CharacterX - 12)
        list.append(app.bullets, app.CharacterY)
        list.append(app.bullets2, app.CharacterX + 17)
        list.append(app.bullets2, app.CharacterY)

def game_bulletCheck(app):
    return True

def game_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    if len(app.bullets) >= 2:
        for i in range(1, len(app.bullets), 2):
            drawCircle(app.bullets[i], app.bullets[i+1], 5, fill='cyan')
            drawCircle(app.bullets2[i], app.bullets2[i+1], 5, fill='cyan')
    characterWidth, characterHeight = getImageSize(app.character)
    drawImage(app.character, app.CharacterX+2.5, app.CharacterY+2.5, align = 'center', width = characterWidth/6, height = characterHeight/6)
    if len(app.aliens) >= 2:
        for i in range(1, len(app.aliens), 2):
            alienWidth, alienHeight = getImageSize(app.alien)
            drawImage(app.alien, app.aliens[i], app.aliens[i+1], width = 15, height = 15)

def game_onStep(app):
    if len(app.bullets) >= 2:
        for i in range(2, len(app.bullets), 2):
            if i >= len(app.bullets):
                break
            if app.bullets[i] < -5:
                app.bullets.pop(i)
                app.bullets.pop(i-1)
                app.bullets2.pop(i)
                app.bullets2.pop(i-1)
                i -= 2
            else:
                app.bullets[i] -= 10
                app.bullets2[i] -= 10
    if len(app.aliens) < 2:
        for i in range(1, random.randint(1, 10), 2):
            app.aliens.append(random.randint(0, app.width))
            app.aliens.append(5)
    else:
        for i in range(1, len(app.aliens), 2):
            x = app.CharacterX - app.aliens[i]
            y = app.CharacterY - app.aliens[i+1]
            distance = (x ** 2 + y ** 2) ** 0.5
            if distance != 0:
                app.aliens[i] += x / distance * 5
                app.aliens[i+1] += y / distance * 5

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