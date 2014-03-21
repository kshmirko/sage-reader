# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:35:29 2014

@author: Администратор
"""

from sage2.readsubs import readSage
from datetime import date
import pylab as plt
import numpy as np
from matplotlib.patches import Circle

Radius = 3 # degree
Lon0, Lat0 = 131.9, 43.1





index, spec=readSage('.',date(1984,11,1))



Lon = index['Lon']
Lat = index['Lat']
YMD = index['YYYYMMDD']

# find indices inside the region
Distance=np.sqrt((Lon-Lon0)**2+(Lat-Lat0)**2)
ok = Distance<Radius
print(YMD[ok])


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
circ = plt.Circle((Lon0,Lat0), radius=Radius, color='g', ls='solid', lw=2, fill=False)
ax.add_patch(circ)
ax.plot(Lon[ok],Lat[ok],'r.', mew=3)

plt.show()




