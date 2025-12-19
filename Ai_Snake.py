#codigo do humano modificado com as interaçoes de ia e apagando as do usuario, muitos comentarios foram perdidos or conta da quantidade de mudanças que ocorreram no codigo e mudanças na ia

import pygame  # importando os coisa
import sys
import random  # preocupado porque esta com cor de comentario, deve ser por conta do pc batata (tomara)

pygame.init()   # abrindo a pygame

WIDTH, HEIGHT = 600, 600  # config padrão pra testar a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Ia prot")

GRID_SIZE = 20  # tamanho da malha

font = pygame.font.SysFont(None, 30)  # fonte simples pra mostrar texto

snake_x = 300  # var para as informações da cobra
snake_y = 300

pontuation = 0  # pontuation :p

base_move_delay = 150  # tempo ok de passo inicial
move_delay = base_move_delay  # começa no valor base

last_move = pygame.time.get_ticks()


dir_x = 1# começa andando pra direita tipo o game de verdade
dir_y = 0

snake_body = [(snake_x, snake_y)]  # corpo da cobra
clock = pygame.time.Clock()

food_size = GRID_SIZE  # tds as var em ingles pq é universal né pae B)

game_over = False  # autoexplicativo



def spawn_food(snake_body):# garante que a comida nunca nasce dentro da cobra
    while True:
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)

        if (x, y) not in snake_body:
            return x, y



food_x, food_y = spawn_food(snake_body)# cria a primeira comida corretamente


ai_lock = 3          # quantos passos a decisão fica travada
locked_dir = None    # direção travada


DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}


def safe_go_to_food(snake_body, current_dir):
    head_x, head_y = snake_body[0]

    best_move = None
    best_dist = float("inf")

    for dx, dy in DIRECTIONS.values():


        if (-dx, -dy) == current_dir:# não deixa inverter
            continue

        new_x = head_x + dx * GRID_SIZE
        new_y = head_y + dy * GRID_SIZE


        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:# parede
            continue


        if (new_x, new_y) in snake_body:  # corpo
            continue


        dist = abs(new_x - food_x) + abs(new_y - food_y)# distância até a comida


        temp_body = [(new_x, new_y)] + snake_body[:-1]# simulação simples de segurança

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


        if escape == 0: # se não tem saída, ignora
            continue

        if dist < best_dist:
            best_dist = dist
            best_move = (dx, dy)

    return best_move


def follow_tail(snake_body, current_dir):
    head_x, head_y = snake_body[0]
    tail_x, tail_y = snake_body[-1]

    best_move = None
    best_dist = float("inf")

    for dx, dy in DIRECTIONS.values():


        if (-dx, -dy) == current_dir:# não inverte a direção
            continue

        new_x = head_x + dx * GRID_SIZE
        new_y = head_y + dy * GRID_SIZE


        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT: # parede
            continue


        if (new_x, new_y) in snake_body[:-1]: # ignora o último segmento pq o rabo anda
            continue

        dist = abs(new_x - tail_x) + abs(new_y - tail_y)

        if dist < best_dist:
            best_dist = dist
            best_move = (dx, dy)

    return best_move


running = True  # lopzinho de cria
while running:  # enquanto ta rodando roda, soq em ingles

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if game_over:
        if keys[pygame.K_r]: # se morreu, trava tudo e espera o reset
            snake_x = 300  # reseta as var
            snake_y = 300
            dir_x = 1
            dir_y = 0
            pontuation = 0
            snake_body = [(snake_x, snake_y)]
            food_x, food_y = spawn_food(snake_body)
            game_over = False

        screen.fill((0, 0, 0))
        text = font.render(
            f"GAME OVER - R reset | Q sair | Pontuação: {pontuation}",
            True,
            (200, 200, 200)
        )
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(60)

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

        continue


    # lógica da IA
    if ai_lock > 0 and locked_dir:
        dir_x, dir_y = locked_dir
        ai_lock -= 1
    else:
        move = safe_go_to_food(snake_body, (dir_x, dir_y))

        if move:
            locked_dir = move
            dir_x, dir_y = move
            ai_lock = 5  # trava a decisão por alguns passos
        else:
            move = follow_tail(snake_body, (dir_x, dir_y))
            if move:
                locked_dir = move
                dir_x, dir_y = move
                ai_lock = 3


    current_time = pygame.time.get_ticks()

    if current_time - last_move >= move_delay:
        last_move = current_time

        snake_x += dir_x * GRID_SIZE
        snake_y += dir_y * GRID_SIZE

        snake_body.insert(0, (snake_x, snake_y))


        if (snake_x, snake_y) in snake_body[1:]:
            game_over = True # colisão com o corpo

        snake_body.pop()



    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True# colisão com parede


    screen.fill((0, 0, 0))


    for x, y in snake_body:
        pygame.draw.rect(screen, (0, 200, 0), (x, y, GRID_SIZE, GRID_SIZE))# desenha a cobrona


    food_rect = pygame.Rect(food_x, food_y, food_size, food_size)
    pygame.draw.rect(screen, (200, 0, 0), food_rect) # desenha a comida


    if snake_body[0] == (food_x, food_y):
        food_x, food_y = spawn_food(snake_body)# comeu
        pontuation += 1
        snake_body.append(snake_body[-1])


        move_delay = max(50, base_move_delay - pontuation * 5) # acelera com a pontuação

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()#gg
