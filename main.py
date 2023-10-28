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


def draw_text(text, font, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))


def read_high_score():
    with open("high score.txt", "r") as f:
        return f.read()


def quit():
    pygame.quit()
    sys.exit()


def main_menu():
    running = True
    button1 = pygame.image.load("Images/botao.png")
    button2 = pygame.image.load("Images/botao.png")
    button3 = pygame.image.load("Images/botao.png")
    buttonRect1 = button1.get_rect()
    buttonRect2 = button2.get_rect()
    buttonRect3 = button3.get_rect()
    buttonRect1.topleft = (250, 300)
    buttonRect2.topleft = (250, 400)
    buttonRect3.topleft = (250, 500)
    font = pygame.font.Font(None, 36)
    text = False
    text1 = "JOGAR"
    text2 = "AJUDA"
    text3 = "SAIR"
    textSur1 = font.render(text1, True, (0, 0, 0))
    textRect1 = textSur1.get_rect()
    textRect1.center = buttonRect1.center
    textSur2 = font.render(text2, True, (0, 0, 0))
    textRect2 = textSur2.get_rect()
    textRect2.center = buttonRect2.center
    textSur3 = font.render(text3, True, (0, 0, 0))
    textRect3 = textSur3.get_rect()
    textRect3.center = buttonRect3.center
    tittle = pygame.image.load("Images/titulo.png")
    button4 = pygame.image.load("Images/botao2.png")
    buttonRect4 = button4.get_rect()
    buttonRect4.topleft = (100, 350)
    highScore = int(read_high_score())
    text4 = str(highScore)
    textSur4 = font.render(text4, True, (0, 0, 0))
    textRect4 = textSur4.get_rect()
    textRect4.center = buttonRect4.center

    while running:
        if pygame.mouse.get_pressed()[0] and buttonRect1.collidepoint(
            pygame.mouse.get_pos()
        ):
            game()
        if pygame.mouse.get_pressed()[0] and buttonRect2.collidepoint(
            pygame.mouse.get_pos()
        ):
            text = True
        if pygame.mouse.get_pressed()[0] and buttonRect3.collidepoint(
            pygame.mouse.get_pos()
        ):
            quit()

        screen.blit(background, (0, 0))
        screen.blit(button1, (250, 300))
        screen.blit(button2, (250, 400))
        screen.blit(button3, (250, 500))
        screen.blit(textSur1, textRect1)
        screen.blit(textSur2, textRect2)
        screen.blit(textSur3, textRect3)
        screen.blit(textSur4, textRect4)
        screen.blit(button4, (100, 350))
        draw_text("HIGH", pygame.font.Font(None, 30), 125, 360)
        draw_text("SCORE", pygame.font.Font(None, 30), 115, 380)
        screen.blit(tittle, (50, -100))

        if text:
            draw_text("+ PONTOS = + RAPIDO", pygame.font.Font(None, 30), 360, 390)
            draw_text("CLIQUE PARA MATAR", pygame.font.Font(None, 30), 368, 360)
            draw_text("SE TE PEGAREM", pygame.font.Font(None, 30), 390, 420)
            draw_text("VOCE MORRE!", pygame.font.Font(None, 30), 400, 450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()


def game():
    def sprites(variable_name, img1_loc, img2_loc):
        variable_name.append(pygame.image.load(img1_loc))
        variable_name.append(pygame.image.load(img2_loc))

    def fogoPos():
        return random.randint(32, 568)

    black = (0, 0, 0)
    screen.fill(black)
    running = True
    castelo = pygame.image.load("Images/castelo.png")
    castelo_rect = pygame.Rect(275, 275, 50, 50)
    castelo_pos = 236
    clock = pygame.time.Clock()
    spawn = pygame.USEREVENT + 1
    fps = 20
    indexImg = 0
    esqueleto = []
    sprites(esqueleto, "Images/esqueleto1.png", "Images/esqueleto2.png")
    ceifador = []
    sprites(ceifador, "Images/ceifador1.png", "Images/ceifador2.png")
    aranha = []
    sprites(aranha, "Images/aranha1.png", "Images/aranha2.png")
    fantasma = []
    sprites(fantasma, "Images/fantasma1.png", "Images/fantasma2.png")
    fogo = []
    sprites(fogo, "Images/fogo1.png", "Images/fogo2.png")
    olho = []
    sprites(olho, "Images/olho1.png", "Images/olho2.png")
    inimigo_spawn = False
    lista_inimigos1 = [esqueleto, fantasma]
    lista_inimigos2 = [esqueleto, fantasma, aranha]
    boss_spawn = False
    lista_boss = [ceifador, olho]
    destino = (270, 300)
    pontos = 0
    ataque = pygame.image.load("Images/ataque.png")
    cooldown = 60
    explosao = pygame.mixer.Sound("Sounds/explosion.wav")
    fogo1 = ((fogoPos()), (fogoPos()))
    fogo2 = ((fogoPos()), (fogoPos()))
    fogo3 = ((fogoPos()), (fogoPos()))
    fogo4 = ((fogoPos()), (fogoPos()))
    numero_fogos = random.randint(1, 4)
    pontos_boss = 15
    contagem_boss = 0
    posicoes_possiveis = [
        (-100, -100),
        (-100, 275),
        (-100, 700),
        (275, 700),
        (700, 700),
        (700, 275),
        (700, -100),
        (275, -100),
    ]
    pygame.time.set_timer(spawn, 3000)

    try:
        high_score = int(read_high_score())
    except:
        high_score = 0

    while running:
        if high_score < pontos:
            high_score = pontos
        with open("high score.txt", "w") as f:
            f.write(str(high_score))

        multiplicador_velocidade = 1 + (pontos * 0.005)

        if fps <= 30:
            fps -= 1
        if fps <= 0:
            fps = 30
            if indexImg == 1:
                indexImg -= 1
            else:
                indexImg += 1

        screen.blit(background, (0, 0))

        def sprite_fogo(fogo_pos1, fogo_pos2):
            screen.blit(fogo[indexImg], (fogo_pos1, fogo_pos2))

        if numero_fogos == 1:
            sprite_fogo(fogo1[0], fogo1[1])
        elif numero_fogos == 2:
            sprite_fogo(fogo1[0], fogo1[1])
            sprite_fogo(fogo2[0], fogo2[1])
        elif numero_fogos == 3:
            sprite_fogo(fogo1[0], fogo1[1])
            sprite_fogo(fogo2[0], fogo2[1])
            sprite_fogo(fogo3[0], fogo3[1])
        elif numero_fogos == 4:
            sprite_fogo(fogo1[0], fogo1[1])
            sprite_fogo(fogo2[0], fogo2[1])
            sprite_fogo(fogo3[0], fogo3[1])
            sprite_fogo(fogo4[0], fogo4[1])

        screen.blit(castelo, (castelo_pos, castelo_pos))

        if inimigo_spawn:
            if pygame.mouse.get_pressed()[0] and inimigo.rect.collidepoint(
                pygame.mouse.get_pos()
            ):
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
                explosao.play()
                game_over()

        draw_text("pontos: " + str(pontos), pygame.font.Font(None, 30), 460, 560)
        draw_text("cooldown: " + str(cooldown), pygame.font.Font(None, 30), 40, 560)

        if cooldown < 1:
            cooldown = 1
        cooldown -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == spawn:
                if inimigo_spawn == False:
                    inimigo_spawn = True
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
                    inimigo = Inimigos(
                        tipo, vida, velocidade, inimigo_position[0], inimigo_position[1]
                    )

                if pontos >= pontos_boss:
                    pontos_boss = pontos_boss * 2
                    if boss_spawn == False:
                        boss_spawn = True
                        contagem_boss += 1
                        boss_pos = pygame.Vector2(random.choice(posicoes_possiveis))
                        if contagem_boss == 1:
                            boss_tipo = ceifador
                            boss_vida = 5
                            boss_velocidade = 0.35
                        if contagem_boss == 2:
                            boss_tipo = olho
                            boss_vida = 8
                            boss_velocidade = 0.04
                        if contagem_boss >= 3:
                            boss_tipo = random.choice(lista_boss)
                            if boss_tipo == ceifador:
                                boss_vida = 5
                                boss_velocidade = 0.35
                            if boss_tipo == olho:
                                boss_vida = 8
                                boss_velocidade = 0.04
                        boss = Inimigos(
                            boss_tipo,
                            boss_vida,
                            boss_velocidade,
                            boss_pos[0],
                            boss_pos[1],
                        )
                        boss.seguir(destino)

        if boss_spawn:
            boss_rect = boss.tipo[0].get_rect()
            boss_rect.topleft = boss_pos

            if boss_pos[0] < destino[0]:
                boss_pos[0] += 0.35
            if boss_pos[0] > destino[0]:
                boss_pos[0] -= 0.35
            if boss_pos[1] < destino[1]:
                boss_pos[1] += 0.35
            if boss_pos[1] > destino[1]:
                boss_pos[1] -= 0.35

            if pygame.mouse.get_pressed()[0] and boss_rect.collidepoint(
                pygame.mouse.get_pos()
            ):
                if cooldown == 0:
                    screen.blit(ataque, boss_pos)
                    boss_vida -= 1
                    explosao.play()
                    if boss_vida < 1:
                        boss_spawn = False
                    cooldown = 60

            screen.blit(boss.tipo[indexImg], boss_pos)
            if boss_tipo == ceifador:
                draw_text("REAPER", pygame.font.Font(None, 40), 240, 70)
                draw_text(str(boss_vida), pygame.font.Font(None, 50), 290, 100)
            elif boss_tipo == olho:
                draw_text("EYE OF TRUTH", pygame.font.Font(None, 40), 195, 70)
                draw_text(str(boss_vida), pygame.font.Font(None, 50), 290, 100)

            if boss_rect.colliderect(castelo_rect):
                explosao.play()
                game_over()

        pygame.display.update()

        clock.tick(60)


def game_over():
    running = True
    botao1 = pygame.image.load("Images/botao.png")
    botao2 = pygame.image.load("Images/botao.png")
    botao1_rect = botao1.get_rect()
    botao2_rect = botao2.get_rect()
    botao1_rect.topleft = (250, 300)
    botao2_rect.topleft = (250, 400)
    botao3 = pygame.image.load("Images/botao2.png")
    botao3_rect = botao3.get_rect()
    botao3_rect.topleft = (400, 300)
    font = pygame.font.Font(None, 36)
    texto1 = "JOGAR"
    texto2 = "SAIR"
    texto1_surface = font.render(texto1, True, (0, 0, 0))
    texto1_rect = texto1_surface.get_rect()
    texto1_rect.center = botao1_rect.center
    texto2_surface = font.render(texto2, True, (0, 0, 0))
    texto2_rect = texto2_surface.get_rect()
    texto2_rect.center = botao2_rect.center
    titulo = pygame.image.load("Images/game_over.png")
    high_score = int(read_high_score())
    texto3 = str(high_score)
    texto3_surface = font.render(texto3, True, (0, 0, 0))
    texto3_rect = texto3_surface.get_rect()
    texto3_rect.center = botao3_rect.center

    while running:
        if pygame.mouse.get_pressed()[0] and botao1_rect.collidepoint(
            pygame.mouse.get_pos()
        ):
            game()
        if pygame.mouse.get_pressed()[0] and botao2_rect.collidepoint(
            pygame.mouse.get_pos()
        ):
            quit()

        screen.blit(background, (0, 0))
        screen.blit(botao1, (250, 300))
        screen.blit(botao2, (250, 400))
        screen.blit(texto1_surface, texto1_rect)
        screen.blit(texto2_surface, texto2_rect)
        screen.blit(botao3, (400, 300))
        screen.blit(titulo, (40, -100))
        draw_text("HIGH", pygame.font.Font(None, 30), 425, 310)
        draw_text("SCORE", pygame.font.Font(None, 30), 415, 330)
        screen.blit(texto3_surface, texto3_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()



main_menu()
