import numpy as np
import matplotlib.pyplot as plt
import os
import imp

os.add_dll_directory('D:\\Lumarical\\v202\\api\\python')
lumapi = imp.load_source('lumapi', 'D:\\Lumarical\\v202\\api\\python\\lumapi.py')

fdtd = lumapi.FDTD()

def setupB(delta=0):
	global fdtd

	delta = int(delta)
	for i in range(1,14+delta):
		fdtd.setnamed("circle_8_"+str(i), "enabled", False)
	for i in range(14+delta, 26):
		fdtd.setnamed("circle_8_"+str(i), "enabled", True)
	start = 13+delta
	for i in range(13, 24):
		fdtd.setnamed("circle_9_"+str(i), "enabled", i!=start and i-1!=start)
		fdtd.setnamed("circle_9_"+str(i+1), "enabled", i!=start)
		fdtd.setnamed("circle_10_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_11_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_12_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_13_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_14_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_15_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_16_"+str(i+5), "enabled", i!=start)

def setupA(delta=0):
	global fdtd

	delta = int(delta)
	for i in range(1,14+delta):
		fdtd.setnamed("circle_28_"+str(i), "enabled", False)
	for i in range(14+delta, 26):
		fdtd.setnamed("circle_28_"+str(i), "enabled", True)
	start = 13+delta
	for i in range(13, 24):
		fdtd.setnamed("circle_27_"+str(i), "enabled", i!=start and i-1!=start)
		fdtd.setnamed("circle_27_"+str(i+1), "enabled", i!=start)
		fdtd.setnamed("circle_26_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_25_"+str(i+2), "enabled", i!=start)
		fdtd.setnamed("circle_24_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_23_"+str(i+3), "enabled", i!=start)
		fdtd.setnamed("circle_22_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_21_"+str(i+4), "enabled", i!=start)
		fdtd.setnamed("circle_20_"+str(i+5), "enabled", i!=start)

  
Xsize = 21e-6
Ysize = 16e-6
Zsize = 0.22e-6

space = 10e-6

dy = 0.4330127272727273e-6

fdtd.addrect()
fdtd.set('x', 0.0)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)
fdtd.set('z span', Zsize)
fdtd.set('index', 2.44);

fdtd.addfdtd()
fdtd.set('x', 0.0)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)

fdtd.set('dimension', '2D')
fdtd.set('simulation time', 10000e-15)
fdtd.set('dt stability factor', 0.8)

#fdtd.set('layers', 16)
fdtd.set('mesh accuracy', 8)

fdtd.addpower()
fdtd.set('name', 'monitor')
fdtd.set('monitor type', 'Linear Y')
fdtd.set('x', 9.0e-6)
fdtd.set('y', 0.e-6)
fdtd.set('y span', 0.6e-6)
fdtd.set('z', Zsize/2.0)

fdtd.set('override global monitor settings', True)
fdtd.set('frequency points', 1000)

fdtd.set('output Px', True)
fdtd.set('output Py', True)
fdtd.set('output Pz', True)

lineSource = [10, -10, 0]
sourceName = ['source A', 'source B', 'source S']

for i in range(3):
	fdtd.addmode()
	fdtd.set('name', sourceName[i])
	fdtd.set('x', -9.25e-6)
	fdtd.set('y', dy*lineSource[i])
	fdtd.set('y span', 1.176e-6)
	fdtd.set('z', Zsize/2.0)
	fdtd.set('z span', 10.0e-6)
	fdtd.set('number of trial modes', 20)
	fdtd.set('center wavelength', 1.55e-6)
	fdtd.set('wavelength span', 0.0)
	fdtd.set('mode selection', 'fundamental TE mode')

####################################
###### CILINDERS GENERATION ########
####################################

fdtd.addstructuregroup()
fdtd.set("name", "Cilinders Group")
fdtd.set("x", -8.5e-6)
fdtd.set("y", 0.0)
fdtd.set("z", Zsize/2.0)
fdtd.groupscope("Cilinders Group")

z_span = 0.22e-6
index = 2.44
material = 'etch'
ny = 35
nx = 33
a = 0.5e-6
radius = 1.55e-7

n_rows = 2*round((ny-1)/2)
n_cols = nx
even_flag = 0

for i in range(round(-n_rows/2), round(n_rows/2) + 1):
  for j in range(1, n_cols + 1):
    if i!=0 or (i == 0 and j == 17):
    	if i == 0 and j == 17:
    		even_flag = 0
    	fdtd.addcircle()
    	fdtd.set("name", "circle_" + str(i+18) + "_" + str(j))
    	fdtd.set("radius",radius)
    	if even_flag==0:
    		fdtd.set("x",(j-1)*a + a/2)
    	else :
    		fdtd.set("x",(j-1)*a)
    	fdtd.set("y",(i)*a*np.sqrt(3)/2)
    	fdtd.set("z",0)
    	fdtd.set("z span",z_span)
    	fdtd.set("material",material)
    	if fdtd.get("material")=="<Object defined dielectric>":
    		fdtd.set("index",index)
  if even_flag==0:
    even_flag=1
  else:
    even_flag=0
  if i == 0:
    even_flag = 0

fdtd.save('myNand.fsp')

fdtd.groupscope('::model')

fdtd.addstructuregroup()
fdtd.set("name", "Rectangle Group")
fdtd.set("x", 0.0)
fdtd.set("y", 0.0)
fdtd.set("z", Zsize/2.0)
fdtd.groupscope("Rectangle Group")

positRecLeft = -9.15e-6
positRecRight = 8.65e-6
recSizeX = 1.8e-6
recSizeY = 0.32e-6
recSizeZ = 0.36e-6

recLines = [-11, -9, -1, 1, 9, 11]
recLinesOut = [-1, 1]

for i in recLines:
	fdtd.addrect()
	fdtd.set('x', positRecLeft)
	fdtd.set('x span', recSizeX)
	fdtd.set('y', dy*i)
	fdtd.set('y span', recSizeY)
	fdtd.set('z', Zsize/2.0)
	fdtd.set('z span', recSizeZ)
	fdtd.set("material",material)

for i in recLinesOut:
	fdtd.addrect()
	fdtd.set('x', positRecRight)
	fdtd.set('x span', recSizeX)
	fdtd.set('y', dy*i)
	fdtd.set('y span', recSizeY)
	fdtd.set('z', Zsize/2.0)
	fdtd.set('z span', recSizeZ)
	fdtd.set("material",material)

fdtd.groupscope('::model')

fdtd.groupscope("Cilinders Group")
fdtd.setnamed('circle_17_'+str(18), 'radius', 70)
fdtd.setnamed('circle_17_'+str(19), 'radius', 70)
fdtd.setnamed('circle_17_'+str(17), 'radius', 70)

#setupB
delta = 0
for i in range(1,14+delta):
	fdtd.setnamed("circle_8_"+str(i), "enabled", False)
for i in range(14+delta, 26):
	fdtd.setnamed("circle_8_"+str(i), "enabled", True)
start = 13+delta
for i in range(13, 24):
	fdtd.setnamed("circle_9_"+str(i), "enabled", i!=start and i-1!=start)
	fdtd.setnamed("circle_9_"+str(i+1), "enabled", i!=start)
	fdtd.setnamed("circle_10_"+str(i+2), "enabled", i!=start)
	fdtd.setnamed("circle_11_"+str(i+2), "enabled", i!=start)
	fdtd.setnamed("circle_12_"+str(i+3), "enabled", i!=start)
	fdtd.setnamed("circle_13_"+str(i+3), "enabled", i!=start)
	fdtd.setnamed("circle_14_"+str(i+4), "enabled", i!=start)
	fdtd.setnamed("circle_15_"+str(i+4), "enabled", i!=start)
	fdtd.setnamed("circle_16_"+str(i+5), "enabled", i!=start)

#setupA
delta = 10
for i in range(1,14+delta):
	fdtd.setnamed("circle_28_"+str(i), "enabled", False)
for i in range(14+delta, 26):
	fdtd.setnamed("circle_28_"+str(i), "enabled", True)
start = 13+delta
for i in range(13, 24):
	fdtd.setnamed("circle_27_"+str(i), "enabled", i!=start and i-1!=start)
	fdtd.setnamed("circle_27_"+str(i+1), "enabled", i!=start)
	fdtd.setnamed("circle_26_"+str(i+2), "enabled", i!=start)
	fdtd.setnamed("circle_25_"+str(i+2), "enabled", i!=start)
	fdtd.setnamed("circle_24_"+str(i+3), "enabled", i!=start)
	fdtd.setnamed("circle_23_"+str(i+3), "enabled", i!=start)
	fdtd.setnamed("circle_22_"+str(i+4), "enabled", i!=start)
	fdtd.setnamed("circle_21_"+str(i+4), "enabled", i!=start)
	fdtd.setnamed("circle_20_"+str(i+5), "enabled", i!=start)

fdtd.save('myNand.fsp')

"""
fdtd.run()
T1 = fdtd.getresult('monitor', 'T')
T1 = T1['T']
print(T1[0])"""