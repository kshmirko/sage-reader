sage-reader
===========

Provides several routines for reading SAGE II experiment data and a routine for saving data into netcdf4 format.
The main purpose of this code - is to provide easy access to SAGE II experiment data. Initially, SAGE II binary 
format is hard to support and it didn't save information about metadata.

SAGE II experiment data is stored in two separate files: index file ans spectra file. Below their structute is 
provided. 

Element size of FLTARR is 4
                INTARR is 2
                LONARR is 4



    PRO sg2_indexinfo, data

    data = {num_prof:           0L,            $ ; Number of profiles in these files
        ; Revision Info
        Met_Rev_Date:       0L,            $ ; LaRC Met Model Revision Date (YYYYMMDD)
        Driver_Rev:         BYTARR(8),     $ ; LaRC Driver Version (e.g. 6.20)
        Trans_Rev:          BYTARR(8),     $ ; LaRC Transmission Version
        Inv_Rev:            BYTARR(8),     $ ; LaRC Inversion Version
        Spec_Rev:           BYTARR(8),     $ ; LaRC Inversion Version
        Eph_File_Name:      BYTARR(32),    $ ; Ephemeris data file name
        Met_File_Name:      BYTARR(32),    $ ; Meteorological data file name
        Ref_File_Name:      BYTARR(32),    $ ; Refraction data file name
        Tran_File_Name:     BYTARR(32),    $ ; Transmission data file name
        Spec_File_Name:     BYTARR(32),    $ ; Species profile file name
        FillVal:            0.0E0,         $ ; Fill value

        ; Altitude grid and range info
        Grid_Size:          0.0E0,         $ ; Altitude grid spacing (0.5 km)
        Alt_Grid:           FLTARR(200),   $ ; Geometric altitudes (0.5,1.0,...,100.0 km)
        Alt_Mid_Atm:        FLTARR(70),    $ ; Middle atmosphere geometric altitudes
        Range_Trans:        FLTARR(2),     $ ; Transmission min & max altitudes       [0.5,100.]
        Range_O3:           FLTARR(2),     $ ; Ozone min & max altitudes              [0.5,70.0]
        Range_NO2:          FLTARR(2),     $ ; NO2 min & max altitudes                [0.5,50.0]
        Range_H2O:          FLTARR(2),     $ ; Water vapor min & max altitudes        [0.5,50.0]
        Range_Ext:          FLTARR(2),     $ ; Aerosol extinction min & max altitudes [0.5,40.0]
        Range_Dens:         FLTARR(2),     $ ; Density min & max altitudes            [0.5,70.0]
        Spare:              FLTARR(2),     $ ; 

        ; Event specific info useful for data subsetting
        YYYYMMDD:           LONARR(930),   $ ; Event date at 20 km subtangent point
        Event_Num:          LONARR(930),   $ ; Event number
        HHMMSS:             LONARR(930),   $ ; Event time at 20 km
        Day_Frac:           FLTARR(930),   $ ; Time of year (DDD.frac) at 20 km
        Lat:                FLTARR(930),   $ ; Subtangent latitude  at 20 km (-90,+90)
        Lon:                FLTARR(930),   $ ; Subtangent longitude at 20 km (-180,+180)
        Beta:               FLTARR(930),   $ ; Spacecraft beta angle (deg)
        Duration:           FLTARR(930),   $ ; Duration of event (sec)
        Type_Sat:           INTARR(930),   $ ; Event Type: Instrument (0=SR, 1=SS)
        Type_Tan:           INTARR(930),   $ ; Event Type: Local      (0=SR, 1=SS)

        ; Process tracking and flag info
        Dropped:            LONARR(930),   $ ; Dropped event flag
        InfVec:             LONARR(930),   $ ; Bit flags relating to processing

        ; Record creation dates and times
        Eph_Cre_Date:       LONARR(930),   $ ; Record creation date (YYYYMMDD format)
        Eph_Cre_Time:       LONARR(930),   $ ; Record creation time (HHMMSS format)
        Met_Cre_Date:       LONARR(930),   $ ; Record creation date (YYYYMMDD format)
        Met_Cre_Time:       LONARR(930),   $ ; Record creation time (HHMMSS format)
        Ref_Cre_Date:       LONARR(930),   $ ; Record creation date (YYYYMMDD format)
        Ref_Cre_Time:       LONARR(930),   $ ; Record creation time (HHMMSS format)
        Tran_Cre_Date:      LONARR(930),   $ ; Record creation date (YYYYMMDD format)
        Tran_Cre_Time:      LONARR(930),   $ ; Record creation time (HHMMSS format)
        Spec_Cre_Date:      LONARR(930),   $ ; Record creation date (YYYYMMDD format)
        Spec_Cre_Time:      LONARR(930)    } ; Record creation time (HHMMSS format)

    END


    PRO sg2_specinfo, data

    data = {Tan_Alt:              FLTARR(8),     $ ; Subtangent Altitudes (km)
        Tan_Lat:              FLTARR(8),     $ ; Subtangent Latitudes  @ Tan_Alt (deg)
        Tan_Lon:              FLTARR(8),     $ ; Subtangent Longitudes @ Tan_Alt (deg)
        NMC_Pres:             FLTARR(140),   $ ; Gridded Pressure profile (mb)
        NMC_Temp:             FLTARR(140),   $ ; Gridded Temperature profile (K)
        NMC_Dens:             FLTARR(140),   $ ; Gridded Density profile (cm^(-3))
        NMC_Dens_Err:         INTARR(140),   $ ; Error in NMC_Dens (%*1000)
        Trop_Height:          0.0E0,         $ ; NMC Tropopause Height (km)
        Wavelength:           FLTARR(7),     $ ; Wavelength of each channel (nm)
        O3:                   FLTARR(140),   $ ; O3  Density profile 0-70Km (cm^(-3))
        NO2:                  FLTARR(100),   $ ; NO2 Density profile 0-50Km (cm^(-3))
        H2O:                  FLTARR(100),   $ ; H2O Volume Mixing Ratio 0-50Km (ppp)
        Ext386:               FLTARR(80),    $ ; 386 nm Extinction   0-40Km (1/km)
        Ext452:               FLTARR(80),    $ ; 452 nm Extinction   0-40Km (1/km)
        Ext525:               FLTARR(80),    $ ; 525 nm Extinction   0-40Km (1/km)
        Ext1020:              FLTARR(80),    $ ; 1020nm Extinction   0-40Km (1/km)
        Density:              FLTARR(140),   $ ; Calculated Density  0-70Km (cm^(-3))
        SurfDen:              FLTARR(80),    $ ; Aerosol surface area dens 0-40km (um^2/cm^3)
        Radius:               FLTARR(80),    $ ; Aerosol effective radius 0-40km (um)
        Dens_Mid_Atm:         FLTARR(70),    $ ; Middle Atmosphere Density (cm^(-3))
        O3_Err:               INTARR(140),   $ ; Error in  O3 density profile (%*100)
        NO2_Err:              INTARR(100),   $ ; Error in NO2 density profile (%*100)
        H2O_Err:              INTARR(100),   $ ; Error in H2O mixing ratio (%*100)
        Ext386_Err:           INTARR(80),    $ ; Error in  386nm Extinction (%*100)
        Ext452_Err:           INTARR(80),    $ ; Error in  452nm Extinction (%*100)
        Ext525_Err:           INTARR(80),    $ ; Error in  525nm Extinction (%*100)
        Ext1020_Err:          INTARR(80),    $ ; Error in 1019nm Extinction (%*100)
        Density_Err:          INTARR(140),   $ ; Error in Density (%*100)
        SurfDen_Err:          INTARR(80),    $ ; Error in surface area dens (%*100)
        Radius_Err:           INTARR(80),    $ ; Error in aerosol radius (%*100)
        Dens_Mid_Atm_Err:     INTARR(70),    $ ; Error in Middle Atm. Density (%*100)
        InfVec:               INTARR(140)    } ; Informational Bit flags

    END
