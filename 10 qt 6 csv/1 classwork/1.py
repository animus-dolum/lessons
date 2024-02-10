with open('input.bmp', 'rb') as f:
    data = f.read()
    data = list(data[:54]) + list(map(lambda x: 255 - x, list(data[54:])))

with open('res.bmp', 'wb') as f:
    f.write(bytes(data))
