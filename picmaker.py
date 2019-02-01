# Maggie Zhao
# MKS66- Graphics
# 2019-01-31

import random, math
NUMROWS = 600;
NUMCOLS = 600;
minReal, maxReal = -1.5, 0.7
minIm, maxIm = -1.0, 1.0


def header(f) :
    f.write("P3\n")
    f.write(str(NUMCOLS) + " ")
    f.write(str(NUMROWS) + "\n")
    f.write("255\n")

def colorize(f):
    for i in range(NUMROWS):
        for j in range(NUMCOLS):
            n = mandelbrot(j, i) * 16
            r = j / 2
            g = n % 256
            b = j + i/4
            f.write(str(r) + " ")
            f.write(str(g) + " ")
            f.write(str(b) + "\t")
            # XXX:

        f.write("\n")

def mandelbrot(x,y):
    creal = x * ((maxReal - minReal) / NUMCOLS) + minReal
    cim = y * ((maxIm - minIm) / NUMROWS) + minIm

    zreal = creal
    zim = cim
    counter = 1
    while ((math.sqrt(zreal * zreal + zim * zim)) <= 2 and counter < 25):
        xreal = zreal
        zreal = creal + (zreal * zreal - zim * zim)
        zim = cim + (xreal * zim * 2)
        counter += 1
    return counter

f = open("image.ppm", "w")
header(f)
colorize(f)
f.close()
