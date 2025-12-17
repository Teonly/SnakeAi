#codigo base do jogo, para  ser jogado por humanos
import pygame  # importando os coisa
import sys
import random  # preocupado porque esta com cor de comentario, deve ser por conta do pc batata (tomara)

pygame.init()   # abrindo a pygame

WIDTH, HEIGHT = 600, 600  # config padrão pra testar a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Ia prot")

GRID_SIZE = 20  # tamanho da malha (movimento travado tipo snake de verdade)

# fonte simples pra mostrar texto
font = pygame.font.SysFont(None, 30)

snake_x = 300  # var para as informações da cobra
snake_y = 300
pontuation = 0 #pontuation :p
base_move_delay = 150  # tempo ok de passo inicial


last_move = pygame.time.get_ticks()

# começa andando pra direita tipo o game de verdade
dir_x = 1
dir_y = 0
snake_body = [(snake_x, snake_y)]  # corpo da cobra
clock = pygame.time.Clock()

food_size = GRID_SIZE  # var em ingles pq é universal né pae B)
def spawn_food(snake_body):
    while True:
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)

        # garante que a comida não nasce dentro da cobra
        if (x, y) not in snake_body:
            return x, y


game_over = False  # autoexplicativo

running = True  # lopzinho de cria
while running:  # enquanto ta rodando roda, soq em ingles

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # se não tiver rodando não roda
    move_delay = max(50, base_move_delay - pontuation * 5) #fica mais rapido com apontuação, maximo para não ter vel infinita
    keys = pygame.key.get_pressed()  # essa biblioteca já le o teclado, facilitou muito

    # se morreu, trava tudo e espera o reset
    if game_over:
        if keys[pygame.K_r]:  # reset pra n ter que da exit direto
            snake_x = 300 #reseta as var tudo
            snake_y = 300
            dir_x = 1
            dir_y = 0
            pontuation=0
            snake_body = [(snake_x, snake_y)]
            food_x = random.randrange(0, WIDTH, GRID_SIZE)
            food_y = random.randrange(0, HEIGHT, GRID_SIZE)
            game_over = False
        screen.fill((0, 0, 0))
        text = font.render(
            f"GAME OVER - R reset | Q sair | Pontuação: {pontuation}",#escreve tudo na tela
            True,
            (200, 200, 200)
        )
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(60)
        if keys[pygame.K_q]:  #pra quitt

            pygame.quit()
            sys.exit()


        continue#trava o codigo ate o ser querer fazer alguma coisa



    # controle da cobra (não deixa inverter)
    if keys[pygame.K_UP] and dir_y == 0:
        dir_x = 0
        dir_y = -1
    elif keys[pygame.K_DOWN] and dir_y == 0:
        dir_x = 0
        dir_y = 1
    elif keys[pygame.K_LEFT] and dir_x == 0:
        dir_x = -1
        dir_y = 0
    elif keys[pygame.K_RIGHT] and dir_x == 0:
        dir_x = 1
        dir_y = 0

    current_time = pygame.time.get_ticks()  # tempo

    if current_time - last_move >= move_delay:
        last_move = current_time

        # anda um bloco
        snake_x += dir_x * GRID_SIZE
        snake_y += dir_y * GRID_SIZE

        snake_body.insert(0, (snake_x, snake_y))  # cresce pra frente

        # se colide com o proprio corpo morre
        if (snake_x, snake_y) in snake_body[1:]:
            game_over = True

        # se não comeu n fica grande
        snake_body.pop()

    # parana parede
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True

    # apaga a tela
    screen.fill((0, 0, 0))

    #desenha a cobrona
    for x, y in snake_body:
        pygame.draw.rect(screen, (0, 200, 0), (x, y, GRID_SIZE, GRID_SIZE))

    food_rect = pygame.Rect(food_x, food_y, food_size, food_size)  # comida
    pygame.draw.rect(screen, (200, 0, 0), food_rect)


    if snake_body[0] == (food_x, food_y): #cobra come comida huahaha
        food_x = random.randrange(0, WIDTH, GRID_SIZE)
        food_y = random.randrange(0, HEIGHT, GRID_SIZE)
        pontuation +=1
        snake_body.append(snake_body[-1])  # se come fica grande

    pygame.display.flip()
    clock.tick(60)  # pra n ser maluco esse tempo tá ok

pygame.quit()
sys.exit()
 #gg

