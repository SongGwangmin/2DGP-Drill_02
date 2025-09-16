from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while True:
    #사각형
    while x < 800:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)

    while y < 560:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y += 2
        delay(0.01)

    while x > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x -= 2
        delay(0.01)

    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)

    while x < 400:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 2
        delay(0.01)
    #원
    x = 400
    y = 90
    theta = 1.5 * math.pi
    for i in range(0, 180):
        clear_canvas()
        grass.draw(400, 30)
        #x = (x - 400) * math.cos(2 * math.pi / 180) - (y - 300) * math.sin(2 * math.pi / 180) + 400
        #y = (x - 400) * math.sin(2 * math.pi / 180) + (y - 300) * math.cos(2 * math.pi / 180) + 300
        # 반지름이 어떻게 될까 ----- 300 - 90 = 210
        x = 400 + 210 * math.cos(theta)
        y = 300 + 210 * math.sin(theta)
        theta -= 2 * math.pi / 180

        character.draw(x , y)
        update_canvas()
        delay(0.01)
    x = 400
    y = 90
    delay(0.01)

close_canvas()
