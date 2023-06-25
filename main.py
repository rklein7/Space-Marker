import pygame
#import winsound
from tkinter import simpledialog


pygame.init()


pygame.init()
tamanho = (1000, 563)
branco = (255, 255, 255)
raiocirculo = 10
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
estrelas = {}
fundo = pygame.image.load("bg.jpg")
som = pygame.mixer.Sound("Space_Machine_Power.mp3")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)
som.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicaomouse = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrelas[item] = posicaomouse
            if item == "":
                item = "Desconhecido"+str(posicaomouse)
            estrelas[item] = posicaomouse
    
    for item,posicao in estrelas.items():
        pygame.draw.circle(tela,branco,posicao,raiocirculo)
        pygame.draw.line(tela,branco,list(estrelas.values())[0], posicao)
        fonte = pygame.font.Font(None,20)
        texto = fonte.render(item, True,(255,255,255))
        tela.blit(texto,(posicao[0]+10,posicao[1]+10))

    pygame.display.flip()
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    pygame.display.update()
    clock.tick(60)    
            








        
        
