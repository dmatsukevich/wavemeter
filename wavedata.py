# -*- coding:utf-8 -*-
"""
Created on Aug 4, 2013

@author: Dima
"""

from wavemeter import wavemeter
from time import time

class ChannelData(object):
    def __init__(self, channel):
        self.channel    = channel
        self.wavelength = 0.0
        self.exposure   = 0
        self.exposure2  = 0
        self.error      = 0
        self.error_msg  = "No data"
        self.hasdata    = False
    
    def writeData(self, file):
        if (self.hasdata):
            message = str(self.channel) + ", " + str(self.wavelength) + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
        else:
            message = str(self.channel) + ", " + self.error_msg + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
       
        file.write(message)
            
        
        
    def setWavelength(self, wavelength):
        self.wavelength = wavelength
        self.oktime     = time.time()
        self.hasdata    = True
        
    def setExposure(self, exposure, exposure2):
        self.exposure  = exposure
        self.exposure2 = exposure2
        self.oktime    = time.time()
        self.hasdata   = True
     
    def setError(self, errno, errmsg):
        self.error     = errno
        self.error_msg = errmsg  
        if (self.hasdata):
            self.errtime   = time.time()
            self.hasdata   = False
            

class WavemeterData(object):
    
    nchannels = 8
    
    ''' Class to collect and store recent wavemeter data '''
    def __init__(self):
        self.wm = wavemeter()
        self.ch = {}       
        for i in range(1, self.nchannels+1):
            self.ch[i] = ChannelData(i)  
    
    def writeData(self, file):
        for i in range(1, self.nchannels+1):
            self.ch[i].writeData(file)
