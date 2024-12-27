#Programa reproduz um áudio MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('assets\snore-mimimimimimi.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait