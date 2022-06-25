"""
Configuration du jeu
"""
import pygame

# Definition des constantes

# Taille de la fenetre du jeu : nombre de ligne x nombre de colonnes
WINDOW_SIZE = {
    "Facile": [10,20],
    "Modéré": [25,40],
    "Difficile": [30,60]
}

# Images
EMPTY_BOX = pygame.transform.scale(pygame.image.load("img/empty.png"), (30,30))
FLAG_BOX = pygame.transform.scale(pygame.image.load("img/flag.png"), (30,30))
MINE_BOX = pygame.transform.scale(pygame.image.load("img/mine.png"), (30,30))
MINE_RED_BOX = pygame.transform.scale(pygame.image.load("img/mine_red.png"), (30,30))
NO_MINE = pygame.transform.scale(pygame.image.load("img/nomine.png"), (30,30))


