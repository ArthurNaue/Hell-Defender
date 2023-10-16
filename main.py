import pygame, sys, random
from inimigos import Inimigos

pygame.init()

screen = pygame.display.set_mode((600, 600))
branco = (255, 255, 255)

def __init__():
    main_menu()

def draw_text(text, font, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))

def main_menu():
    running = True
    pygame.display.set_caption("MAIN MENU")
    botao1 = pygame.Rect(250, 280, 100, 50)
    botao2 = pygame.Rect(250, 360, 100, 50)
    font = pygame.font.Font(None, 36)
    texto1 = "JOGAR"
    texto2 = "SAIR"
    texto1_surface = font.render(texto1, True, (0, 0, 0))
    texto1_rect = texto1_surface.get_rect()
    texto1_rect.center =  botao1.center
    texto2_surface = font.render(texto2, True, (0, 0, 0))
    texto2_rect = texto2_surface.get_rect()
    texto2_rect.center =  botao2.center
    cor = (186, 80, 68)

    while running:
        if pygame.mouse.get_pressed()[0] and botao1.collidepoint(pygame.mouse.get_pos()):
            game()
        if pygame.mouse.get_pressed()[0] and botao2.collidepoint(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()

        screen.fill(cor)

        pygame.draw.rect(screen, (branco), botao1)
        pygame.draw.rect(screen, (branco), botao2)
        screen.blit(texto1_surface, texto1_rect)
        screen.blit(texto2_surface, texto2_rect)

        draw_text("CASTLE", pygame.font.Font(None, 30), 260, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def game():
    pygame.display.set_caption("GAME")
    black = (0, 0, 0)
    screen.fill(black)
    running =  True
    castelo = pygame.image.load("Images/castelo.png")
    castelo_rect = pygame.Rect(275, 275, 50, 50)
    castelo_x = 236
    castelo_y = 236
    clock = pygame.time.Clock()
    spawn = pygame.USEREVENT + 1
    fps = 20
    indexImg = 0
    esqueleto = []
    esqueleto.append(pygame.image.load("Images/esqueleto_andando1.png"))
    esqueleto.append(pygame.image.load("Images/esqueleto_andando2.png"))
    ceifador = []
    ceifador.append(pygame.image.load("Images/ceifador_andando1.png"))
    ceifador.append(pygame.image.load("Images/ceifador_andando2.png"))
    aranha = []
    aranha.append(pygame.image.load("Images/aranha_andando1.png"))
    aranha.append(pygame.image.load("Images/aranha_andando1.png"))
    inimigo_spawn = False
    lista_inimigos1 = [esqueleto, ceifador]
    lista_inimigos2 = [esqueleto, ceifador, aranha]
    timer_spawn = 3000
    destino = (270, 300)
    background = pygame.image.load("Images/background.png")
    pontos = 0
    ataque = pygame.image.load("Images/ataque.png")
    cooldown = 60

    pygame.time.set_timer(spawn, timer_spawn)

    while running:
        multiplicador_velocidade = 1 + (pontos * 0.00005)

        if fps <= 30:
            fps -= 1
        if fps <= 0:
            fps = 30
            if indexImg == 1:
                indexImg -= 1
            else:
                indexImg += 1

        screen.blit(background, (0, 0))

        screen.blit(castelo, (castelo_x, castelo_y))

        if inimigo_spawn:
            screen.blit(inimigo.tipo[indexImg], inimigo.pos)
            inimigo.seguir(destino)

            if pygame.mouse.get_pressed()[0] and inimigo.rect.collidepoint(pygame.mouse.get_pos()):
                if cooldown == 0:
                    screen.blit(ataque, inimigo.pos)
                    vida -= 1
                    if vida < 1:
                        inimigo_spawn = False
                        if tipo == esqueleto:
                            pontos += 1
                            timer_spawn -= 100
                        elif tipo == ceifador:
                            pontos += 2
                            timer_spawn -= 200
                        elif tipo == aranha:
                            pontos += 2
                            timer_spawn -= 200
                    cooldown = 60

            if inimigo.rect.colliderect(castelo_rect):
                pygame.quit()
                sys.exit()
        
        draw_text("pontos: " + str(pontos), pygame.font.Font(None, 30), 460, 20)
        draw_text("cooldown: " + str(cooldown), pygame.font.Font(None, 30), 460, 40)

        if cooldown < 1:
            cooldown = 1
        cooldown -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == spawn:
                if inimigo_spawn == False:
                    inimigo_spawn = True
                    posicoes_possiveis = [(-10, -10), (-10, 810), (810, -10), (810, 810), (-10, 300), (300, -10), (300, 810), (810, 300)]
                    inimigo_position = random.choice(posicoes_possiveis)
                    if pontos < 5:
                        tipo = esqueleto
                    elif pontos < 10:
                        tipo = random.choice(lista_inimigos1)
                    elif pontos >= 10:
                        tipo = random.choice(lista_inimigos2)
                    if tipo == esqueleto:
                        vida = 1
                        if pontos == 0:
                            velocidade = 2
                        else:
                            velocidade = 2 * multiplicador_velocidade
                    if tipo == ceifador:
                        vida = 2
                        velocidade = 2 * multiplicador_velocidade
                    if tipo == aranha:
                        vida = 1
                        velocidade = 3 * multiplicador_velocidade
                    inimigo = Inimigos(tipo, vida, velocidade, inimigo_position[0], inimigo_position[1])

        pygame.display.update()

        clock.tick(60)

main_menu()