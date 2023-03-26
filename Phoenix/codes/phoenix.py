from cmu_graphics.cmu_graphics import *

##################################
# App
##################################

def onAppStart(app):
    print('In onAppStart')

def onAppStop(app):
    print('In onAppStop')

##################################
# StartScreen
##################################

def startScreen_onAppStart(app):
    print('In startScreen_onAppStart')

def startScreen_onScreenActivate(app):
    print('In startScreen_onScreenActivate')

def startScreen_onMousePress(app, x, y):
    if x >= 130 and x <= 180 and y >= 44 and y <= 55: setActiveScreen('game')

def startScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Welcome to Phoenix 3', app.width/2, 30, size=16, fill='white')
    drawLabel('Press START to begin the game', app.width/2, 50, size=16, fill='white')

##################################
# Game
##################################

def game_onAppStart(app):
    print('In game')
    app.CharacterX = app.width/2
    app.CharacterY = 650
    app.firstBulletX = None
    app.firstBulletY = None


def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onMousePress(app, x, y):
    app.CharacterX = x-10
    app.CharacterY = y-10

def game_onMouseDrag(app, x, y):
    app.CharacterX = x-10
    app.CharacterY = y-10

def game_onKeyPress(app, key):
    if key == 'p': setActiveScreen('pause')
    while key == 'space':
        app.firstBulletX = app.CharacterX
        app.firstBulletY = app.CharacterY

def game_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawRect(app.CharacterX, app.CharacterY, 20, 20, fill='white')
    if app.firstBulletX != None:
        drawRect(app.firstBulletX, app.firstBulletY, 5, 1, fill='white')
        app.firstBulletX+3
    drawLabel('Game', app.width/2, 30, size=16)

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