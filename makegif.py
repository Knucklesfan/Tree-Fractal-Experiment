from os import listdir
from os.path import isfile, join

from PIL import Image, ImageDraw;

images = []
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
onlyfiles = sorted(onlyfiles)

for n in onlyfiles:
    if n.endswith(".png"):
        frame = Image.open(n)
        images.append(frame)

images[0].save('gif.gif',
                save_all=True,
                append_images=images[1:],
                duration=100,
                loop=0)
