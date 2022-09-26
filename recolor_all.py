# recolors all files ending in .inp

import os

color_dict_name = None
for file in os.listdir():
	if file.endswith(".csv"):
		color_dict_name = file
if not color_dict_name:
	print('Error: No color dictionary!')
	quit()

for file in os.listdir():
	if file.endswith(".inp"):
		# Prints only text file present in My Folder
		print(f'recoloring file: {file}')
		os.system(f'python radmatcolor.py {file} {color_dict_name} {file}-recolor.inp')
