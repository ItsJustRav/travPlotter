####################### Traverse System Probe Visualisation ######################
####################### Northumbria Univeristy Wind Tunnel #######################
######################## script by Ravindu Ranaweera (2024) ######################

""" 
> Requirements: use environment file env_trav_plotter.yml to set-up/activate environment with required modules
> To set-up (first run), "conda env create -f env_trav_plotter.yml". This will set-up an environment "trav_plotter" with required modules. Only require during a fresh set-up
> To activate the already set-up environment, "conda activate trav_plotter"
> To update the installed trav_plotter environment, "conda update -f env_trav_plotter.yml"
"""

# Required modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
from stl import mesh
from pathlib import Path
import time
import sys

start_time = time.time()

########### Parameters ###########
# Probe co-ordinates
print('Setting parameters...')
probe_data_file = 'xyz_pointsi.txt'
rows_to_skip = 0 # 1st row 0 is counted
data_colums_to_use = (0,1,2) # 1st column 0 is counted, 3 columns minimum required.
plot_probe_labels = True # False to hide probe labels
name_column = (0) # Column number of the data labels, column 0 is counted
move_probes = True
move_probes_x, move_probes_y, move_probes_z = 0, 0, 0 # To align or move each probe as required by x, y, z amount.

# STL Model
stl_model = 'AB_.stl' # STL model location and name(case sensitive), path not required (only file name) if the model is in the same directory as the script. Will skip if path not found (leave empty to skip, i.e. '')
face_colour, show_wireframe, edge_colour= 'grey', 'False', 'darkgrey' # show_wireframe: True to show edges/wireframe, False to hide edges/wireframe
x_transform, y_transform, z_transform = 0, 0, 0 # Move the model by x, y z
x_rotate_stl, y_rotate_stl, z_rotate_stl, degrees_rotate_stl = 0, 0, 0, 0 # Co-ordinates (x, y, z) vector to rotate about and the degrees to rotate by

# Graph Customization
title = 'Northumbria University Wind Tunnel Traverse Sampling Preview'
x_label, y_label, z_label, show_grid = 'X', 'Y', 'Z', 'True' # Toggle grid using True or False
point_colour = 'red' # Colour of the points on graph
probe_marker = '.' # Symbol for points on graph
x_pad, y_pad, z_pad = 15, 15, 0 # Padding for axis labels
x_rot, y_rot, z_rot = 90, 90, 0 # Axis label rotation

## Axis limits and Intervals
x_start, x_end, x_interval = 0, 1900, 100
y_start, y_end, y_interval = 0, 1650, 100
z_start, z_end, z_interval = 0, 510, 100

## Initial view of the generated plot
change_default_view = True # True if a specific view is required. If true, enter parameters below.
elevation, azimuth = -4, -42  # Elevation angle in degrees (negative for looking down) & Azimuth angle in degrees (clockwise)

## Text to display on edge planes
display_text_top = True # False to hide text. If true, enter parameters below.
text_top,  text_top_colour, text_top_font_size = 'Tunnel Top', 'grey', 12
text_top_horizontal_alignment, text_top_vertical_alignment = 'center', 'top'
text_top_x, text_top_y, text_top_z = 950, 825, 900

display_text_floor = False # False to hide text. If true, enter parameters below.
text_floor, text_floor_colour, text_floor_font_size = 'Tunnel Floor', 'grey', 12
text_floor_horizontal_alignment, text_floor_vertical_alignment = 'center', 'top'
text_floor_x, text_floor_y, text_floor_z = 950, 825, -200

display_text_back = True # False to hide text. If true, enter parameters below.
text_back, text_back_colour, text_back_font_size = 'Tunnel Outlet', 'grey', 12
text_back_horizontal_alignment, text_back_vertical_alignment = 'right', 'center'
text_back_x,text_back_y, text_back_z = -100, 825, 255

display_text_doors = True # False to hide text. If true, enter parameters below.
text_doors, text_doors_colour, text_doors_font_size = 'Tunnel Right', 'grey', 12
text_doors_horizontal_alignment, text_doors_vertical_alignment = 'left', 'center'
text_doors_x, text_doors_y, text_doors_z = 950, 1750, 255

display_text_window = False # False to hide text. If true, enter parameters below.
text_window, text_window_colour, text_window_font_size = '', 'grey', 12
text_window_horizontal_alignment, text_window_vertical_alignment = 'right', 'center'
text_window_x, text_window_y, text_window_z = 950, -200, 255

display_text_inlet = False # False to hide text. If true, enter parameters below.
text_inlet, text_inlet_colour, text_inlet_font_size = '', 'grey', 12
text_inlet_horizontal_alignment = 'left'
text_inlet_vertical_alignment = 'center'
text_inlet_x, text_inlet_y, text_inlet_z = 2000, 825, 255

print('Parameters set')
########### Parameters End ###########

# Load probe data
probe_data_path = Path(probe_data_file)
if probe_data_path.exists():
    print(f'Loading data from {probe_data_file}')
    probe_data = np.loadtxt(probe_data_file, delimiter = ',', skiprows = rows_to_skip, usecols=data_colums_to_use)
    print('Data preview (first 5 lines):')
    print(probe_data[:5])
    #if move_probes == True:
            #moved_probe_data = probe_data[:,0] - move_probes_x
else:
    print(f'***WARNING:Probe data file {probe_data_file} not found. Aborting...')
    time.sleep(3)
    sys.exit()

# Plot
print('Generating plot...')
## Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
## Plot STL model if it exists
stl_filepath = Path(stl_model)
if stl_filepath.exists():
    print(f'Loading STL model {stl_model}')
    model_stl = mesh.Mesh.from_file(stl_model)
    translation = np.array([x_transform, y_transform, z_transform])
    model_stl.translate(translation)
    rotation_axis = np.array([x_rotate_stl, y_rotate_stl, z_rotate_stl])
    rotation_angle = np.deg2rad(degrees_rotate_stl)
    model_stl.rotate(rotation_axis, rotation_angle)
    poly_collection = mplot3d.art3d.Poly3DCollection(model_stl.vectors)
    ax.add_collection3d(poly_collection)
    poly_collection.set_facecolor(face_colour)
    if show_wireframe == 'True':
        poly_collection.set_edgecolor(edge_colour) # Colour for edges
        ax.add_collection3d(poly_collection)
else:
    print(f'***WARNING:STL model {stl_model} not found, skipping...')

## PLot 3D scatter of probe points
#ax.scatter3D(x_data, y_data, z_data, c=point_colour, marker=probe_marker)

print('Plotting probes')
ax.scatter3D(probe_data[:, 0],probe_data[:, 1], probe_data[:, 2], c=point_colour, marker=probe_marker)
print(f'Probe colour: {point_colour}')
print(f'Probe marker: {probe_marker}')

if plot_probe_labels == True:
    print('Adding probe labels')
    for i, (probe_name, x, y, z) in enumerate(probe_data):
      ax.text3D(x, y, z, probe_name, zdir='z', color='green', fontsize=8)
else:
    print('Probe labels skipped')

# Graph Customisation
print('Customising plot...')
## Rotating viewpoint
ax.view_init(elev=elevation, azim=azimuth)
print(f'View set: elevation {elevation}, azimuth {azimuth}')
ax.grid(show_grid)
print(f'Grid visibility:{show_grid}')
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_zlabel(z_label)
ax.set_title(title)
print('Axis labels and title set')
## Axis label rotation
ax.tick_params(axis='x', which='major', pad =x_pad, labelrotation=x_rot)
ax.tick_params(axis='y', which='major', pad =y_pad, labelrotation=y_rot)
ax.tick_params(axis='z', which='major', pad =z_pad, labelrotation=z_rot)
print(f'Setting axis label rotation: x {x_rot} degrees with pad {x_pad}, y {y_rot} degrees with pad {y_pad}, z {z_rot} degrees with pad {z_pad}')
## Axis limits (to flip any axes, change the switch the start and end variable below)
ax.set_xlim(x_start, x_end)
ax.set_ylim(y_start, y_end)
ax.set_zlim(z_start, z_end) 
print(f'Setting axis label limits: x {x_start} to {x_end}, y {y_start} to {y_end}, z {z_start} to {z_end}')
## Set ticks at intervals of 100 for all axes
ax.set_xticks(range(x_start, x_end, x_interval))
ax.set_yticks(range(y_start, y_end, y_interval))
ax.set_zticks(range(z_end, z_start, z_interval))
print(f'Setting axis intervals: x {x_interval}, y {y_interval}, z {z_interval}')
ax.set_aspect('equal')
## Text on edge planes
if display_text_top == 'True':
    ax.text(text_top_x, text_top_y, text_top_z, text_top, ha=text_top_horizontal_alignment, va=text_top_vertical_alignment, fontsize=text_top_font_size, color=text_top_colour)
    print('Top text set')
if display_text_floor == 'True':
    ax.text(text_floor_x, text_floor_y, text_floor_z, text_floor, ha=text_floor_horizontal_alignment, va=text_floor_vertical_alignment, fontsize=text_floor_font_size, color=text_floor_colour)
    print('Floor text set')
if display_text_back == 'True':
    ax.text(text_back_x, text_back_y, text_back_z, text_back, ha=text_back_horizontal_alignment, va=text_back_vertical_alignment, fontsize=text_back_font_size, color=text_back_colour)
    print('Back text set')
if display_text_doors == 'True':
    ax.text(text_doors_x, text_doors_y, text_doors_z, text_doors, ha=text_doors_horizontal_alignment, va=text_doors_vertical_alignment, fontsize=text_doors_font_size, color=text_doors_colour)
    print('Door side text set')
if display_text_window == 'True':
    ax.text(text_window_x, text_window_y, text_window_z, text_window, ha=text_window_horizontal_alignment, va=text_window_vertical_alignment, fontsize=text_window_font_size, color=text_window_colour)
    print('Window side text set')
if display_text_inlet == 'True':
    ax.text(text_inlet_x, text_inlet_y, text_inlet_z, text_inlet, ha=text_inlet_horizontal_alignment, va=text_inlet_vertical_alignment, fontsize=text_inlet_font_size, color=text_inlet_colour)
    print('Inlet text set')

plt.tight_layout()

end_time = time.time()
execution_time = end_time - start_time
print(f'Execution time: {execution_time:.2f} seconds')
print('Plotting complete...')

plt.show()