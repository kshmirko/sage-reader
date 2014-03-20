# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:16:45 2014

@author: Администратор
"""

from sage2.readsubs import readSageZip
from datetime import date

from convert.converter import NCPack

PATH=r"d:\disks\1TB\#data#\#SAT#\OZONE\SAGE_II"
#Radius = 4 # degree
#Lon0, Lat0 = 131.9, 43.1
SINGLE=True

if SINGLE:
    P = NCPack('SAGE-II-6.20.nc', 'NETCDF_CLASSIC', zlib=True, complevel=7)
    
    for year in range(1984,2006):
        for month in range(1,13):
            index, spec = readSageZip(PATH, date(year,month,1))

            # если вернулись None и None - файла не существует
            if (not (index is None)) and (not (spec is None)):
                print('Processing %04d-%02d...'%(year,month))
                P.add(index,spec)

    P.close()

else:
    for year in range(1984,2006):
        for month in range(1,13):
            index, spec = readSageZip(PATH, date(year,month,1))
    
            # если вернулись None и None - файла не существует
            if (not (index is None)) and (not (spec is None)):
                print('Processing %04d-%02d...'%(year,month))

                P = NCPack('SAGE-II_%04d-%02d.nc'%(year,month), 'NETCDF4_CLASSIC', zlib=True, complevel=7)
                P.add(index,spec)
                P.close()
    
