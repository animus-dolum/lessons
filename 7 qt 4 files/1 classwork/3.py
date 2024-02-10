def reverse():
    with open('input.dat', 'rb', encoding='utf-8') as f:
        dt = f.read()[::-1]
    with open('output.dat', 'wb', encoding='utf-8') as f:
        f.write(dt)
