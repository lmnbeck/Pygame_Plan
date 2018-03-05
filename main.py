import pygame
import sys
import traceback
from pygame.locals import *
from myPlan import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 600, 850
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战 -- lmn")

#load images
background = pygame.image.load("image/Stars_large.png").convert()

#load music
pygame.mixer.music.load("sound/background.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/Shoot.wav")
bullet_sound.set_volume(0.2)
boomb_sound = pygame.mixer.Sound("sound/ExplosionPlayer.wav")
boomb_sound.set_volume(0.2)
supply_sound = boomb_sound
get_bomb_sound = boomb_sound
upgrade_sound = boomb_sound
enemy3_fly_sound = boomb_sound
enemy_down_sound = ("sound/ExplosionEnemy.wav")
me_down_sound = boomb_sound


def main():
    pygame.mixer.music.play(-1)

    myBluePlanImage = pygame.image.load("image/BluePlan.png")
    myBluePlanImage = pygame.transform.scale(myBluePlanImage, (200,100))
    myBluePlan = myPlan(myBluePlanImage, (bg_size[0]//2,bg_size[1] - 200), (0,0), bg_size )


    mySpeed = [0,0]
    
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    mySpeed = [0,-2]
                elif event.key == K_DOWN:
                    mySpeed = [0,2]
                elif event.key == K_LEFT:
                    mySpeed = [-2,0]
                elif event.key == K_RIGHT:
                    mySpeed = [2,0]
            if event.type == pygame.KEYUP:
                mySpeed = [0,0]

        screen.blit(background, (0,0))

        #my Plan
        myPlanPos = myBluePlan.move(mySpeed)
        screen.blit(myBluePlan.image, myBluePlan.rect)
        #print(myPlanPos)
        myBulletPos = (myPlanPos.left+100-9, myPlanPos.top-30)
        myBulletSpeed = [0,-5]
        my
        #print(myBulletPos)
        screen.blit(myBluePlan.shoot(), myBulletPos)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
