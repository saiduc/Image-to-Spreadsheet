import csv
import numpy as np
import pandas as pd
from PIL import Image

im = Image.open("psyduck_profile.jpg")
im = im.convert('1')
image_data = np.array(im)
x, y = image_data.shape
