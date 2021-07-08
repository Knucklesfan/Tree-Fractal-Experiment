
import math
import sys
import random
from PIL import Image, ImageDraw

def drawFractal(image, x1, y1, angle, depth, size, factor,color):
    if(depth > 0):
        x2 = x1 + math.cos(math.radians(angle)) * depth * size * factor
        y2 = y1 + math.sin(math.radians(angle)) * depth * size * factor
        image.line([(x1, y1),(x2,y2)], color, int(0.5*depth))
        drawFractal(id, x2, y2, angle, depth-2, size, factor,(random.randint(1, 255), 0, 0))
        drawFractal(id, x2, y2, angle - 35, depth-2, size, factor,(random.randint(1, 255), 0, 0))
        drawFractal(id, x2, y2, angle + 35, depth-2, size, factor,(random.randint(1, 255), 0, 0))

i = 0
tries = int(sys.argv[0])
images = []
while(i < tries):
    word = "Processing image #" + str(i) + "..."
    print(word)
    im = Image.new("RGB", (1280, 1280), (255, 255, 255, 0))
    id = ImageDraw.Draw(im,"RGB")
    random.seed(10)
    drawFractal(id, im.width/2, im.height - im.height/4, -90, i, 5, 1.0, (0,0,0,0))
    filename = "image" + str(i) + ".png"
    images.append(im)
    i+=1

images[0].save('gif.gif',
                save_all=True,
                append_images=images[1:],
                duration=100,
                loop=0)
