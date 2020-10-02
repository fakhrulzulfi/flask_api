from PIL import Image

img = Image.open('/home/julpi/Pictures/Screenshot from 2020-04-26 11-01-18.png')

basewidth = 1000

wpercent = (basewidth/float(img.size[0]))

hsize = int((float(img.size[1]) * float(wpercent)))
print(wpercent, hsize)

img_resize = img.resize((basewidth, hsize), Image.BICUBIC)
print(img_resize)
img_resize.save('../a.png')

print('done')