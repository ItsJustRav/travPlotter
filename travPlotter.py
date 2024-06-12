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

########### Parameters ###########
# Probe co-ordinates
x_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y_data = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600]
z_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

# STL Model
stl_model = 'AB_.stl'#STL model location and name(case sensitive), path not required (only file name) if the model is in the same directory as the script
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
elevation, azimuth = -4, -42  # Elevation angle in degrees (negative for looking down) & Azimuth angle in degrees (clockwise)

## Text to display on edge planes (set text_xxx to '' to hide, example: text_window = '', 'grey', 12)
text_top,  text_top_colour, text_top_font_size = 'Tunnel Top', 'grey', 12
text_top_horizontal_alignment, text_top_vertical_alignment = 'center', 'top'
text_top_x, text_top_y, text_top_z = 950, 825, 900

text_floor, text_floor_colour, text_floor_font_size = 'Tunnel Floor', 'grey', 12
text_floor_horizontal_alignment, text_floor_vertical_alignment = 'center', 'top'
text_floor_x, text_floor_y, text_floor_z = 950, 825, -200

text_back, text_back_colour, text_back_font_size = 'Tunnel Outlet', 'grey', 12
text_back_horizontal_alignment, text_back_vertical_alignment = 'right', 'center'
text_back_x,text_back_y, text_back_z = -100, 825, 255

text_doors, text_doors_colour, text_doors_font_size = 'Tunnel Right', 'grey', 12
text_doors_horizontal_alignment, text_doors_vertical_alignment = 'left', 'center'
text_doors_x, text_doors_y, text_doors_z = 950, 1750, 255

text_window, text_window_colour, text_window_font_size = '', 'grey', 12
text_window_horizontal_alignment, text_window_vertical_alignment = 'right', 'center'
text_window_x, text_window_y, text_window_z = 950, -200, 255

text_inlet, text_inlet_colour, text_inlet_font_size = '', 'grey', 12
text_inlet_horizontal_alignment = 'left'
text_inlet_vertical_alignment = 'center'
text_inlet_x, text_inlet_y, text_inlet_z = 2000, 825, 255

########### Parameters End ###########


# Plot

## Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
## Plot STL Model
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
## PLot 3D scatter of probe points
ax.scatter3D(x_data, y_data, z_data, c=point_colour, marker=probe_marker)


# Graph Customisation
## Rotating viewpoint
ax.view_init(elev=elevation, azim=azimuth)
ax.grid(show_grid)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_zlabel(z_label)
ax.set_title(title)
## Axis label rotation
ax.tick_params(axis='x', which='major', pad =x_pad, labelrotation=x_rot)
ax.tick_params(axis='y', which='major', pad =y_pad, labelrotation=y_rot)
ax.tick_params(axis='z', which='major', pad =z_pad, labelrotation=z_rot)
## Axis limits (to flip any axes, change the switch the start and end variable below)
ax.set_xlim(x_start, x_end)
ax.set_ylim(y_start, y_end)
ax.set_zlim(z_start, z_end) 
## Set ticks at intervals of 100 for all axes
ax.set_xticks(range(x_start, x_end, x_interval))
ax.set_yticks(range(y_start, y_end, y_interval))
ax.set_zticks(range(z_end, z_start, z_interval))
ax.set_aspect('equal')
## Text on edge planes
ax.text(text_top_x, text_top_y, text_top_z, text_top, ha=text_top_horizontal_alignment, va=text_top_vertical_alignment, fontsize=text_top_font_size, color=text_top_colour)
ax.text(text_floor_x, text_floor_y, text_floor_z, text_floor, ha=text_floor_horizontal_alignment, va=text_floor_vertical_alignment, fontsize=text_floor_font_size, color=text_floor_colour)
ax.text(text_back_x, text_back_y, text_back_z, text_back, ha=text_back_horizontal_alignment, va=text_back_vertical_alignment, fontsize=text_back_font_size, color=text_back_colour)
ax.text(text_doors_x, text_doors_y, text_doors_z, text_doors, ha=text_doors_horizontal_alignment, va=text_doors_vertical_alignment, fontsize=text_doors_font_size, color=text_doors_colour)
ax.text(text_window_x, text_window_y, text_window_z, text_window, ha=text_window_horizontal_alignment, va=text_window_vertical_alignment, fontsize=text_window_font_size, color=text_window_colour)
ax.text(text_inlet_x, text_inlet_y, text_inlet_z, text_inlet, ha=text_inlet_horizontal_alignment, va=text_inlet_vertical_alignment, fontsize=text_inlet_font_size, color=text_inlet_colour)

plt.tight_layout()

plt.show()