import pygame
import random
import sys

pygame.init() #starts up pygame
screen = pygame.display.set_mode((600, 350)) #creates a screen of width 350 and length 600
clock = pygame.time.Clock() #sets up an FPS(frames per second)

TILESIZE = 80

#fonts
font = pygame.font.Font('rock-paper-scissors/assets/PixeloidMono.ttf', 15)
message = font.render("Welcome to the Rock, Paper, Scissors game! Good Luck :)", True, "white")
messagerect = message.get_rect()
messagerect.center = (300,20)

rulesfont = pygame.font.Font('rock-paper-scissors/assets/PixeloidMono.ttf', 12)
rules = rulesfont.render("Rules: rock beats scissor, scissor beats paper, and paper beats rock", True, "white")
rulesrect = rules.get_rect()
rulesrect.center = (300,45)


choicemessage = font.render("Click on one of the below:", True, "white")
choicemessagerect = choicemessage.get_rect()
choicemessagerect.center = (160,90)


#buttons
rock = pygame.image.load('rock-paper-scissors/assets/rock.png')
rock= pygame.transform.scale(rock, (TILESIZE*0.9, TILESIZE*0.9))
paper = pygame.image.load('rock-paper-scissors/assets/paper.png')
paper= pygame.transform.scale(paper, (TILESIZE, TILESIZE))
scissors = pygame.image.load('rock-paper-scissors/assets/scissors.png')
scissors= pygame.transform.scale(scissors, (TILESIZE, TILESIZE))

rock_rect = rock.get_rect(center=(75,150))
paper_rect = paper.get_rect(center=(200,150))
scissors_rect = scissors.get_rect(center=((75+125/2),230))

robot = pygame.image.load('rock-paper-scissors/assets/robot.png')
robot = pygame.transform.scale(robot, (TILESIZE*3, TILESIZE*3))
robot_rect = robot.get_rect(center=(500,260))

text = pygame.image.load('rock-paper-scissors/assets/text.png')
text = pygame.transform.scale(text, (TILESIZE*2.5, TILESIZE*2.5))
text_rect = text.get_rect(center=(420,180))

robot_font = pygame.font.Font('rock-paper-scissors/assets/PixeloidMono.ttf', 12) #makes the robot font size smaller
robot_voice = robot_font.render("My choice is:", True, "black")
robot_voicerect = robot_voice.get_rect()
robot_voicerect.center = (420,130)



def robot_choice():
    x = random.randint(1,3) #1 is rock, 2 is paper, 3 is scissors
    return x
    


roborock= pygame.transform.scale(rock, (TILESIZE/2, TILESIZE/2))
roborock_rect = roborock.get_rect(center=(420,170))

robopaper = pygame.transform.scale(paper, (TILESIZE/2, TILESIZE/2))
robopaper_rect = robopaper.get_rect(center=(420,170))

roboscissors = pygame.transform.scale(scissors, (TILESIZE/2, TILESIZE/2))
roboscissors_rect = roboscissors.get_rect(center=(420,170))

finalfont = pygame.font.Font('rock-paper-scissors/assets/PixeloidMono.ttf', 30)


running = True
robot_choice_made = False
rc = None #robot choice
yc = None #your choice
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #above 4 lines make it so the user has a way to close the screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos): #if the place where the mouse was clikced is inside the rock_rect
                yc = 1
            elif paper_rect.collidepoint(event.pos):
                yc = 2
            elif scissors_rect.collidepoint(event.pos):
                yc = 3

            rc = robot_choice()
            robot_choice_made = True
            
    screen.fill("darkslateblue") #creates backgroud
    screen.blit(message, messagerect) #creates welcome message
    screen.blit(choicemessage, choicemessagerect)
    screen.blit(rules, rulesrect)

    screen.blit(rock, rock_rect)
    screen.blit(paper, paper_rect)
    screen.blit(scissors, scissors_rect)

    if robot_choice_made:
        screen.blit(robot, robot_rect)
        screen.blit(text, text_rect)
        screen.blit(robot_voice,robot_voicerect)
        
        if rc == 1:
            screen.blit(roborock,roborock_rect)
        elif rc == 2:
            screen.blit(robopaper,robopaper_rect)
        elif rc == 3:
            screen.blit(roboscissors,roboscissors_rect)

    if rc != None and yc != None:
        if rc == yc:
            winner = finalfont.render("It's a tie. Play again!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc == 1 and yc == 2: #robot is rock, you are paper
            winner = finalfont.render("You win!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc == 1 and yc == 3: #robot is rock, you are scissors
            winner = finalfont.render("Robot wins!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc == 2 and yc == 1: #robot is paper and you are rock
            winner = finalfont.render("Robot wins!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc == 2 and yc == 3: #robot is paper and you are scissors
            winner = finalfont.render("You win!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc == 3 and yc == 1: #robot is scissors and you are rock
            winner = finalfont.render("You win!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
        elif rc ==3 and yc == 2: #robot is scissors and you are paper
            winner = finalfont.render("Robot wins!", True, "white")
            winnerrect = winner.get_rect()
            winnerrect.center = (300,330)
            screen.blit(winner, winnerrect)
    
    pygame.display.flip()



