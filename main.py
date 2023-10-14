import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 600))

def __init__():
    main_menu()

def main_menu():
    running = True
    pygame.display.set_caption("MAIN MENU")
    botao1 = pygame.Rect(250, 280, 100, 50)
    botao2 = pygame.Rect(250, 360, 100, 50)
    font = pygame.font.Font(None, 36)
    texto = "JOGAR"
    texto_surface = font.render(texto, True, (0, 0, 0))
    texto_rect = texto_surface.get_rect()
    texto_rect.center =  botao1.center

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

        pygame.draw.rect(screen, (255, 255, 255), botao1)
        pygame.draw.rect(screen, (255, 255, 255), botao2)
        screen.blit(texto_surface, texto_rect)

        pygame.display.update()

def game():
    pygame.display.set_caption("GAME")
    black = (0, 0, 0)
    screen.fill(black)
    running =  True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main_menu()