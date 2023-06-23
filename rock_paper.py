import pygame
import random as rm
from pygame import mixer
pygame.init()
print("ROCK PAPER SCSSIOR GAME")
print("GAME START!")
mixer.music.load('TCD25PS-game-success.mp3')
mixer.music.play(1)
while True:
    
    print("please enter you choice :")

    gammer=input()
    choicee=["rock" , "paper" , "scessior"]
    suff=rm.choice(choicee)
    print(suff)

    if gammer == "rock" and suff == "paper":
        print("you win")
        mixer.music.load('winning.mp3')
        mixer.music.play(1)
    elif gammer == "paper" and suff == "rock":
        print("you lose")
        mixer.music.load('lose.mp3')
        mixer.music.play(1)
    elif gammer == "scessior" and suff == "rock":
        print("you lose")
        mixer.music.load('winning.mp3')
        mixer.music.play(1)
    elif gammer == "rock" and suff == "rock":
        print("game tie")
        mixer.music.load('mixkit-arcade-game-complete-or-approved-mission-205.wav')
        mixer.music.play(1)
    elif gammer == "paper" and suff == "paper":
        print("game tie")
        mixer.music.load('mixkit-arcade-game-complete-or-approved-mission-205.wav')
        mixer.music.play(1)
    elif gammer == "scessior" and suff == "scessior":
        print("game tie")
        mixer.music.load('mixkit-arcade-game-complete-or-approved-mission-205.wav')
        mixer.music.play(1)
    elif gammer == "scessior" and suff == "paper":
        print("you win")
        mixer.music.load('winning.mp3')
        mixer.music.play(1)
    elif gammer == "paper" and suff == "scessior":
        print("you lose")
        mixer.music.load('lose.mp3')
        mixer.music.play(1)
    elif gammer == "rock" and suff == "scessior":
        print("you win")
        mixer.music.load('winning.mp3')
        mixer.music.play(1)
    else:
        pass




