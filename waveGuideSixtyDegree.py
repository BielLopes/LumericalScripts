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
fdtd.set('index', 2.44);

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
fdtd.set('name', 'monitor_deitado')
fdtd.set('monitor type', 'Linear X')
fdtd.set('x', 8.75e-6)
fdtd.set('x span', 0.6e-6)
fdtd.set('y', 0.87e-6)
fdtd.set('z', Zsize/2.0)

fdtd.set('override global monitor settings', True)
fdtd.set('frequency points', 1000)

fdtd.set('output Px', True)
fdtd.set('output Py', True)
fdtd.set('output Pz', True)

fdtd.addpower()
fdtd.set('name', 'monitor_em pe')
fdtd.set('monitor type', 'Linear Y')
fdtd.set('x', 19.75e-6)
fdtd.set('y', 3.03e-6)
fdtd.set('y span', 0.6e-6)
fdtd.set('z', Zsize/2.0)

fdtd.set('override global monitor settings', True)
fdtd.set('frequency points', 1000)

fdtd.set('output Px', True)
fdtd.set('output Py', True)
fdtd.set('output Pz', True)

fdtd.addmode()
fdtd.set('x', 0.0)
fdtd.set('y', -1.725e-6)
fdtd.set('y span', 1.186e-6)
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
fdtd.set("x", 0.0)
fdtd.set("y", 0.0)
fdtd.set("z", Zsize/2.0)

z_span = 0.22e-6
index = 2.44
material = 'etch'
ny = 21
nx = 40
a = 0.5e-6
radius = 1.55e-7
bigRadius = 1.96e-7

n_rows = 2*round((ny-1)/2)
n_cols = nx
even_flag = 0

fdtd.set("construction group", True)
fdtd.set("Script", """
z_span = {z_span};
index = {index};
material = {material};
ny = {ny};
nx = {nx};
a = {a};
radius = {radius};
bigRadius = {bigRadius};

n_rows = {n_rows};
n_cols = {n_cols};
even_flag = 0;
new_even_flag = 1;

count1 = 1;
count2 = 1;

for(i=round(-n_rows/2):round(n_rows/2)) {
  for(j=1:n_cols) {
    if(i!=-4 & j<15){
      addcircle;
      if (i==-3 & j==14){
        set("name", 'a2');
      }   
      set("radius",radius);      
      if( even_flag==0 ) {
        set("x",(j-1)*a + a/2);        
      } else {
        set("x",(j-1)*a);
      }
      set("y",(i)*a*sqrt(3)/2);
      set("z",0);
      set("z span",z_span);
      set("material",material);
      if(get("material")=="<Object defined dielectric>")
  { set("index",index); } 
    } else if(j>=15 & j<21){
      if ( (new_even_flag==1 & i-j != (-4+count2)-(15+count1)) | (new_even_flag==0 & i-j != (-4+count2)-(15+count1)-1)){
        addcircle;
         if (i==-5 & j==15){
            set("name", 'a1');
        }
        if (i==-5 & j==16){
            set("name", 'q1');
        }
        if (i==-4 & j==16){
            set("name", 'b1');
        }
        if (i==-3 & j==15){
            set("name", 'q2');
        }
        if (i==-2 & j==15){
            set("name", 'b2');
        }    
        set("radius",radius);      
        if( even_flag==0 ) {
          set("x",(j-1)*a + a/2);        
        } else {
          set("x",(j-1)*a);
        }
        set("y",(i)*a*sqrt(3)/2);
        set("z",0);
        set("z span",z_span);
        set("material",material);
        if(get("material")=="<Object defined dielectric>")
    { set("index",index); }         
      } else {
          if(new_even_flag==1) {
            new_even_flag=0;
            count2 = count2 + 1;
          } else {
            new_even_flag=1;
            count1 = count1 + 1;
            count2 = count2 + 1;
          }
      }
    } else if(j>=21 & i!=7){
      addcircle;    
      set("radius",radius);      
      if( even_flag==0 ) {
        set("x",(j-1)*a + a/2);        
      } else {
        set("x",(j-1)*a);
      }
      set("y",(i)*a*sqrt(3)/2);
      set("z",0);
      set("z span",z_span);
      set("material",material);
      if(get("material")=="<Object defined dielectric>")
        { set("index",index); } 
    }
  }
  if(even_flag==0) {
    even_flag=1;
  } else {
    even_flag=0;
  }
}

#setnamed("q1", "radius", bigRadius);

#select("q2");
#delete;
#setnamed("a2", "radius", bigRadius);
#setnamed("b2", "radius", bigRadius);

""".replace('{z_span}', str(z_span))
	 .replace('{index}', str(index))
	 .replace('{material}', '\''+material+'\'')
	 .replace('{ny}', str(ny))
	 .replace('{nx}', str(nx))
	 .replace('{a}', str(a))
   .replace('{radius}', str(radius))
	 .replace('{bigRadius}', str(bigRadius))
	 .replace('{n_rows}', str(n_rows))
	 .replace('{n_cols}', str(n_cols))

)

fdtd.save('SiliconSixtyDegreeTest.fsp')
fdtd.run()

T1 = fdtd.getresult('monitor_deitado', 'T')
T2 = fdtd.getresult('monitor_em pe', 'T')

print(T1['T'])
print(T2['T'])
