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
    rel_path = "./pictures/background-free-video.png"
    app.backgrd = os.path.join(script_dir, rel_path)
    app.maxScore = 0

def onAppStop(app):
    print('In onAppStop')

##################################
# StartScreen
##################################

def startScreen_onAppStart(app):
    print('In startScreen_onAppStart')

def startScreen_onScreenActivate(app):
    print('In startScreen_onScreenActivate')
    app.CharacterX = app.width/2
    app.CharacterY = 650
    app.bullets = []
    app.aliens = []
    app.score = 0
    app.magazine = 4

def startScreen_onKeyPress(app, key):
    setActiveScreen('game')

def startScreen_onMousePress(app, x, y):
    setActiveScreen('game')

def startScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Welcome to Phoenix 3', app.width/2, 30, size=16, fill='white')
    drawLabel('Press any key to begin the game', app.width/2, 50, size=16, fill='white')
    drawLabel('Max Score: '+ str(app.maxScore), app.width/2, 70, size=16, fill='white')
    drawLabel('Instructions:', app.width/2, 90, size=16, fill='white')
    drawLabel('Hold mouse to move the ship', app.width/2, 110, size=16, fill='white')
    drawLabel('Press space to shoot', app.width/2, 130, size=16, fill='white')
    drawLabel('Press p to pause', app.width/2, 150, size=16, fill='white')

##################################
# Game
##################################

class Aliens:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 10)
        self.speed = random.randint(3, 5)

class Bullets:
    def __init__(self, CharX, CharY):
        self.x = CharX
        self.y = CharY

def game_onAppStart(app):
    print('In game')
    app.CharacterX = app.width/2
    app.CharacterY = 650
    app.bullets = []
    app.aliens = []
    app.stepsPerSecond = 100
    app.score = 0
    app.magazine = 4

def game_onScreenActivate(app):
    print('In game_onScreenActivate')

def game_onKeyPress(app, key):
    if key == 'p': setActiveScreen('pause')
    if key == 'space' and len(app.bullets) <= 3:
        app.bullets.append(Bullets(app.CharacterX, app.CharacterY))
        app.magazine -= 1

def game_onMousePress(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_onMouseDrag(app, x, y):
    app.CharacterX = x-2.5
    app.CharacterY = y-2.5

def game_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Score: '+ str(app.score), app.width/2, 30, size=16, fill='white')
    drawLabel('Magazine: '+ str(app.magazine), app.width/2, 50, size=16, fill='white')
    drawImage(app.character, app.CharacterX+2.5, app.CharacterY+2.5, align = 'center', width = 58, height = 58)
    for i in range(0, len(app.bullets)):
        drawCircle(app.bullets[i].x, app.bullets[i].y, 5, fill='cyan')
    for i in range(0, len(app.aliens)):
        drawImage(app.alien, app.aliens[i].x-20, app.aliens[i].y-20, width = 40, height = 40)

def game_onStep(app):
    if len(app.bullets) >= 0:
        for i in range(0, len(app.bullets)):
            if i < len(app.bullets) and app.bullets[i].y < -4:
                del app.bullets[i]
                app.magazine += 1
                i -= 1
            elif i < len(app.bullets):
                app.bullets[i].y -= 10
    if len(app.aliens) == 0:
        for i in range(0, random.randint(2, 7)):
            alien = Aliens()
            app.aliens.append(alien)
    else:
        for alien in app.aliens:
            x = app.CharacterX - alien.x
            y = app.CharacterY - alien.y
            distance = (x ** 2 + y ** 2) ** 0.5
            if distance != 0:
                alien.x += x / distance * alien.speed
                if(y / distance * alien.speed < 0): #difficulty increase
                    alien.y += y / distance * alien.speed - (app.score * 0.1)
                elif(y / distance * alien.speed > 0):
                    alien.y += y / distance * alien.speed + (app.score * 0.1)
        for alien in app.aliens:
            if len(app.bullets) == 0:
                break
            for bullet in app.bullets:
                if bullet.x >= alien.x-20 and bullet.x <= alien.x+20 and bullet.y >= alien.y-20 and bullet.y <= alien.y+20:
                    app.bullets.remove(bullet)
                    app.aliens.remove(alien)
                    app.score += 1
                    app.magazine += 1
                    break
        for alien in app.aliens:
            if alien.x > app.CharacterX+2.5-25 and alien.x < app.CharacterX+2.5+25 and alien.y > app.CharacterY+2.5-25 and alien.y < app.CharacterY+2.5+25:
                if app.score > app.maxScore: app.maxScore = app.score
                setActiveScreen('gameOver')

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
# Game Over
##################################

def gameOver_onAppStart(app):
    print('In gameOver')

def gameOver_onScreenActivate(app):
    print('In gameOver_onScreenActivate')

def gameOver_onKeyPress(app, key):
    if key == 'escape': setActiveScreen('startScreen')

def gameOver_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawLabel('Game Over', app.width/2, 30, size=25, fill='white')
    drawLabel('Press escape to exit the game', app.width/2, 50, size=16, fill='white')

##################################
# main
##################################

def main():
    runAppWithScreens(initialScreen='startScreen', height=700)

main()