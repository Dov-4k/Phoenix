from cmu_graphics.cmu_graphics import *
import os

##################################
# App
##################################

def onAppStart(app):
    print('In onAppStart')
    script_dir = os.path.dirname(__file__)
    rel_path = "./pictures/Real Phoenix.png"
    app.image = os.path.join(script_dir, rel_path)

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
    app.stepsPerSecond = 100
    app.bulletCounter = 0

def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onMousePress(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_onMouseDrag(app, x, y):
    app.CharacterX = x-10
    app.CharacterY = y-10

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
    drawLabel('Game', app.width/2, 30, size=16)
    imageWidth, imageHeight = getImageSize(app.image)
    drawImage(app.image, app.CharacterX, app.CharacterY, align = 'center', width = imageWidth/6, height = imageHeight/6)

def game_onStep(app):
    if len(app.list) >= 2:
        for i in range(2, len(app.list), 2):
            if app.list[i] >= -5:
                app.list[i] -= 7

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