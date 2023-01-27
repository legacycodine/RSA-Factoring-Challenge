import os

a = os.path.join('/', "media", "davidwin")
b = os.listdir(a)
while True:
    try:
        c = os.path.join(a, b[0])
        d = os.listdir(c)
        print(d)
    except TypeError:
        print('.', end="")
