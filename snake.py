import pygame,sys,time,random
from pygame.locals import *
scale = 300
pygame.init()
play_surface = pygame.display.set_mode((scale,scale))
pygame.display.set_caption(f"Snake")
fps = pygame.time.Clock()
def food_spawn():
    x = random.randint(0,((scale/10)-1))*10
    y = random.randint(0,((scale/10)-1))*10
    spawn = [x,y]
    return spawn

def main():
    snake_pos = [100,50]
    snake_body = [[100,50], [90,50], [80,50]]
    direction = "RIGHT"
    change = direction
    food_pos = food_spawn()
    score = 0


    run = True
    while run:
        for event in pygame.event.get():
            #Salir del juego
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_q or event.type == pygame.QUIT:
                    run = False
            #Detectar teclas de direccion
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        #comprobar que no se mueva hacia atras
        if change == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        if change == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change == "UP" and direction != "DOWN":
            direction = "UP"
        if change == "DOWN" and direction != "UP":
            direction = "DOWN"
        #Mover serpiente
        if direction == "RIGHT":
            snake_pos[0] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10

        #Insertar
        snake_body.insert(0, list(snake_pos))
        #Comprobar que este en la posicion de la comida
        if snake_pos == food_pos:
            food_pos = food_spawn() #si se encuentra con la comida se crea otra
            score +=1 #se añade un punto al score
            #y se omite el corte de la ultima posicion mientras esté en contacto con la comida
        else: #sino
            snake_body.pop(-1) #corta la ultima posicion
        #comprueba que no toque los bordes de la pantalla
        myfont = pygame.font.SysFont("monospace", 16)
        gameover = myfont.render("GAME OVER!", 1, (255, 255, 255))

        if snake_pos[0] >= scale or snake_pos[0] < 0:
            play_surface.blit(gameover,((scale/2)-50,(scale/2)-50))
            pygame.display.flip()
            time.sleep(3)
            run = False
        if snake_pos[1] >= scale or snake_pos[1] < 0:
            play_surface.blit(gameover, ((scale / 2) - 50, (scale / 2) - 50))
            pygame.display.flip()
            time.sleep(3)
            run = False
        #comprueba que no toque su cuerpo
        if snake_pos in snake_body[1:]:
            play_surface.blit(gameover, ((scale / 2) - (scale/10), (scale / 2) - (scale/10)))
            pygame.display.flip()
            time.sleep(3)
            run = False
        play_surface.fill((0,0,0))
        #dibuja el cuerpo de la serpiente
        for pos in snake_body:
            pygame.draw.rect(play_surface,(200,200,200), pygame.Rect(pos[0],pos[1],10,10))
        #dibuja la comida
        pygame.draw.rect(play_surface,(200,0,0),pygame.Rect(food_pos[0],food_pos[1],10,10))


        scoretext = myfont.render("Score = " + str(score), 1, (255, 255, 255))

        play_surface.blit(scoretext, (5, 10))

        pygame.display.flip()
        fps.tick(10)

main()
pygame.quit()

if __name__ == "__main__":
    main()
    pygame.quit()