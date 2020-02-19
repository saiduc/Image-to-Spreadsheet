import csv
import numpy as np
import pandas as pd
from PIL import Image

image = "psyduck_profile.jpg"
im = Image.open(image)
im = im.convert('1')
image_data = np.array(im)
x, y = image_data.shape


new_image_data = np.zeros((x, y))
for i in range(x):
    for j in range(y):
        if image_data[i][j] == True:
            new_image_data[i][j] = 1
        elif image_data[i][j] == False:
            new_image_data[i][j] = 0

df = pd.DataFrame(data=new_image_data, index=None, columns=None)
writer = pd.ExcelWriter('image.xlsx', engine="xlsxwriter")
df.to_excel(writer, sheet_name='Sheet1', index=None, header=None)

workbook = writer.book
worksheet = writer.sheets['Sheet1']
worksheet.conditional_format('A1:XFD1048576', {'type': '2_color_scale'})
writer.save()
