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
    app.color = 'gold'
    app.activatedCounter1 = 0

def startScreen_onScreenActivate(app):
    print('In startScreen_onScreenActivate')
    app.activatedCounter1 += 1

def startScreen_onKeyPress(app, key):
    if key == 's': setActiveScreen('screen2')
    elif key == 'c': app.color = 'navy' if (app.color == 'gold') else 'gold'

def startScreen_redrawAll(app):
    drawLabel('Screen 1', app.width/2, 30, size=16)
    drawLabel('Press c to change square color', app.width/2, 50, size=16)
    drawLabel('Press s to change screen to screen2', app.width/2, 70, size=16)
    drawRect(100, 100, app.width-200, app.height-200, fill=app.color)
    drawLabel(f'Screen1 was activated {app.activatedCounter1} times',
            app.width/2,app.height-30, size=12)

##################################
# Screen2
##################################

def screen2_onAppStart(app):
    print('In screen2_onAppStart')
    app.cx = app.width/2
    app.dx = 10

def screen2_onScreenActivate(app):
    print('In screen2_onScreenActivate')

def screen2_onKeyPress(app, key):
    if key == 's': setActiveScreen('screen1')
    elif key == 'd': app.dx = -app.dx

def screen2_onStep(app):
    app.cx = (app.cx + app.dx) % app.width

def screen2_redrawAll(app):
    drawLabel('Screen 2', app.width/2, 30, size=16)
    drawLabel('Press d to change direction of dot', app.width/2, 50, size=16)
    drawLabel('Press s to change the screen to screen1', app.width/2, 70, size=16)
    drawCircle(app.cx, app.height/2, 50, fill='lightGreen')

##################################
# main
##################################

def main():
    runAppWithScreens(initialScreen='screen1', width=800)

main()