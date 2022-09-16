# script to color materials in Radiant input

# Script can be run in terminal with arguments:
# python radmatcolor.py <input_name> <material_color_directory> [<output_name> <additional_changes>]

# TO DO: Some materials should be invisible.
#        Script should add visability section and make
#        bodies with invisible materials invisible.

import regex as re
import os
import sys
import csv

# BIG CHANGE

print('big change')

### READING ARGUMENTS IN TERMINAL ###
if len(sys.argv) == 1:      # no arguments
    print('\nScript radmatcolor.py recolors your radiant input (.inp file) as described in material color dictionary (.csv file).\nTo run:\npython radmatcolor.py <rad_input> <mat_color_dict> [<output_name>]\nHere arguments inside [] are optional.\nFor help run:\npython radmatcolor.py -h\n')
    quit()
elif len(sys.argv) == 2:    # one argument (help or example)
    arg = sys.argv[1]
    if arg == '-h' or arg == '-help':
        print('\nFor alternative script modes use:\npython radmatcolor.py -option\n\nWith options:\n\t-h\tor -help\t for help\n\t-e\tor -example\t for example files\n')
    elif arg == '-e' or arg == '-example':
        print('Make example rad.inp and color_dict.csv')
    quit()
elif len(sys.argv) > 3:     # specified output name
    in_name = sys.argv[1]
    mat_color_dict_name = sys.argv[2]
    out_name = os.path.splitext(sys.argv[3])[0]
    specified_out_name = True
else:
    in_name = sys.argv[1]   # not specified output name
    mat_color_dict_name = sys.argv[2]
    out_name = os.path.splitext(in_name)[0]
    specified_out_name = False

### READING MATERIAL COLOR DICTIONARY FILE ###
mat_file = open(mat_color_dict_name, mode='r')
mat_reader = csv.reader(mat_file)
mat_color = {}
for rows in mat_reader:
    mat_color[int(rows[0])] = f'  {rows[1]}  {rows[2]}  {rows[3]}  {rows[4]}  '

### OPENING RADIANT INPUT FILE ###
in_file = open(in_name, 'r')
in_lines = in_file.readlines()
in_file.close()

### READING MATERIALS IN RADIANT INPUT ###
line_mat = []       # a list of materials in each line of Radiant input file 
for i in in_lines:
    mat = re.findall(r'm(\d+)', i)
    # print(mat)
    if len(mat) > 1: print(f'Error: more than one material in line:\n\t{i}')
    elif len(mat) == 1: line_mat.append(int(mat[0]))
    else: line_mat.append(None)

### MAKING NEW RADIANT INPUT ###
out_lines = []
# Go trough all lines
for i,v in enumerate(line_mat):
    if not v:
        out_lines.append(in_lines[i])               # copy old line if no material is asigned
        change = 'no material'
    else:                                           # if material is asigned do more checks
        if list(mat_color.keys()).count(v) > 0:     # is the material the one we want to change?
           # we need to change the color code:
           new_color = mat_color[v]
           changed_line = re.sub(r'\s+\d+\s+\d+\s+\d+\s+\d+\s+!', f'{new_color}!', in_lines[i])
           out_lines.append(changed_line)
           change = f'material {v} has been changed to {new_color}'
        else:
            out_lines.append(in_lines[i])
            change = f"didn't change material {v}"
    print(f'line {i:03}:\t{change}')

### FILE SAVING ###
if specified_out_name:
    out_file = open(f'{out_name}.inp', 'w')
    out_file.writelines(out_lines)
    out_file.close()
else:
    def format(i): return f'{out_name}-{i:03}.inp'
    i = 1
    is_file = os.path.isfile(format(i))
    while is_file:
        i += 1
        is_file = os.path.isfile(format(i))
    out_file = open(format(i), 'w')
    out_file.writelines(out_lines)
    out_file.close()