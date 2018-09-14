"This file uses data from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3584085/ to plot relationship between ommatidia size and eye radius in the same manner as was done by Barlow in 1952 (http://jeb.biologists.org/content/29/4/667) and McLeish in 2015 (http://rsfs.royalsocietypublishing.org/content/5/6/20150041)"

import math
import random
import matplotlib.pyplot as plt
import numpy as np

lengths = [2.1, 1.8, 3.2, 2.0, 1.6, 2.8, 2.9, 2.9, 3.6, 2.4, 2.4, 3.6, 2.1, 2.1, 2.8]
widths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ommatidia_ds = [25, 22, 38, 24, 22, 34, 35, 31, 46, 26, 25, 40, 26, 25, 36]

for i in range(15):
    widths[i] = lengths[i]/2.0

plt.suptitle('Bee Eyes')
plt.plot(widths[0:9], ommatidia_ds[0:9], 'bo', widths[10], ommatidia_ds[10], 'rs', widths[11:14], ommatidia_ds[11:14], 'bo')
plt.ylabel("Diameter of ommatidia -- $\mu$m")
plt.xlabel("sqrt of R (radius of the eye) -- mm")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Apis florea (yellow)')
plt.plot(widths[0:2], ommatidia_ds[0:2], 'yo', widths[3:9], ommatidia_ds[3:9], 'bo', widths[10], ommatidia_ds[10], 'bs', widths[11:14], ommatidia_ds[11:14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Apis andreniformis (green)')
plt.plot(widths[0:2], ommatidia_ds[0:2], 'bo', widths[3:5], ommatidia_ds[3:5], 'go', widths[6:9], ommatidia_ds[6:9], 'bo', widths[10], ommatidia_ds[10], 'bs', widths[11:14], ommatidia_ds[11:14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Apis dorsata (cyan)')
plt.plot(widths[0:5], ommatidia_ds[0:5], 'bo', widths[6:8], ommatidia_ds[6:8], 'co', widths[9], ommatidia_ds[9], 'bo', widths[10], ommatidia_ds[10], 'bs', widths[11:14], ommatidia_ds[11:14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Apis mellifera (red)')
plt.plot(widths[0:8], ommatidia_ds[0:8], 'bo', widths[9], ommatidia_ds[9], 'ro', widths[10], ommatidia_ds[10], 'rs', widths[11], ommatidia_ds[11], 'ro', widths[12:14], ommatidia_ds[12:14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Apis cerana (black)')
plt.plot(widths[0:9], ommatidia_ds[0:9], 'bo', widths[10], ommatidia_ds[10], 'bs', widths[11], ommatidia_ds[11], 'bo', widths[12:14], ommatidia_ds[12:14], 'ko')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Queens (red)')
plt.plot(widths[0], ommatidia_ds[0], 'ro', widths[1:2], ommatidia_ds[1:2], 'bo', widths[3], ommatidia_ds[3], 'ro', widths[4:5], ommatidia_ds[4:5], 'bo', widths[6], ommatidia_ds[6], 'ro', widths[7:8], ommatidia_ds[7:8], 'bo', widths[9], ommatidia_ds[9], 'ro', widths[10], ommatidia_ds[10], 'bs', widths[11], ommatidia_ds[11], 'bo', widths[12], ommatidia_ds[12], 'ro', widths[13:14], ommatidia_ds[13:14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Workers (red)')
plt.plot(widths[0], ommatidia_ds[0], 'bo', widths[1], ommatidia_ds[1], 'ro', widths[2], ommatidia_ds[2], 'bo', widths[3], ommatidia_ds[3], 'bo', widths[4], ommatidia_ds[4], 'ro', widths[5], ommatidia_ds[5], 'bo', widths[6], ommatidia_ds[6], 'bo', widths[7], ommatidia_ds[7], 'ro', widths[8], ommatidia_ds[8], 'bo', widths[9], ommatidia_ds[9], 'bo', widths[10], ommatidia_ds[10], 'rs', widths[11], ommatidia_ds[11], 'bo', widths[12], ommatidia_ds[12], 'bo', widths[13], ommatidia_ds[13], 'bo', widths[14], ommatidia_ds[14], 'bo')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()

plt.suptitle('Drones (red)')
plt.plot(widths[0:1], ommatidia_ds[0:1], 'bo', widths[2], ommatidia_ds[2], 'ro', widths[3:4], ommatidia_ds[3:4], 'bo', widths[5], ommatidia_ds[5], 'ro', widths[6:7], ommatidia_ds[6:7], 'bo', widths[8], ommatidia_ds[8], 'ro', widths[9], ommatidia_ds[9], 'bo', widths[10], ommatidia_ds[10], 'bs', widths[11], ommatidia_ds[11], 'ro', widths[12:13], ommatidia_ds[12:13], 'bo', widths[14], ommatidia_ds[14], 'ro')
plt.ylabel("Diameter of ommatidia (\mu m)")
plt.xlabel("sqrt of R(radius of the eye)")
plt.axis([0, 2.5, 0, 40])
plt.show()
