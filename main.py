import pygame, sys, random
from inimigos import Inimigos

pygame.init()

screen = pygame.display.set_mode((600, 600))
branco = (255, 255, 255)

def __init__():
    main_menu()

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0] and botao1.collidepoint(pygame.mouse.get_pos()):
            game()
        if pygame.mouse.get_pressed()[0] and botao2.collidepoint(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (branco), botao1)
        pygame.draw.rect(screen, (branco), botao2)
        screen.blit(texto1_surface, texto1_rect)
        screen.blit(texto2_surface, texto2_rect)

        pygame.display.update()

def game():
    pygame.display.set_caption("GAME")
    black = (0, 0, 0)
    screen.fill(black)
    running =  True
    castelo = pygame.image.load("castelo.png")
    castelo_rect = castelo.get_rect()
    castelo_x = 236
    castelo_y = 236
    castelo_rect.topleft = (castelo_x, castelo_y)
    clock = pygame.time.Clock()
    spawn = pygame.USEREVENT + 1
    inimigo1 = pygame.image.load("player_down2.png")
    inimigo_spawn = False
    destino = (270, 300)

    pygame.time.set_timer(spawn, 3000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == spawn:
                if inimigo_spawn == False:
                    inimigo_spawn = True
                    inimigo_x = random.randint(0, 800)
                    inimigo_y = random.randint(0, 800)
                    inimigo = Inimigos(inimigo1, inimigo_x, inimigo_y)

        screen.fill((0, 0, 0))

        screen.blit(castelo, (castelo_x, castelo_y))

        if inimigo_spawn:
            screen.blit(inimigo.tipo, inimigo.pos)
            inimigo.seguir(destino)

            if pygame.mouse.get_pressed()[0] and inimigo.rect.collidepoint(pygame.mouse.get_pos()):
                inimigo_spawn = False
            
            if inimigo.rect.colliderect(castelo_rect):
                pygame.quit()
                sys.exit()

        pygame.display.update()

        clock.tick(60)

main_menu()