import pygame, sys, random
from inimigos import Inimigos

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("HELL DEFENDER")
pygame.display.set_icon(pygame.image.load("Images/icon.ico"))
branco = (255, 255, 255)
pygame.mixer.init()
musica = pygame.mixer.music.load("Sounds/musica.wav")
pygame.mixer.music.play(-1)
background = pygame.image.load("Images/background.png")

def __init__():
    main_menu()

def draw_text(text, font, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))

def sair():
    pygame.quit()
    sys.exit() 

def main_menu():
    running = True
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
    titulo = pygame.image.load("Images/titulo.png")

    while running:
        if pygame.mouse.get_pressed()[0] and botao1.collidepoint(pygame.mouse.get_pos()):
            game()
        if pygame.mouse.get_pressed()[0] and botao2.collidepoint(pygame.mouse.get_pos()):
            sair()

        screen.blit(background, (0,0))

        pygame.draw.rect(screen, (branco), botao1)
        pygame.draw.rect(screen, (branco), botao2)
        screen.blit(texto1_surface, texto1_rect)
        screen.blit(texto2_surface, texto2_rect)

        screen.blit(titulo, (175, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()

        pygame.display.update()

def game():
    black = (0, 0, 0)
    screen.fill(black)
    running =  True
    castelo = pygame.image.load("Images/castelo.png")
    castelo_rect = pygame.Rect(275, 275, 50, 50)
    castelo_pos = 236
    clock = pygame.time.Clock()
    spawn = pygame.USEREVENT + 1
    fps = 20
    indexImg = 0
    esqueleto = []
    esqueleto.append(pygame.image.load("Images/esqueleto1.png"))
    esqueleto.append(pygame.image.load("Images/esqueleto2.png"))
    ceifador = []
    ceifador.append(pygame.image.load("Images/ceifador1.png"))
    ceifador.append(pygame.image.load("Images/ceifador2.png"))
    aranha = []
    aranha.append(pygame.image.load("Images/aranha1.png"))
    aranha.append(pygame.image.load("Images/aranha2.png"))
    fantasma = []
    fantasma.append(pygame.image.load("Images/fantasma1.png"))
    fantasma.append(pygame.image.load("Images/fantasma2.png"))
    fogo = []
    fogo.append(pygame.image.load("Images/fogo1.png"))
    fogo.append(pygame.image.load("Images/fogo2.png"))
    inimigo_spawn = False
    lista_inimigos1 = [esqueleto, fantasma]
    lista_inimigos2 = [esqueleto, fantasma, aranha]
    destino = (270, 300)
    pontos = 0
    ataque = pygame.image.load("Images/ataque.png")
    cooldown = 60
    explosao = pygame.mixer.Sound("Sounds/explosion.wav")
    fogo1 = ((random.randint(32, 568)), (random.randint(32, 568)))
    fogo2 = ((random.randint(32, 568)), (random.randint(32, 568)))
    fogo3 = ((random.randint(32, 568)), (random.randint(32, 568)))
    fogo4 = ((random.randint(32, 568)), (random.randint(32, 568)))
    numero_fogos = random.randint(1, 4)
    pontos_boss = 3
    boss = False
    boss_rect = ceifador[0].get_rect()

    pygame.time.set_timer(spawn, 3000)

    while running:
        multiplicador_velocidade = 1 + (pontos * 0.01)

        if fps <= 30:
            fps -= 1
        if fps <= 0:
            fps = 30
            if indexImg == 1:
                indexImg -= 1
            else:
                indexImg += 1

        screen.blit(background, (0, 0))

        if numero_fogos == 1:
            screen.blit(fogo[indexImg], (fogo1[0], fogo1[1]))
        elif numero_fogos == 2:
            screen.blit(fogo[indexImg], (fogo2[0], fogo1[1]))
            screen.blit(fogo[indexImg], (fogo3[0], fogo2[1]))
        elif numero_fogos == 3:
            screen.blit(fogo[indexImg], (fogo1[0], fogo1[1]))
            screen.blit(fogo[indexImg], (fogo2[0], fogo2[1]))
            screen.blit(fogo[indexImg], (fogo3[0], fogo3[1]))
        elif numero_fogos == 4:
            screen.blit(fogo[indexImg], (fogo1[0], fogo1[1]))
            screen.blit(fogo[indexImg], (fogo2[0], fogo2[1]))
            screen.blit(fogo[indexImg], (fogo3[0], fogo3[1]))
            screen.blit(fogo[indexImg], (fogo4[0], fogo4[1]))

        screen.blit(castelo, (castelo_pos, castelo_pos))

        if inimigo_spawn:
            if pygame.mouse.get_pressed()[0] and inimigo.rect.collidepoint(pygame.mouse.get_pos()):
                if cooldown == 0:
                    screen.blit(ataque, inimigo.pos)
                    vida -= 1
                    explosao.play()
                    if vida < 1:
                        inimigo_spawn = False
                        if tipo == fantasma:
                            pontos += 1
                        elif tipo == esqueleto:
                            pontos += 2
                        elif tipo == aranha:
                            pontos += 3
                    cooldown = 60

            screen.blit(inimigo.tipo[indexImg], inimigo.pos)
            inimigo.seguir(destino)

            if inimigo.rect.colliderect(castelo_rect):
                sair()

        if boss:
            boss_rect.topleft = boss_pos

            if boss_pos[0] < destino[0]:
                boss_pos[0] += 0.35
            if boss_pos[0] > destino[0]:
                boss_pos[0] -= 0.35
            if boss_pos[1] < destino[1]:
                boss_pos[1] += 0.35
            if boss_pos[1] > destino[1]:
                boss_pos[1] -= 0.35

            if pygame.mouse.get_pressed()[0] and boss_rect.collidepoint(pygame.mouse.get_pos()):
                if cooldown == 0:
                    screen.blit(ataque, boss_pos)
                    boss_vida -= 1
                    explosao.play()
                    if boss_vida < 1:
                        boss = False
                    cooldown = 60

            screen.blit(ceifador[indexImg], boss_pos)
            draw_text("BOSS", pygame.font.Font(None, 40), 260, 70)
            draw_text(str(boss_vida), pygame.font.Font(None,50), 290, 100)

        draw_text("pontos: " + str(pontos), pygame.font.Font(None, 30), 460, 20)
        draw_text("cooldown: " + str(cooldown), pygame.font.Font(None, 30), 460, 40)

        if cooldown < 1:
            cooldown = 1
        cooldown -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()
            elif event.type == spawn:
                if inimigo_spawn == False:
                    inimigo_spawn = True
                    posicoes_possiveis = [(-100, -100), (-100, 320), (-100, 700), (300, 700), (700, 700), (700, 320), (700, -100), (300, -100)]
                    inimigo_position = random.choice(posicoes_possiveis)
                    if pontos < 10:
                        tipo = fantasma
                    elif pontos < 20:
                        tipo = random.choice(lista_inimigos1)
                    elif pontos >= 20:
                        tipo = random.choice(lista_inimigos2)
                    if tipo == fantasma:
                        vida = 1
                        if pontos == 0:
                            velocidade = 2
                        else:
                            velocidade = 2 * multiplicador_velocidade
                    if tipo == esqueleto:
                        vida = 2
                        velocidade = 1 * multiplicador_velocidade
                    if tipo == aranha:
                        vida = 1
                        velocidade = 2.5 * multiplicador_velocidade
                    inimigo = Inimigos(tipo, vida, velocidade, inimigo_position[0], inimigo_position[1])
                
                if pontos >= pontos_boss:
                    pontos_boss = pontos_boss * 2
                    if boss == False:
                        boss = True
                        posicoes_possiveis2 = [(-100, -100), (-100, 320), (-100, 700), (300, 700), (700, 700), (700, 320), (700, -100), (300, -100)]
                        boss_vida = 5
                        boss_pos = pygame.Vector2(random.choice(posicoes_possiveis2))
                        boss = Inimigos(ceifador, boss_vida, 0.35, boss_pos[0], boss_pos[1])
                        boss.seguir(destino)

        pygame.display.update()

        clock.tick(60)

main_menu()