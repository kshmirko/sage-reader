# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:43:18 2014

@author: Dr. Konstantin A. Shmirko

"""
import numpy as np
from datetime import datetime
import os
import zipfile as zf
from sage2.sageIItypes import _INDEX, _SPECITEM


def _readIndex(fname):
    ret = np.fromfile(fname,dtype=_INDEX)
    return ret

def _readIndex1(fname):
    ret = np.frombuffer(fname,dtype=_INDEX)
    return ret

def _readSpecItem(fname):
    ret = np.fromfile(fname,dtype=_SPECITEM)
    return ret

def _readSpecItem1(fname):
    ret = np.frombuffer(fname,dtype=_SPECITEM)
    return ret

def readSage(path,date,suffx='.6.20'):
    """
        suffx = '.6.20' | '.7.00'
    """
    indexstr = 'SAGE_II_INDEX_'+datetime.strftime(date,'%Y%m')+suffx
    indexpath = os.path.join(path,indexstr)
    index = _readIndex(indexpath)
    specstr = index['Spec_File_Name'][0].strip().decode('ascii')
    print(specstr)
    specpath = os.path.join(path,specstr)
    spec = _readSpecItem(specpath)

    return index, spec


def readSageZip(path,date):
    datestr = datetime.strftime(date,'%Y%m')
    zipfilestr = 'sage2_v6.20_'+datestr+'.zip'


    zipfilename = os.path.join(path, zipfilestr)
    if os.path.exists(zipfilename):

        with zf.ZipFile(zipfilename,'r') as f:
            indexstr = 'SAGE_II_INDEX_'+datestr+'.6.20'
            indexbuffer = f.read(indexstr)
            index = _readIndex1(indexbuffer)
            specstr = index['Spec_File_Name'][0].strip().decode('ascii')
            specbuffer = f.read(specstr)
            spec = _readSpecItem1(specbuffer)
        return index, spec

    return None,None



