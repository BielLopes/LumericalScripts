import numpy as np
import matplotlib.pyplot as plt
import os
import imp

os.add_dll_directory('D:\\Lumarical\\v202\\api\\python')
lumapi = imp.load_source('lumapi', 'D:\\Lumarical\\v202\\api\\python\\lumapi.py')

fdtd = lumapi.FDTD()
  
Xsize = 22e-6
Ysize = 11e-6
Zsize = 0.22e-6

space = 10e-6

fdtd.addrect()
fdtd.set('x', space)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)
fdtd.set('z span', Zsize)
fdtd.set('index', 2.43);

fdtd.addfdtd()
fdtd.set('x', space)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)

fdtd.set('dimension', '2D')
fdtd.set('simulation time', 5000e-15)
fdtd.set('dt stability factor', 0.9)

#fdtd.set('layers', 16)
fdtd.set('mesh accuracy', 3)


fdtd.addindex()
fdtd.set('x', space)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)

fdtd.addprofile()
fdtd.set('x', space)
fdtd.set('x span', Xsize)
fdtd.set('y', 0.0)
fdtd.set('y span', Ysize)
fdtd.set('z', Zsize/2.0)
fdtd.set('output Px', True)
fdtd.set('output Py', True)
fdtd.set('output Pz', True)

fdtd.addpower()
fdtd.set('name', 'monitor_em pe')
fdtd.set('monitor type', 'Linear Y')
fdtd.set('x', 19.25e-6)
fdtd.set('y', 0.0)
fdtd.set('y span', 0.6e-6)
fdtd.set('z', Zsize/2.0)

fdtd.set('override global monitor settings', True)
fdtd.set('frequency points', 1000)

fdtd.set('output Px', True)
fdtd.set('output Py', True)
fdtd.set('output Pz', True)

fdtd.addmode()
fdtd.set('x', 0.0)
fdtd.set('y', 0.0)
fdtd.set('y span', 1.186e-6)
fdtd.set('z', Zsize/2.0)
fdtd.set('z span', 10.0e-6)
fdtd.set('number of trial modes', 20)
fdtd.set('center wavelength', 1.55e-6)
fdtd.set('wavelength span', 0.0)

####################################
###### CILINDERS GENERATION ########
####################################

z_span = 0.22e-6
index = 1.4
material = 'etch'
ny = 21
nx = 40
a = 0.5e-6
radius = 0.16e-6

n_rows = 2*round((ny-1)/2)
n_cols = nx
even_flag = 0

fdtd.addstructuregroup()
fdtd.set("name", "Cilinders Group")
fdtd.set("x", 0.0)
fdtd.set("y", 0.0)
fdtd.set("z", Zsize/2.0)
fdtd.groupscope("Cilinders Group")

for i in range(round(-n_rows/2), round(n_rows/2)):
  for j in range(1, n_cols):

    if i != 0:
      fdtd.addcircle()
      fdtd.set("radius",radius)    

      if even_flag == 0:
        fdtd.set("x",(j-1)*a + a/2)
      else:
        fdtd.set("x",(j-1)*a)

      fdtd.set("y",(i)*a*np.sqrt(3)/2)
      fdtd.set("z",0)
      fdtd.set("z span",z_span)
      fdtd.set("material",material)

      if fdtd.get("material") == "<Object defined dielectric>":
      	fdtd.set("index",index)

  if even_flag == 0:
    even_flag=1
  else:
    even_flag=0


fdtd.groupscope('::model');


fdtd.save('SiliconWaveGuide.fsp')
