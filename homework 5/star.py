from turtle import *
speed (0)

def draw_star(x, y, length):
    for i in range (5):
        forward(100)
        left(144)

color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()

# random.randint function returns a random integer N such that -300 <= N <= 300