import pygame
import sys
import time
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Skrzyżowanie 4-wlotowe z sygnalizacją świetlną")

# Kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Parametry samochodów
CAR_SIZE = (30, 30)
CAR_SPEED = 3

# Funkcja rysująca sygnalizację świetlną
def draw_traffic_light(x, y, color):
    pygame.draw.rect(screen, BLACK, (x, y, 50, 150))
    pygame.draw.circle(screen, RED if color == 'red' else BLACK, (x + 25, y + 25), 20)
    pygame.draw.circle(screen, YELLOW if color == 'yellow' else BLACK, (x + 25, y + 75), 20)
    pygame.draw.circle(screen, GREEN if color == 'green' else BLACK, (x + 25, y + 125), 20)

# Klasa dla samochodów
class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.moving = True

    def move(self, light_state):
        if self.direction == 'up':
            if light_state == 'green' or (self.y < 300 and light_state != 'red'):
                self.y -= CAR_SPEED
            else:
                self.moving = False
        elif self.direction == 'down':
            if light_state == 'green' or (self.y > 300 and light_state != 'red'):
                self.y += CAR_SPEED
            else:
                self.moving = False
        elif self.direction == 'left':
            if light_state == 'green' or (self.x < 300 and light_state != 'red'):
                self.x -= CAR_SPEED
            else:
                self.moving = False
        elif self.direction == 'right':
            if light_state == 'green' or (self.x > 300 and light_state != 'red'):
                self.x += CAR_SPEED
            else:
                self.moving = False

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, CAR_SIZE[0], CAR_SIZE[1]))

# Główna pętla programu
def main():
    clock = pygame.time.Clock()
    light_color_x = 'red'
    light_color_y = 'green'
    last_change_time = time.time()

    cars = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Zmiana koloru sygnalizacji co 5 sekund
        current_time = time.time()
        if current_time - last_change_time > 5:
            # if light_color == 'red':
            #     light_color = 'green'
            # elif light_color == 'green':
            #     light_color = 'yellow'
            # elif light_color == 'yellow':
            #     light_color = 'red'
            if light_color_x == 'red':
                light_color_x = 'green'
                light_color_y = 'red'
            elif light_color_y == 'red':
                light_color_y = 'green'
                light_color_x = 'red'
            elif light_color_x == 'green':
                light_color_x = 'yellow'
                light_color_y = 'yellow'
            elif light_color_y == 'green':
                light_color_x = 'yellow'
                light_color_y = 'yellow'
            elif light_color_x == 'yellow':
                light_color_x = 'red'
                light_color_y = 'green'
            elif light_color_y == 'yellow':
                light_color_y = 'red'
                light_color_x = 'green'
            last_change_time = current_time

        # Losowe dodawanie samochodów
        if random.random() < 0.02:
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up':
                cars.append(Car(350, 600, 'up'))
            elif direction == 'down':
                cars.append(Car(200, 0, 'down'))
            elif direction == 'left':
                cars.append(Car(600, 200, 'left'))
            elif direction == 'right':
                cars.append(Car(0, 350, 'right'))

        # Rysowanie tła
        screen.fill(WHITE)

        # Rysowanie dróg
        pygame.draw.line(screen, BLACK, (300, 0), (300, 600), 5)  # Pionowa droga
        pygame.draw.line(screen, BLACK, (0, 300), (600, 300), 5)  # Pozioma droga

        # Rysowanie sygnalizacji świetlnej
        draw_traffic_light(250, 100, light_color_x)
        draw_traffic_light(250, 400, light_color_x)
        draw_traffic_light(100, 250, light_color_y)
        draw_traffic_light(400, 250, light_color_y)

        # Poruszanie i rysowanie samochodów
        for car in cars:
            if car.direction == 'right' or car.direction == 'left':
                light_color = light_color_y
            else:
                light_color = light_color_x

            car.move(light_color)
            car.draw()

        # Usuwanie samochodów poza ekranem
        cars = [car for car in cars if 0 <= car.x <= 600 and 0 <= car.y <= 600]

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()




