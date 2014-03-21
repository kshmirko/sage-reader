# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:43:18 2014

@author: Dr. Konstantin A. Shmirko
"""
import numpy as np

_INDEX = [
#; Revision Info 
    ('Num_Prof', 'i4'),             #; Number of profiles in these files 
    ('Met_Rev_Date','i4'),          #; LaRC Met Model Revision Date (YYYYMMDD) 
    ('Driver_Rev','a8'),            #; LaRC Driver Version (e.g. 6.20)
    ('Transmission_Rev','a8'),      #; LaRC Transmission Version 
    ('Inversion_Rev','a8'),         #; LaRC Inversion Version 
    ('Spectroscopy_Rev','a8'),      #; LaRC Inversion Version 
    ('Eph_File_Name','a32'),        #; Ephemeris data file name 
    ('Met_File_Name','a32'),        #; Meteorological data file name 
    ('Ref_File_Name','a32'),        #; Refraction data file name
    ('Trans_File_Name','a32'),      #; Transmission data file name 
    ('Spec_File_Name','a32'),       #; Species profile file name 
    ('FillValue','f4'),             #; Fill value

#; Altitude grid and range info 
    ('GridSize','f4'),              #; Altitude grid spacing (0.5 km) 
    ('AltGrid', ('f4',200)),        #; Geometric altitudes (0.5,1.0,...,100.0 km) 
    ('AltMidAtm',('f4',70)),        #; Middle atmosphere geometric altitudes 
    ('Range_Trans',('f4',2)),       #; Transmission min & max altitudes       [0.5,100.] 
    ('Range_O3',('f4',2)),          #; Ozone min & max altitudes              [0.5,70.0] 
    ('Range_NO2',('f4',2)),         #; NO2 min & max altitudes                [0.5,50.0] 
    ('Range_N2O',('f4',2)),         #; Water vapor min & max altitudes        [0.5,50.0]    
    ('Range_Ext',('f4',2)),         #; Aerosol extinction min & max altitudes [0.5,40.0] 
    ('Range_Density',('f4',2)),     #; Density min & max altitudes            [0.5,70.0] 
    ('Range_Surface',('f4',2)),


#; Event specific info useful for data subsetting
    ('YYYYMMDD',('i4',930)),        #; Event date at 20 km subtangent point 
    ('Event_Num',('i4',930)),       #; Event number 
    ('HHMMSS',('i4',930)),          #; Event time at 20 km 
    ('DayFrac',('f4',930)),         #; Time of year (DDD.frac) at 20 km 
    ('Lat',('f4',930)),             #; Subtangent latitude  at 20 km (-90,+90) 
    ('Lon',('f4',930)),             #; Subtangent longitude at 20 km (-180,+180)
    ('Beta',('f4',930)),            #; Spacecraft beta angle (deg) 
    ('Duration',('f4',930)),        #; Duration of event (sec) 
    ('Type_Sat',('i2',930)),        #; Event Type: Instrument (0=SR, 1=SS) 
    ('Type_Tan',('i2',930)),        #; Event Type: Local      (0=SR, 1=SS) 

#; Process tracking and flag info     
    ('Dropped',('i4',930)),         #; Dropped event flag 
    ('InfVec',('i4',930)),          #; Bit flags relating to processing 

#; Record creation dates and times 
    ('Eph_Cre_Date',('i4',930)),    #; Record creation date (YYYYMMDD format) 
    ('Eph_Cre_Time',('i4',930)),    #; Record creation time (HHMMSS format) 
    ('Met_Cre_Date',('i4',930)),    #; Record creation date (YYYYMMDD format) 
    ('Met_Cre_Time',('i4',930)),    #; Record creation time (HHMMSS format) 
    ('Ref_Cre_Date',('i4',930)),    #; Record creation date (YYYYMMDD format) 
    ('Ref_Cre_Time',('i4',930)),    #; Record creation time (HHMMSS format) 
    ('Trans_Cre_Date',('i4',930)),  #; Record creation date (YYYYMMDD format) 
    ('Trans_Cre_Time',('i4',930)),  #; Record creation time (HHMMSS format) 
    ('Species_Cre_Date',('i4',930)),#; Record creation date (YYYYMMDD format) 
    ('Species_Cre_Time',('i4',930)),#; Record creation time (HHMMSS format) 
]


_SPECITEM = [
    ('Tan_Alt', ('f4',8)),          #; Subtangent Altitudes (km) 
    ('Tan_Lat', ('f4',8)),          #; Subtangent Latitudes  @ Tan_Alt (deg) 
    ('Tan_Lon', ('f4',8)),          #; Subtangent Longitudes @ Tan_Alt (deg) 
    
    ('NMC_Pres', ('f4',140)),       #Gridded Pressure profile (mb) 
    ('NMC_Temp', ('f4',140)),       #Gridded Temperature profile (K) 
    ('NMC_Dens', ('f4',140)),       #Gridded Density profile (cm^(-3)) 
    ('NMC_Dens_Err', ('i2',140)),   #Error in NMC_Dens (%*1000) 
    ('Trop_Height', 'f4'),          #NMC Tropopause Height (km) 

    ('Wavelength', ('f4',7)),       #Wavelength of each channel (nm) 

    ('O3', ('f4',140)),             #O3  Density profile 0-70Km (cm^(-3)) 
    ('NO2', ('f4',100)),            #NO2 Density profile 0-50Km (cm^(-3)) 
    ('H2O', ('f4',100)),            #H2O Volume Mixing Ratio 0-50Km (ppp) 

    ('Ext386', ('f4',80)),          #386 nm Extinction   0-40Km (1/km)
    ('Ext452', ('f4',80)),          #452 nm Extinction   0-40Km (1/km)
    ('Ext525', ('f4',80)),          #525 nm Extinction   0-40Km (1/km) 
    ('Ext1020', ('f4',80)),         #1020nm Extinction   0-40Km (1/km) 

    ('Density', ('f4',140)),        #Calculated Density  0-70Km (cm^(-3))
    ('SurfDen', ('f4',80)),          #Aerosol surface area dens 0-40km (um^2/cm^3) 
    ('Radius', ('f4',80)),          #Aerosol effective radius 0-40km (um)
    ('Dens_Mid_Atm', ('f4',70)),    #Middle Atmosphere Density (cm^(-3)) 

    ('O3_Err', ('i2',140)),         #Error in  O3 density profile (%*100)
    ('NO2_Err', ('i2',100)),        #Error in NO2 density profile (%*100) 
    ('H2O_Err', ('i2',100)),        #Error in H2O mixing ratio (%*100)

    ('Ext386_Err', ('i2',80)),      #Error in  386nm Extinction (%*100)
    ('Ext452_Err', ('i2',80)),      #Error in  452nm Extinction (%*100) 
    ('Ext525_Err', ('i2',80)),      #Error in  525nm Extinction (%*100) 
    ('Ext1020_Err', ('i2',80)),     #Error in 1019nm Extinction (%*100)

    ('Density_Err', ('i2',140)),    #Error in Density (%*100) 
    ('SurfDen_Err', ('i2',80)),      #Error in surface area dens (%*100) 
    ('Radius_Err', ('i2',80)),      #Error in aerosol radius (%*100) 
    ('Dens_Mid_Atm_Err', ('i2',70)),#Error in Middle Atm. Density (%*100) 
    
    ('InfVec', ('i2',140))          #Informational Bit flags 
    
]

