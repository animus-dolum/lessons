from PIL import Image


with Image.open('image.bmp') as im:
    x, y = im.size
    pxls = im.load()
    upper, lower = 0, y // 4
    for b in range(4):
        left, right = 0, x // 4
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save(f'image{b + 1}1.bmp')
        for a in range(3):
            left += x // 4
            right += x // 4
            im_crop = im.crop((left, upper, right, lower))
            if b + 1 == 4 and a + 2 == 4:
                pass
            else:
                im_crop.save(f'image{b + 1}{a + 2}.bmp')
        upper += y // 4
        lower += y // 4

