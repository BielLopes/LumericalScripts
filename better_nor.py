import numpy as np
import matplotlib.pyplot as plt
from setupWaveGuide.setups import setupA, setupB, setupUpperRadius
import os
import imp

os.add_dll_directory('C:\\Program Files\\Lumerical\\v202\\api\\python')
os.environ['PATH'] = 'C:\\Program Files\\Lumerical\\v202\\api\\python' + os.pathsep + os.environ['PATH']
lumapi = imp.load_source('lumapi', 'C:\\Program Files\\Lumerical\\v202\\api\\python\\lumapi.py')

fdtd = lumapi.FDTD()
  
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
fdtd.set('simulation time', 5000e-15)
fdtd.set('dt stability factor', 0.9)

#fdtd.set('layers', 16)
fdtd.set('mesh accuracy', 3)

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
	fdtd.set('amplitude', 1)	
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

fdtd.save('betterNor.fsp')

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
setupB(fdtd)

fdtd.save('betterNor.fsp')

fdtd.switchtolayout()
fdtd.groupscope('::model')
fdtd.groupscope("Cilinders Group")

solution = [214.97621649685348, 100.80651260056283, 161.12679122422543, 89.44894115940613, 0.534205081529767, 7.0]

setupA(fdtd, solution[5])

fdtd.setnamed('circle_17_18', 'radius', 1e-9*solution[0])
fdtd.setnamed('circle_17_19', 'radius', 1e-9*solution[1])
fdtd.setnamed('circle_17_17', 'radius', 1e-9*solution[2])

setupUpperRadius(fdtd, solution)

fdtd.setnamed('circle_18_17', 'radius', 1e-9*solution[3])

fdtd.groupscope('::model')
fdtd.setnamed('source S', 'amplitude', solution[4])

fdtd.setnamed('source A', 'enabled', True);
fdtd.setnamed('source B', 'enabled', True);

fdtd.save('betterNor.fsp')
