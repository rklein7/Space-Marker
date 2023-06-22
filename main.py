import pygame



pygame.init()

tamanho = (1000,563)
tela = pygame.display.set_mode(tamanho)
imagem_fundo = pygame.image.load("bg.jpg")
icon = pygame.image.load("space.ico")
pygame.display.set_caption("SPACE MAKER")
pygame.display.set_icon(icon)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
marcador_estrela = []


    
    
