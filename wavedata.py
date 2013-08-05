# -*- coding:utf-8 -*-
"""
Created on Aug 4, 2013

@author: Dima
"""

from wavemeter import wavemeter, GetFuncError, SetFuncError
import time
import threading

w = wavemeter()

class ChannelData(object):
    def __init__(self, channel):
        self.channel    = channel
        self.wavelength = 0.0
        self.exposure   = 0
        self.exposure2  = 0
        self.error      = 0
        self.error_msg  = "No signal"
        self.hasdata    = False
        self.geterr     = GetFuncError(0) # We are interested in the message text onlt
    
    # Prints data for a web page
    def writeData(self, file):
        if (self.hasdata):
            message = str(self.channel) + ", " + str(self.wavelength) + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
        else:
            message = str(self.channel) + ", " + self.error_msg + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
       
        file.write(message)
            
        
        
    def setWavelength(self, wavelength):
        if (wavelength > 0):
            self.wavelength = wavelength
            self.oktime     = time.time()
            self.hasdata    = True
        else:
            self.error     = wavelength
            self.error_msg = self.geterr.message(wavelength)
            if (self.hasdata):
                self.errtime   = time.time()
                self.hasdata   = False
 
        
    def setExposure(self, exposure, exposure2):
        self.exposure  = exposure
        self.exposure2 = exposure2

    def setExposure1(self, exposure):
        self.exposure  = exposure

    def setExposure2(self, exposure):
        self.exposure2  = exposure
     
    def setError(self, errno, errmsg):
        self.error     = errno
        self.error_msg = errmsg  
        if (self.hasdata):
            self.errtime   = time.time()
            self.hasdata   = False
            
    def readWavelength(self):
        try:
            wavelength = w.GetWavelengthNum(self.channel)
            self.setWavelength(wavelength)
        except GetFuncError as e:
            self.setError(e.value, e.msg)

    def readExposure(self):
        try:
            exp1 = w.GetExposureNum(self.channel, 1)
            exp2 = w.GetExposureNum(self.channel, 2)
            self.setExposure(exp1, exp2)
        except GetFuncError as e:
            self.setError(e.value, e.msg)


class WavemeterData(threading.Thread):
    ''' Class to collect and store recent wavemeter data '''
    nchannels = 8
    
    def __init__(self):
        threading.Thread.__init__(self)

        self.ch = {}       
        for i in range(1, self.nchannels+1):
            self.ch[i] = ChannelData(i)
 
        # Ask for callback function and wait for data
        self.InstantiateWaitFunc()
            
    def __del__(self):
        w.Instantiate(w.df.cInstNotification, w.df.cNotifyRemoveWaitEvent, 0, 0)
    
    def run(self):
        self.WaitForData()
    
    def writeData(self, file):
        for i in range(1, self.nchannels+1):
            self.ch[i].writeData(file)
            
    def InstantiateWaitFunc(self):
        # Ask wavemeter to call WaitForWLMEvent whenever new data are ready
        res = w.Instantiate(w.df.cInstNotification, w.df.cNotifyInstallWaitEvent, -1, 0)
        print "Instantiate = ", res
        
    # Main function: gets data in a loop and updates  
    def WaitForData(self):
        while(True):
            # Wait for the new data forever
            (ret, mode, IntVal, DblVal) = w.WaitForWLMEvent()
            
            # No wavemeter, return 
            if (ret == 0):
                return
            elif (ret == -2):
                print "Unknown event or error\n"
            
            # Long switch - case to process the data
            # Wavelength
            if(mode == w.df.cmiWavelength1): 
                self.ch[1].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength2):
                self.ch[2].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength3):
                self.ch[3].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength4):
                self.ch[4].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength5):
                self.ch[5].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength6):
                self.ch[6].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength7):
                self.ch[7].setWavelength(DblVal)
            elif (mode == w.df.cmiWavelength8):
                self.ch[8].setWavelength(DblVal)
            # Exposure values, CCD 1
            elif (mode == w.df.cmiExposureValue11):
                self.ch[1].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue12):
                self.ch[2].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue13):
                self.ch[3].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue14):
                self.ch[4].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue15):
                self.ch[5].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue16):
                self.ch[6].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue17):
                self.ch[7].setExposure1(IntVal)
            elif (mode == w.df.cmiExposureValue18):
                self.ch[8].setExposure1(IntVal)
            # Exposure values, CCD 2
            elif (mode == w.df.cmiExposureValue21):
                self.ch[1].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue22):
                self.ch[2].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue23):
                self.ch[3].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue24):
                self.ch[4].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue25):
                self.ch[5].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue26):
                self.ch[6].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue27):
                self.ch[7].setExposure2(IntVal)
            elif (mode == w.df.cmiExposureValue28):
                self.ch[8].setExposure2(IntVal)
                

        
        