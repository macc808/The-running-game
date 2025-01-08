from pygame import *

# Ініціалізація Pygame
init()

# Створення вікна
WIDTH, HEIGHT = 700, 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Догонялки')


# Завантаження та масштабування фону
background = transform.scale(image.load("background.png"), (700, 500))
sprite1 = transform.scale(image.load("red_amongus left.png"),(100,100))
sprite2 = transform.scale(image.load("green amongus_amongus_left.png"),(100,100))
x1_red = 0
y1_red = 0
x1_green = 100
y1_green = 400
SPRITE_WIDTH, SPRITE_HEIGHT = 100, 100
FPS = 55
clock = time.Clock()
clock.tick(FPS)

# Основний цикл гри
game = True
while game:
    # Виведення фону на екран
    window.blit(background, (0,0))
    window.blit(sprite1,(x1_red,y1_red))
    window.blit(sprite2,(x1_green,y1_green))
    # Натиски на кнопки
    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_w] and y1_red > 0:  # Вверх
        y1_red -= 0.3
    if keys_pressed[K_s] and y1_red < HEIGHT - SPRITE_HEIGHT:  # Вниз
        y1_red += 0.3
    if keys_pressed[K_a] and x1_red > 0:  # Влево
        x1_red -= 0.3
    if keys_pressed[K_d] and x1_red < WIDTH - SPRITE_WIDTH:  # Вправо
        x1_red += 0.3

    # Зеленый персонаж
    if keys_pressed[K_UP] and y1_green > 0:  # Вверх
        y1_green -= 0.3
    if keys_pressed[K_DOWN] and y1_green < HEIGHT - SPRITE_HEIGHT:  # Вниз
        y1_green += 0.3
    if keys_pressed[K_LEFT] and x1_green > 0:  # Влево
        x1_green -= 0.3
    if keys_pressed[K_RIGHT] and x1_green < WIDTH - SPRITE_WIDTH:  # Вправо
        x1_green += 0.3
    
    rect_red = Rect(x1_red, y1_red, 70, 70)  # Прямоугольник вокруг красного
    rect_green = Rect(x1_green, y1_green, 70, 70)  # Прямоугольник вокруг зеленого

    if rect_red.colliderect(rect_green):  # Проверка перекрытия
        print("Столкновение! Игра окончена!")
        game = False
    # Обробка подій
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()


