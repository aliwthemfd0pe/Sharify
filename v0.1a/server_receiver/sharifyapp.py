# DISPLAY_RECEIVER

# Informations
print("Sharify Server v0.02-a, Ali KHELFAOUI (2022)")
print("Date : 20SEP2022")

# Fonctions
def interface_attente():    
    pygame.draw.line(screen, r, (0, 160), (640, 160))
def interface(titre_musique, titre_album, artiste): # Paramètres : variable titre musique, artiste, AJOUTER GESTION DE L'ECRAN TACTILE ET LES MENUS
    font = pygame.font.Font(None, 32)
    albumcover = pygame.image.load("placeholder.png")
    pygame.draw.line(screen, g, (0, 160), (640, 160))
    titrem_interface = font.render(titre_musique, True, w)
    titrea_interface = font.render(titre_album, True, w)
    artiste_interface = font.render(artiste, True, w)
    screen.blit(titrem_interface, (200, 200))
    screen.blit(titrea_interface, (200, 250))
    screen.blit(artiste_interface, (200, 300))
    screen.blit(albumcover, (8, 200))


# Variables 
connected = False
#titre_musique = "0"
#titre_album = "1"
#artiste = "2"
# code_ok = True
# code_ko = False
# code_waiting = True # Ajouter condition si codes précédemment enregistrés, alors False
running = True
# Réseau
SERVER_HOST = "0.0.0.0" # Cette machine
SERVER_PORT = 5555
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
# Écran
screen_width = 640
screen_height = 400
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)

# Chargement et initialisation des libraries
import pygame
import socket
import tqdm
import os
import threading
import subprocess
from subprocess import call
# import logging
# logging.basicConfig(filename="latest.log", level=logging.DEBUG)
pygame.init()
print("Libraries chargées et initialisées.")
pygame.display.set_caption("Sharify v0.1-a")

# Lancement du serveur
def launch_server():
    call(["python3", "server.py"])
serverThread = threading.Thread(target=launch_server)
serverThread.start()
print("Serveur initialisé.")

# Initialisation écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle principale
while running:
    for event in pygame.event.get(): 
        try:
            spotifybar = pygame.image.load("Spotify_Code.png") #FileNotFoundError
            screen.blit(spotifybar, (0, 0))
            interface("Titre morceau", "Titre album", "Nom de l'artiste")        
            pygame.display.flip()
        except FileNotFoundError:
            spotifybar = pygame.image.load("Spotify_Code_empty.png")
            screen.blit(spotifybar, (0, 0))
            interface_attente()        
            pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False