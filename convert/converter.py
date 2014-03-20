# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 10:55:22 2014

@author: Администратор
"""

import netCDF4 as nc
from datetime import datetime, timedelta
import numpy as np

class NCPack:
    
    def __init__(self, path, format='NETCDF4', **kwargs):
        self.F = self.initNC(path, format, **kwargs)
        self.idx = 0
        self.dtformat = '%Y%m%d%H%M%S'
    
    def initNC(self,path, format, **kwargs):
        """
        Создает файл с необходимой структкрой данных
        Дата+Время
            - единицы измерения / начало отсчета
            - календарь
        Широта
            - единицы измерения    
        Долгота
            - единицы измерения
        Высота
            - единицы измерения
            - Диапазон
            
        Высота для средней атмосферы
            - единицы измерения
            - диапазон    
        Давление
            - единицы измерения    
        Температура
            - единицы измерения
        Плотность
            - единицы измерения
        Ошибка плотности
            - единицы измерения
        Высота тропопаузы
            - единицы измерения
        O3
            - единицы измерения
            - диапазон значения
            - диапазон высот
        NO2
            - единицы измерения
            - диапазон значения
            - диапазон высот
        H2O
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext386            
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext452
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext525
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext1020
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Density
            - единицы измерения
            - диапазон значения
            - диапазон высот
        площадная концентрация частиц
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Радиус частиц
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Плотность в средней атмосфере
            - единицы измерения
            - диапазон значения
            - диапазон высот
    
        O3_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        NO2_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        H2O_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext386_Err           
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext452_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext525_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Ext1020_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Density_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        площадная концентрация частиц_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Радиус частиц_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        Плотность в средней атмосфере_Err
            - единицы измерения
            - диапазон значения
            - диапазон высот
        InfVec
        """
        #Создаем файл
        F = nc.Dataset(path,'w', format)
        
        #определяем размерности
        F.createDimension('time',None)
        F.createDimension('L1',140)
        F.createDimension('L2',100)
        F.createDimension('L3',80)
        F.createDimension('L4',70)
        
        #Определяем переменные
        # Время
        var = F.createVariable('TP','f8',('time',), fill_value=-999.0, **kwargs)
        var.units = 'days since 1984-02-08'
        var.calendar= 'gregorian'
        
        # Широта
        var = F.createVariable('Lat','f4',('time',), fill_value=-999.0, **kwargs)
        var.units = 'Degrees North'
        var.range = [-90.0, 90.0]
        
        # Долгота
        var = F.createVariable('Lon','f4',('time',), fill_value=-999.0, **kwargs)
        var.units = 'Degrees East'
        var.range = [-180.0, 180.0]
        
        # NMC_Pres
        var = F.createVariable('NMC_Pres','f4',('time','L1',), fill_value=-999.0, **kwargs)
        var.units = 'mb'
        
        # NMC_Temp
        var = F.createVariable('NMC_Temp','f4',('time','L1',), fill_value=-999.0, **kwargs)
        var.units = 'K'
        
        # NMC_Dens
        var = F.createVariable('NMC_Dens','f4',('time','L1',), fill_value=-999.0, **kwargs)
        var.units = 'cm^-3'
        
        # NMC_Dens_Err
        var = F.createVariable('NMC_Dens_Err','i2',('time','L1',), fill_value=-999, **kwargs)
        var.units = '1000*%'
        
        # Trop_Height
        var = F.createVariable('Trop_Height','f4',('time',), fill_value=-999.0, **kwargs)
        var.units = 'km'
        
        # O3
        var = F.createVariable('O3','f4',('time','L1',), fill_value=-999.0, **kwargs)
        var.units = 'cm^-3'
        var.alt_range = [0.5, 70.0]
        var.description = 'O3 Density Profile'
        
        # NO2
        var = F.createVariable('NO2','f4',('time','L2',), fill_value=-999.0, **kwargs)
        var.units = 'cm^-3'
        var.alt_range = [0.5, 50.0]
        var.description = 'NO2 Density Profile'
        
        # H2O
        var = F.createVariable('H2O','f4',('time','L2',), fill_value=-999.0, **kwargs)
        var.units = 'ppp'
        var.alt_range = [0.5, 50.0]
        var.description = 'H2O Mixing Ratio Profile'
        
        # Ext386
        var = F.createVariable('Ext386','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = '1/km'
        var.alt_range = [0.5, 40.0]
        var.description = '386 nm Extinction'
        
        # Ext452
        var = F.createVariable('Ext452','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = '1/km'
        var.alt_range = [0.5, 40.0]
        var.description = '452 nm Extinction'
        
        # Ext525
        var = F.createVariable('Ext525','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = '1/km'
        var.alt_range = [0.5, 40.0]
        var.description = '525 nm Extinction'
        
        # Ext1020
        var = F.createVariable('Ext1020','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = '1/km'
        var.alt_range = [0.5, 40.0]
        var.description = '1020 nm Extinction'
        
        # Density
        var = F.createVariable('Density','f4',('time','L1',), fill_value=-999.0, **kwargs)
        var.units = 'cm^-3'
        var.alt_range = [0.5, 70.0]
        var.description = 'Calculated density'
        
        # SurfDen
        var = F.createVariable('SurfDen','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = 'um^2/cm^3'
        var.alt_range = [0.5, 40.0]
        var.description = 'Aerosol surface area density'
        
        # Radius
        var = F.createVariable('Radius','f4',('time','L3',), fill_value=-999.0, **kwargs)
        var.units = 'um'
        var.alt_range = [0.5, 40.0]
        var.description = 'Aerosol effective radius'
        
        # Dens_Mid_Atm
        var = F.createVariable('Dens_Mid_Atm','f4',('time','L4',), fill_value=-999.0, **kwargs)
        var.units = 'cm^-3'
        var.alt_range = [40.5, 75.0]
        var.description = 'Middle Atmosphere Density'
        
        # O3_Err
        var = F.createVariable('O3_Err','i2',('time','L1',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 70.0]
        var.description = 'O3 Density Profile Error'
        
        # NO2_Err
        var = F.createVariable('NO2_Err','i2',('time','L2',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 50.0]
        var.description = 'NO2 Density Profile Error'
        
        # H2O_Err
        var = F.createVariable('H2O_Err','i2',('time','L2',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 50.0]
        var.description = 'H2O Mixing Ratio Profile Error'
        
        # Ext386_Err
        var = F.createVariable('Ext386_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 40.0]
        var.description = '386 nm Extinction Error'
        
        # Ext452_err
        var = F.createVariable('Ext452_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 40.0]
        var.description = '452 nm Extinction Error'
        
        # Ext525_Err
        var = F.createVariable('Ext525_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 40.0]
        var.description = '525 nm Extinction Error'
        
        # Ext1020_Err
        var = F.createVariable('Ext1020_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '100*%'
        var.alt_range = [0.5, 40.0]
        var.description = '1020 nm Extinction Error'
        
        # Density_Err
        var = F.createVariable('Density_Err','i2',('time','L1',), fill_value=-999, **kwargs)
        var.units = '%*100'
        var.alt_range = [0.5, 70.0]
        var.description = 'Calculated density error'
        
        # SurfDen_Err
        var = F.createVariable('SurfDen_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '%*100'
        var.alt_range = [0.5, 40.0]
        var.description = 'Aerosol surface area density error'
        
        # Radius_Err
        var = F.createVariable('Radius_Err','i2',('time','L3',), fill_value=-999, **kwargs)
        var.units = '%*100'
        var.alt_range = [0.5, 40.0]
        var.description = 'Aerosol effective radius Error'
        
        # Dens_Mid_Atm_Err
        var = F.createVariable('Dens_Mid_Atm_Err','i2',('time','L4',), fill_value=-999, **kwargs)
        var.units = '%*100'
        var.alt_range = [40.5, 75.0]
        var.description = 'Middle Atmosphere Density Error'
        
        return F
        
    def close(self):
        self.F.close()
        
    def add(self, index, spec):
        """
        """
        
        vTP = self.F.variables['TP']
        
        Num_Prof = index['Num_Prof'][0]
        
        for i in range(0,Num_Prof):
            yyyy = np.floor(index['YYYYMMDD'][0][i]/10000.0)
            DayFrac = index['DayFrac'][0][i]
            
            # Формируем объект даты
            if (DayFrac==-999.0):
                TP = DayFrac
                
            else:
                TP = datetime(int(yyyy),1,1,0,0,0)+timedelta(days=DayFrac-1)
                TP = nc.date2num(TP, vTP.units, vTP.calendar)
                
            
            
            # ======= Запись в файл
            # Записываем время в файл
            vTP[i+self.idx] = TP
            
            self.F.variables['Lat'][i+self.idx] = index['Lat'][0][i]
            self.F.variables['Lon'][i+self.idx] = index['Lon'][0][i] 
            self.F.variables['NMC_Pres'][i+self.idx,:] = spec['NMC_Pres'][i,:]
            self.F.variables['NMC_Temp'][i+self.idx,:] = spec['NMC_Temp'][i,:]
            self.F.variables['NMC_Dens'][i+self.idx,:] = spec['NMC_Dens'][i,:]
            self.F.variables['NMC_Dens_Err'][i+self.idx,:] = spec['NMC_Dens_Err'][i,:]
            self.F.variables['Trop_Height'][i+self.idx] = spec['Trop_Height'][i]
            self.F.variables['O3'][i+self.idx,:] = spec['O3'][i,:]
            self.F.variables['NO2'][i+self.idx,:] = spec['NO2'][i,:]
            self.F.variables['H2O'][i+self.idx,:] = spec['H2O'][i,:]
            self.F.variables['Ext386'][i+self.idx,:] = spec['Ext386'][i,:]
            self.F.variables['Ext452'][i+self.idx,:] = spec['Ext452'][i,:]
            self.F.variables['Ext525'][i+self.idx,:] = spec['Ext525'][i,:]
            self.F.variables['Ext1020'][i+self.idx,:] = spec['Ext1020'][i,:]
            self.F.variables['Density'][i+self.idx,:] = spec['Density'][i,:]
            self.F.variables['SurfDen'][i+self.idx,:] = spec['SurfDen'][i,:]
            self.F.variables['Radius'][i+self.idx,:] = spec['Radius'][i,:]
            self.F.variables['Dens_Mid_Atm'][i+self.idx,:] = spec['Dens_Mid_Atm'][i,:]
            self.F.variables['O3_Err'][i+self.idx,:] = spec['O3_Err'][i,:]
            self.F.variables['NO2_Err'][i+self.idx,:] = spec['NO2_Err'][i,:]
            self.F.variables['H2O_Err'][i+self.idx,:] = spec['H2O_Err'][i,:]
            self.F.variables['Ext386_Err'][i+self.idx,:] = spec['Ext386_Err'][i,:]
            self.F.variables['Ext452_Err'][i+self.idx,:] = spec['Ext452_Err'][i,:]
            self.F.variables['Ext525_Err'][i+self.idx,:] = spec['Ext525_Err'][i,:]
            self.F.variables['Ext1020_Err'][i+self.idx,:] = spec['Ext1020_Err'][i,:]
            self.F.variables['Density_Err'][i+self.idx,:] = spec['Density_Err'][i,:]
            self.F.variables['SurfDen_Err'][i+self.idx,:] = spec['SurfDen_Err'][i,:]
            self.F.variables['Radius_Err'][i+self.idx,:] = spec['Radius_Err'][i,:]
            self.F.variables['Dens_Mid_Atm_Err'][i+self.idx,:] = spec['Dens_Mid_Atm_Err'][i,:]
            self.F.sync()
        self.idx+=Num_Prof
        print("Num_Prof = %d"%Num_Prof)