from PIL import Image


with Image.open('1.png') as im:
    x, y = im.size
    pxls = im.load()
    left, upper, right, lower = x, y, 0, 0
    for i in range(x):
        for j in range(y):
            if pxls[i, j] != pxls[0, 0]:
                if i < left:
                    left = i
                if i > right:
                    right = i
                if j > lower:
                    lower = j
                if j < upper:
                    upper = j
    im_crop = im.crop((left, upper, right + 1, lower + 1))
    im_crop.save('res.png')
