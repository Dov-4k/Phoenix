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
    drawRect(100, 100, app.width-200, app.height-200, fill=app.color)

##################################
# Game
##################################

def game_onAppStart(app):
    print('In game')
    app.cx = app.width/2
    app.dx = 10

def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onKeyPress(app, key):
    if key == 's': setActiveScreen('startScreen')
    elif key == 'd': app.dx = -app.dx

def game_onStep(app):
    app.cx = (app.cx + app.dx) % app.width

def game_redrawAll(app):
    drawLabel('Game', app.width/2, 30, size=16)
    drawLabel('Press d to change direction of dot', app.width/2, 50, size=16)
    drawLabel('Press s to change the screen to startScreen', app.width/2, 70, size=16)
    drawCircle(app.cx, app.height/2, 50, fill='lightGreen')

##################################c
# main
##################################

def main():
    runAppWithScreens(initialScreen='startScreen', height=700)

main()