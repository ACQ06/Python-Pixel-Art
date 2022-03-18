import numpy as np
from PIL import Image

##CANVAS SIZE
x = 27
y = 27
array = np.zeros([y, x, 3], dtype=np.uint8)

##COLOR VALUES
w = [255, 255, 255]
r = [255, 0, 0]
b = [0, 0, 0]

##SETTING UP A 27X27 PIXEL ART
array[:, :] = [[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, b, b, b, b, b, b, b, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, b, b, b, w, r, r, r, w, b, b, b, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, b, b, r, w, r, r, r, r, r, w, r, b, b, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, b, w, r, r, r, r, r, r, r, r, r, w, b, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, b, w, w, r, r, w, w, w, r, r, w, w, b, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, w, w, w, r, w, w, w, w, w, r, w, w, w, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, w, w, w, r, w, w, w, w, w, r, w, w, w, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, w, w, r, r, w, w, w, w, w, r, r, w, w, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, r, r, r, r, r, w, w, w, r, r, r, r, r, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, r, r, b, b, b, b, b, b, b, b, b, r, r, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, b, b, b, b, w, w, b, w, b, w, w, b, b, b, b, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, b, b, w, w, w, b, w, b, w, w, w, b, b, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, b, w, w, w, w, w, w, w, w, w, b, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, b, b, w, w, w, w, w, w, w, b, b, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, b, b, b, b, b, b, b, b, b, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

##ARRAY TO IMAGE
img = Image.fromarray(array)

##RESIZE AND PIXELATE
(width, height) = (img.width * 40, img.height * 40)
img_resized = img.resize((width, height), Image.NEAREST)

##SHOWING IMAGE
img_resized.show()

##SAVING IMAGE
img_resized.save('PIXELART.PNG')
