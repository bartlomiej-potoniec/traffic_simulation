import pygame
import random


class Vehicle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 10)

    def move_forward(self):
        self.x += self.speed

    def move_backward(self):
        self.x -= self.speed

    def draw(self, screen):
        # draws rectangle as one vehicle
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 20, 10))


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1200, 850))
clock = pygame.time.Clock()

# Create vehicles
vehicles = [Vehicle(200, 200 + i * 20) for i in range(5)]
vehicles2 = [Vehicle(500, 400 - i * 20) for i in range(5)]

# Simulations loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # white screen
    screen.fill((255, 255, 255))

    for vehicle in vehicles:
        vehicle.move_forward()
        vehicle.draw(screen)

    for vehicle in vehicles2:
        vehicle.move_backward()
        vehicle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
