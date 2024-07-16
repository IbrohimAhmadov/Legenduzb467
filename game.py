import pygame
import sys
import random

pygame.init()

win_width = 710
win_height = 1400
win = pygame.display.set_mode((win_width, win_height))

white = (255, 255, 255)

walk_x = 170
walk_y = win_height // 2

left_go = False
right_go = False

bg = pygame.image.load('image/bg.jpg')
bg = pygame.transform.scale(bg, (win_height + 100, win_width + 100))
bg = pygame.transform.rotate(bg, 270)
bg_rect = bg.get_rect(center=(win_width // 2, win_height // 2))

player1_img = pygame.image.load('image/B1.png')
b2_img = pygame.image.load('image/B2.png')
b3_img = pygame.image.load('image/B3.png')
l1_img = pygame.image.load('image/l1.png')
l2_img = pygame.image.load('image/l2.png')
l3_img = pygame.image.load('image/l3.png')
r1_img = pygame.image.load('image/r1.png')
r2_img = pygame.image.load('image/r2.png')
r3_img = pygame.image.load('image/r3.png')

walk_images = [b2_img, player1_img, b3_img, b2_img]
left_walk_images = [l2_img, l1_img, l2_img, l3_img]
right_walk_images = [r2_img, r1_img, r2_img, r1_img]

coin_y = random.randint(100 , 1200)

class Object:
    def __init__(self, x, y, width, height, rotate, images):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = images
        self.rotate = rotate
        self.current_frame = 0
        self.velocity = [0, 0]
        self.animate = 0
        objects.append(self)

    def draw(self):
        rotated_image = pygame.transform.rotate(self.images[self.current_frame], self.rotate)
        scaled_image = pygame.transform.scale(rotated_image, (self.width, self.height))
        win.blit(scaled_image, (self.x, self.y))

    def update(self):
        self.current_frame = (self.current_frame + self.animate) % len(self.images)
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.draw()

    def walk_right(self):
        self.images = right_walk_images
        self.y += 15
        self.animate = 1
    def walk_left(self):
        self.images = left_walk_images
        self.y -= 15 
        self.animate = 1
    def stop(self):
        self.animate = 0
        
    def collidepoint(self, point):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(point)

class Coin:
    def __init__(self, x, y, width, height, image):
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height
        self.image = image
        coins.append(self)
        
    def draw(self):
        win.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
        
    def update(self):
        self.draw()
        
left = pygame.image.load('image/indicator.png')
left = pygame.transform.scale(left, (150, 120))
left = pygame.transform.rotate(left, 90)
left_rect = left.get_rect(center=(130, 60))

right = pygame.image.load('image/indicator.png')
right = pygame.transform.scale(right, (150, 120))
right = pygame.transform.rotate(right, 270)
right_rect = right.get_rect(center=(130, 230))

objects = []
coins = []
player1 = Object(walk_x, walk_y, 120, 90, 270, walk_images)
coin = Coin(175, coin_y, 90, 90, pygame.image.load('image/coin.png'))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if left_rect.collidepoint(event.pos):
                left_go = True
            if right_rect.collidepoint(event.pos):
                right_go = True
        elif event.type == pygame.MOUSEBUTTONUP:
            player1.stop()
            left_go = False
            right_go = False

    win.fill(white)
    win.blit(bg, bg_rect)
    for obj in objects:
        obj.update()
    for con in coins:
        con.update()
    if left_go:
        player1.walk_left()
    if right_go:
        player1.walk_right()
    win.blit(left, left_rect)
    win.blit(right, right_rect)
    
    player_rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
    coin_rect = pygame.Rect(coin.x, coin.y, coin.width, coin.height)
    
    if player_rect.colliderect(coin_rect):
        for con in coins:
            con.update()

    pygame.display.update()
    clock.tick(9)

pygame.quit()
sys.exit()