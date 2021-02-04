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

fdtd.save('SiliconWaveGuide.fsp')
