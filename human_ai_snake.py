#isso deu um trabalho pq n quis reescrever tudo e tentei fazer um franquenstain dos dis outros codigos, tentando mudar a ia pra ficar melhor
#só coloquei os dois codigos em uma if else e mudei um pouco a ia, trocando o lock para ter dois diferentes ao inves de um (não tive mudança significativa no desempenho dela)

import pygame  # importando os coisa
import sys
import random  # preocupado porque esta com cor de comentario, deve ser por conta do pc batata (tomara)

pygame.init()   # abrindo a pygame

WIDTH, HEIGHT = 600, 600  # config padrão pra testar a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Human + IA")

GRID_SIZE = 20  # tamanho da malha (movimento travado tipo snake de verdade)

font = pygame.font.SysFont(None, 30)  # fonte simples pra mostrar texto



snake_x = 300  # posição inicial da cobra
snake_y = 300
snake_body = [(snake_x, snake_y)]  # corpo da cobra

dir_x = 1  # começa andando pra direita
dir_y = 0

pontuation = 0  # pontuation :p

base_move_delay = 150  # tempo base do movimento
last_move = pygame.time.get_ticks()

clock = pygame.time.Clock()

game_over = False

# modo do jogo
# 0 = IA
# 1 = humano
mode = 0



food_size = GRID_SIZE  # tamanho da comida

def spawn_food(snake_body):
    while True:
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)

        # garante que a comida não nasce dentro da cobra
        if (x, y) not in snake_body:
            return x, y

food_x, food_y = spawn_food(snake_body)



DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

ai_lock = 0          # quantos passos a decisão fica travada
locked_dir = None    # direção travada


def safe_go_to_food(snake_body, current_dir):
    head_x, head_y = snake_body[0]

    best_move = None
    best_dist = float("inf")

    for dx, dy in DIRECTIONS.values():


        if (-dx, -dy) == current_dir: # não deixa inverter
            continue

        new_x = head_x + dx * GRID_SIZE
        new_y = head_y + dy * GRID_SIZE


        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:# parede
            continue


        if (new_x, new_y) in snake_body:# corpo
            continue

        dist = abs(new_x - food_x) + abs(new_y - food_y)  # distância até a comida


        temp_body = [(new_x, new_y)] + snake_body[:-1] # simulação simples de segurança

        escape = 0
        for nx, ny in DIRECTIONS.values():
            tx = new_x + nx * GRID_SIZE
            ty = new_y + ny * GRID_SIZE

            if (
                0 <= tx < WIDTH and
                0 <= ty < HEIGHT and
                (tx, ty) not in temp_body
            ):
                escape += 1


        if escape == 0: # se ficar sem saída, só desiste
            continue


        if dist < best_dist: # escolhe o caminho mais próximo da comida
            best_dist = dist
            best_move = (dx, dy)

    return best_move


def follow_tail(snake_body, current_dir):
    head_x, head_y = snake_body[0]
    tail_x, tail_y = snake_body[-1]

    best_move = None
    best_dist = float("inf")

    for dx, dy in DIRECTIONS.values():

        if (-dx, -dy) == current_dir:
            continue

        new_x = head_x + dx * GRID_SIZE
        new_y = head_y + dy * GRID_SIZE


        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:# parede
            continue


        if (new_x, new_y) in snake_body[:-1]:  # ignora o último segmento pq o rabo anda
            continue

        dist = abs(new_x - tail_x) + abs(new_y - tail_y)

        if dist < best_dist:
            best_dist = dist
            best_move = (dx, dy)

    return best_move



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_h]:# troca de modo
        mode = 1  # humano
    if keys[pygame.K_i]:
        mode = 0  # IA

    move_delay = max(50, base_move_delay - pontuation * 5)


    if game_over:
        if keys[pygame.K_r]:
            snake_x = 300
            snake_y = 300
            snake_body = [(snake_x, snake_y)]
            dir_x = 1
            dir_y = 0
            pontuation = 0
            food_x, food_y = spawn_food(snake_body)
            game_over = False
            ai_lock = 0
            locked_dir = None

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        text = font.render(
            f"GAME OVER | R reset | Q sair | Pontuação: {pontuation}",
            True,
            (200, 200, 200)
        )
        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2)
        )
        pygame.display.flip()
        clock.tick(60)
        continue


    if mode == 1:# controle humano

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

    else:# controle da IA

        if ai_lock > 0 and locked_dir:
            dir_x, dir_y = locked_dir
            ai_lock -= 1
        else:
            move = safe_go_to_food(snake_body, (dir_x, dir_y))

            if move:
                locked_dir = move
                dir_x, dir_y = move
                ai_lock = 6  # controla quanto tempo a IA mantém a decisão de comer
            else:
                move = follow_tail(snake_body, (dir_x, dir_y))
                if move:
                    locked_dir = move
                    dir_x, dir_y = move
                    ai_lock = 4 #mesma coisa mas pra seguir a cauda


    current_time = pygame.time.get_ticks()

    if current_time - last_move >= move_delay:
        last_move = current_time

        snake_x += dir_x * GRID_SIZE
        snake_y += dir_y * GRID_SIZE

        snake_body.insert(0, (snake_x, snake_y))

        if (snake_x, snake_y) in snake_body[1:]:
            game_over = True

        snake_body.pop()


    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:# parede
        game_over = True


    screen.fill((0, 0, 0))

    for x, y in snake_body:
        pygame.draw.rect(screen, (0, 200, 0), (x, y, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(
        screen,
        (200, 0, 0),
        (food_x, food_y, food_size, food_size)
    )


    if snake_body[0] == (food_x, food_y):# comeu
        food_x, food_y = spawn_food(snake_body)
        pontuation += 1
        snake_body.append(snake_body[-1])


    mode_text = "HUMANO" if mode == 1 else "IA" # escreve o modo
    info = font.render(f"Modo: {mode_text}", True, (200, 200, 200))
    screen.blit(info, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit() #gg
