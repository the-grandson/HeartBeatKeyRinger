from stl import mesh
import math
import numpy

import stl
# Create 3 faces of a cube

nms = [504,479,524,483,549,511,547,519,543,533]
##nms = []
##
##i = 0
##while i < len(nms_aux)-1:
##    if(nms_aux[i] != nms_aux[i+1]):
##        nms.append(nms_aux[i])
##    nms[i] = nms[i] * 50
##    i+=1
            

ntriangles = len(nms) * 14
data = numpy.zeros(ntriangles, dtype=mesh.Mesh.dtype)

previous_y = 0
actual_x = 100

#if possitive, upwards, else, downwards
upwards = True
downwards = False
previous_direction = upwards
actual_direction = upwards

j = 0
for i in range(len(nms)):
    actual_y = nms[i]
    # Top of the line
    data['vectors'][j] = numpy.array([[actual_x-100, actual_y, 50],[actual_x,actual_y,50],[actual_x-200,previous_y,50]])
    data['vectors'][j+1] = numpy.array([[actual_x,actual_y,50],[actual_x-100,previous_y,50],[actual_x-200,previous_y,50]])
    # Down of line
    data['vectors'][j+2] = numpy.array([[actual_x-100, actual_y, -50],[actual_x,actual_y,-50],[actual_x-200,previous_y,-50]])
    data['vectors'][j+3] = numpy.array([[actual_x,actual_y,-50],[actual_x-100,previous_y,-50],[actual_x-200,previous_y,-50]])
    # Right of line
    data['vectors'][j+4] = numpy.array([[actual_x-100, actual_y, -50],[actual_x-100,actual_y,50],[actual_x-200,previous_y,50]])
    data['vectors'][j+5] = numpy.array([[actual_x-200, previous_y, -50],[actual_x-200,previous_y,50],[actual_x-100,actual_y,-50]])
    # Left of line
    data['vectors'][j+6] = numpy.array([[actual_x, actual_y, -50],[actual_x,actual_y,50],[actual_x-100,previous_y,50]])
    data['vectors'][j+7] = numpy.array([[actual_x-100, previous_y, -50],[actual_x-100,previous_y,50],[actual_x,actual_y,-50]])

    if(i>0):
        if(nms[i] == nms[i-1]):
            continue
        if(nms[i] > nms[i-1]):
            actual_direction = upwards
        else:
            actual_direction = downwards


    scale = 200
    intermediate = 150
##    if(i<len(nms)):
##        if(nms_aux[i] != nms_aux[i+1]):
##            scale = 300
##            intermediate = 200
##        else:
##            scale = 200
##            intermediate = 150

    if(previous_direction != actual_direction):
        if(actual_direction == False):
            data['vectors'][j+8] = numpy.array([[actual_x-scale, previous_y, 50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y+intermediate,50]])
            data['vectors'][j+9] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-100,previous_y,-50],[actual_x-intermediate,previous_y+intermediate,-50]])
            #Left complementar
            data['vectors'][j+10] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-scale,previous_y,50],[actual_x-intermediate,previous_y+intermediate,-50]])
            data['vectors'][j+11] = numpy.array([[actual_x-intermediate, previous_y+intermediate, -50],[actual_x-intermediate,previous_y+intermediate,50],[actual_x-scale,previous_y,50]])
            #Right complementar
            data['vectors'][j+12] = numpy.array([[actual_x-100, previous_y, -50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y+intermediate,-50]])
            data['vectors'][j+13] = numpy.array([[actual_x-intermediate, previous_y+intermediate, -50],[actual_x-intermediate,previous_y+intermediate,50],[actual_x-100,previous_y,50]])
        else:
            data['vectors'][j+8] = numpy.array([[actual_x-scale, previous_y, 50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y-intermediate,50]])
            data['vectors'][j+9] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-100,previous_y,-50],[actual_x-intermediate,previous_y-intermediate,-50]])
            #Left complementar
            data['vectors'][j+10] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-scale,previous_y,50],[actual_x-intermediate,previous_y-intermediate,-50]])
            data['vectors'][j+11] = numpy.array([[actual_x-intermediate, previous_y-intermediate, -50],[actual_x-intermediate,previous_y-intermediate,50],[actual_x-scale,previous_y,50]])
            #Right complementar
            data['vectors'][j+12] = numpy.array([[actual_x-100, previous_y, -50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y-intermediate,-50]])
            data['vectors'][j+13] = numpy.array([[actual_x-intermediate, previous_y-intermediate, -50],[actual_x-intermediate,previous_y-intermediate,50],[actual_x-100,previous_y,50]])

##    if(previous_direction != actual_direction):
##        if(actual_direction == False):
##            data['vectors'][j+8] = numpy.array([[actual_x-scale, previous_y, 50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y+intermediate,50]])
##            data['vectors'][j+9] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-100,previous_y,-50],[actual_x-intermediate,previous_y+intermediate,-50]])
##            #Left complementar
##            data['vectors'][j+10] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-scale,previous_y,50],[actual_x-intermediate,previous_y+intermediate,-50]])
##            data['vectors'][j+11] = numpy.array([[actual_x-intermediate, previous_y+intermediate, -50],[actual_x-intermediate,previous_y+intermediate,50],[actual_x-scale,previous_y,50]])
##            #Right complementar
##            data['vectors'][j+12] = numpy.array([[actual_x-100, previous_y, -50],[actual_x-100,previous_y,50],[actual_x-intermediate,previous_y+intermediate,-50]])
##            data['vectors'][j+13] = numpy.array([[actual_x-intermediate, previous_y+intermediate, -50],[actual_x-intermediate,previous_y+intermediate,50],[actual_x-100,previous_y,50]])
##        else:
##            data['vectors'][j+8] = numpy.array([[actual_x-scale, previous_y, 50],[actual_x-100,previous_y,50],[actual_x-150,previous_y-150,50]])
##            data['vectors'][j+9] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-100,previous_y,-50],[actual_x-150,previous_y-150,-50]])
##            #Left complementar
##            data['vectors'][j+10] = numpy.array([[actual_x-scale, previous_y, -50],[actual_x-scale,previous_y,50],[actual_x-150,previous_y-150,-50]])
##            data['vectors'][j+11] = numpy.array([[actual_x-150, previous_y-150, -50],[actual_x-150,previous_y-150,50],[actual_x-200,previous_y,50]])
##            #Right complementar
##            data['vectors'][j+12] = numpy.array([[actual_x-100, previous_y, -50],[actual_x-100,previous_y,50],[actual_x-150,previous_y-150,-50]])
##            data['vectors'][j+13] = numpy.array([[actual_x-150, previous_y-150, -50],[actual_x-150,previous_y-150,50],[actual_x-100,previous_y,50]])

##    #Up complementar 
##    data['vectors'][j+8] = numpy.array([[actual_x-200, previous_y, 100],[actual_x-100,previous_y,100],[actual_x-150,previous_y+150,100]])
##    #Down complementar
##    data['vectors'][j+9] = numpy.array([[actual_x-200, previous_y, -100],[actual_x-100,previous_y,-100],[actual_x-150,previous_y+150,-100]])
##    #Left complementar
##    data['vectors'][j+10] = numpy.array([[actual_x-200, previous_y, -100],[actual_x-200,previous_y,100],[actual_x-150,previous_y+150,-100]])
##    data['vectors'][j+11] = numpy.array([[actual_x-150, previous_y+150, -100],[actual_x-150,previous_y+150,100],[actual_x-200,previous_y,100]])
##    #Right complementar
##    data['vectors'][j+12] = numpy.array([[actual_x-100, previous_y, -100],[actual_x-100,previous_y,100],[actual_x-150,previous_y+150,-100]])
##    data['vectors'][j+13] = numpy.array([[actual_x-150, previous_y+150, -100],[actual_x-150,previous_y+150,100],[actual_x-100,previous_y,100]])

    j+=14
    actual_x += 100
    previous_y = nms[i]
    previous_direction = actual_direction

###Top of line
##data['vectors'][0] = numpy.array([[0, 405, 100],[100,405,100],[0,0,100]])
##data['vectors'][1] = numpy.array([[100,405,100],[100,0,100],[0,0,100]])
###Down of line
##data['vectors'][2] = numpy.array([[0, 405, -100],[100,405,-100],[0,0,-100]])
##data['vectors'][3] = numpy.array([[100,405,-100],[100,0,-100],[0,0,-100]])
### Right of line
##data['vectors'][4] = numpy.array([[0, 405, -100],[0,405,100],[0,0,100]])
##data['vectors'][5] = numpy.array([[0, 0, -100],[0,0,100],[0,405,-100]])
### Left of line
##data['vectors'][6] = numpy.array([[100, 405, -100],[100,405,100],[100,0,100]])
##data['vectors'][7] = numpy.array([[100, 0, -100],[100,0,100],[100,405,-100]])
##
### Top of the line
##data['vectors'][8] = numpy.array([[100, 668, 100],[200,668,100],[0,405,100]])
##data['vectors'][9] = numpy.array([[200,668,100],[200,405,100],[0,405,100]])
### Down of line
##data['vectors'][10] = numpy.array([[100, 668, -100],[100,668,-100],[0,405,-100]])
##data['vectors'][11] = numpy.array([[200,668,-100],[100,405,-100],[0,405,-100]])
### Right of line
##data['vectors'][12] = numpy.array([[100, 668, -100],[100,668,100],[0,405,100]])
##data['vectors'][13] = numpy.array([[0, 405, -100],[0,405,100],[100,668,-100]])
### Left of line
##data['vectors'][14] = numpy.array([[200, 668, -100],[200,668,100],[100,405,100]])
##data['vectors'][15] = numpy.array([[100, 405, -100],[100,405,100],[200,668,-100]])
### Right face
##data['vectors'][2] = numpy.array([[1, 0, 0],
##[1, 0, 1],
##[1, 1, 0]])
##data['vectors'][3] = numpy.array([[1, 1, 1],
##[1, 0, 1],
##[1, 1, 0]])
### Left face
##data['vectors'][4] = numpy.array([[0, 0, 0],
##[1, 0, 0],
##[1, 0, 1]])
##data['vectors'][5] = numpy.array([[0, 0, 0],
##[0, 0, 1],
##[1, 0, 1]])
# Since the cube faces are from 0 to 1 we can move it to the middle by
# substracting .5
data['vectors'] -= .5
# Generate 4 different meshes so we can rotate them later
meshes = [mesh.Mesh(data.copy()) ]#for _ in range(4)
# Rotate 90 degrees over the Y axis
##meshes[0].rotate([0.0, 0.5, 0.0], math.radians(90))
### Translate 2 points over the X axis
##meshes[1].x += 2
### Rotate 90 degrees over the X axis
##meshes[2].rotate([0.5, 0.0, 0.0], math.radians(90))
### Translate 2 points over the X and Y points
##meshes[2].x += 2
##meshes[2].y += 2
### Rotate 90 degrees over the X and Y axis
##meshes[3].rotate([0.5, 0.0, 0.0], math.radians(90))
##meshes[3].rotate([0.0, 0.5, 0.0], math.radians(90))
# Translate 2 points over the Y axis
#meshes[3].y += 2
# Optionally render the rotated cube faces
from matplotlib import pyplot
from mpl_toolkits import mplot3d
# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
# Render the cube faces
for m in meshes:
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))
    # Auto scale to the mesh size
    scale = numpy.concatenate([m.points for m in meshes]).flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
# Show the plot to the screen
pyplot.show()

meshes[0].save('lisandro.stl', mode=stl.Mode.ASCII)
