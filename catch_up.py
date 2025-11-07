from pygame import *

window = display.set_mode((700,500))
display.set_caption('Догонялки')
clock = time.Clock()
background = transform.scale(image.load('background.png'), (700,500))
game = True
x1 = 100
y1 = 50
x2 = 150
y2 = 200

sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x2,y2))
    window.blit(sprite2, (x1,y1))
    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_UP] and y1 > 5:
        y1 -= 10
    if key_pressed[K_DOWN] and y1 < 400:
        y1 += 10
    if key_pressed[K_LEFT] and x1 > 5:
        x1 -= 10
    if key_pressed[K_RIGHT] and x1 < 600:
        x1 += 10
    
    if key_pressed[K_w] and y2 > 5:
        y2 -= 10
    if key_pressed[K_s] and y2 < 400:
        y2 += 10
    if key_pressed[K_a] and x2 > 5:
        x2 -= 10
    if key_pressed[K_d] and x2 < 600:
        x2 += 10
    clock.tick(60)
    display.update()
