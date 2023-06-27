import pygame
from tkinter import Tk, simpledialog, messagebox

pygame.init()
tamanho = (1000, 563)
branco = (255, 255, 255)
preto = (0,0,0)
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
marcacoes = []
fonte = pygame.font.SysFont("Georgia", 20)

def saveMarks():
    with open("Estrelas Marcadas.txt", "w") as arquivo:
        for posicao, nome in marcacoes:
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")

def loadMarks():
    marcacoes.clear()
    try:
        with open("Estelas Marcadas.txt", "r") as arquivo:
            for linha in arquivo:
                x, y, nome = linha.strip().split(",")
                posicao = (int(x), int(y))
                marcacoes.append((posicao, nome))
    except FileNotFoundError:
        messagebox.showinfo("Erro", "Arquivo de marcações não encontrado.")

def excMarks():
    marcacoes.clear()

def escritasTela():
    texto_opcoes = fonte.render("Opções:", True, branco)
    texto_salvar = fonte.render("F10 - Salvar marcações", True, branco)
    texto_carregar = fonte.render("F11 - Carregar ultimas marcações", True, branco)
    texto_excluir = fonte.render("F12 - Excluir todas as marcações", True, branco)
    tela.blit(texto_opcoes, (10, 10))
    tela.blit(texto_salvar, (10, 40))
    tela.blit(texto_carregar, (10, 70))
    tela.blit(texto_excluir, (10, 100))

def get_star_name():
    root = Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    if star_name is None or star_name.strip() == "":
        star_name = "Desconhecido"
    return star_name

running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            saveMarks()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                saveMarks()
            elif evento.key == pygame.K_F10:
                saveMarks()
            elif evento.key == pygame.K_F11:
                loadMarks()
            elif evento.key == pygame.K_F12:
                excMarks()
        elif evento.type == pygame.MOUSEBUTTONUP:
            posicaomouse = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            estrelas[item] = posicaomouse
            if item == "":
                item = "Desconhecido"+str(posicaomouse)
            estrelas[item] = posicaomouse   

    tela.blit(fundo,(0,0))        

    for item,posicaos in estrelas.items():
        pygame.draw.circle(tela,branco,posicaos,raiocirculo)
        pygame.draw.line(tela,branco,list(estrelas.values())[0], posicaos)
        fonte = pygame.font.Font(None,20)
        texto = fonte.render(item, True,(255,255,255))
        tela.blit(texto,(posicaos[0]+10,posicaos[1]+10))


    escritasTela()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()  
            








        
        
