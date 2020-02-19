import csv
import numpy as np
import pandas as pd
from PIL import Image

im = Image.open("psyduck_profile.jpg")
im = im.convert('1')
image_data = np.array(im)
x, y = image_data.shape


new_image_data = np.zeros((x,y))
for i in range(x):
    for j in range(y):
        if image_data[i][j] == True:
            new_image_data[i][j] = 1
        elif image_data[i][j] == False:
            new_image_data[i][j] = 0
    

df = pd.DataFrame(data=new_image_data, index=None)
with pd.ExcelWriter("image.xlsx") as writer:
    df.to_excel(writer)
    worksheet = writer.sheets['Sheet1']
