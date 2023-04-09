# Program: Phoenix 3
# Authors: Dov Abrahim Kanner and Jack Xu

from cmu_graphics.cmu_graphics import *
import os

#forced reset use:git reset --hard origin/main

##################################
# App 
##################################

def onAppStart(app):
    print('In onAppStart')
    script_dir = os.path.dirname(__file__)
    rel_path = "./pictures/Real Phoenix.png"
    app.character = os.path.join(script_dir, rel_path)
    rel_path = "./pictures/Bluebullet-removebg-preview (1).png"
    app.bullet = os.path.join(script_dir, rel_path)

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
    app.list = [0]
    app.stepsPerSecond = 50
    app.bulletCounter = 0

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
        list.append(app.list, app.CharacterX)
        list.append(app.list, app.CharacterY)

def game_bulletCheck(app):
    return True

def game_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawRect(app.CharacterX, app.CharacterY, 5, 5, fill='white')
    if len(app.list) >= 2:
        for i in range(1, len(app.list), 2):
            drawRect(app.list[i], app.list[i+1], 1, 5, fill='white')
            bulletWidth, bulletHeight = getImageSize(app.bullet)
            drawImage(app.bullet, app.list[i]+2.5, app.list[i+1]+2.5, align = 'center', width = bulletWidth/10, height = bulletHeight/10)
    characterWidth, characterHeight = getImageSize(app.character)
    drawImage(app.character, app.CharacterX+2.5, app.CharacterY+2.5, align = 'center', width = characterWidth/6, height = characterHeight/6)

def game_onStep(app):
    if len(app.list) >= 2:
        for i in range(2, len(app.list), 2):
            if i >= len(app.list):
                break
            if app.list[i] < -5:
                app.list.pop(i)
                app.list.pop(i-1)
                i -= 2
            else:
                app.list[i] -= 10

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