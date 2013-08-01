'''
Created on Jul 30, 2013

@author: cqt
'''
from ctypes import *

class wavemeter_defs(object):
    # for instantiate function
    cInstCheckForWLM = -1
    cInstResetCalc = 0
    cInstReturnMode = cInstResetCalc
    cInstNotification = 1
    cInstCopyPattern = 2
    cInstCopyAnalysis = cInstCopyPattern
    cInstControlWLM = 3
    cInstControlDelay = 4
    cInstControlPriority = 5

    # Notification Constants for 'Mode' parameter
    cNotifyInstallCallback = 0
    cNotifyRemoveCallback = 1
    cNotifyInstallWaitEvent = 2
    cNotifyRemoveWaitEvent = 3
    cNotifyInstallCallbackEx = 4
    cNotifyInstallWaitEventEx = 5


    # enum for units
    cReturnWavelengthVac = 0;
    cReturnWavelengthAir = 1;
    cReturnFrequency = 2;
    cReturnWavenumber = 3;
    cReturnPhotonEnergy = 4;


class wavemeter(object):
    def __init__(self):
#        self.wm = CDLL("C:\Windows\System32\wlmData.dll")
        self.wm = WinDLL("C:\Windows\System32\wlmData.dll")
        self.df = wavemeter_defs()

    def GetWavelengthNum(self, ch):
        # double GetWavelengthNum(long num, double WL);
        f = self.wm.GetWavelengthNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        return res

    def GetFrequencyNum(self, ch):
        # double GetFrequencyNum(long num, double WL);
        f = self.wm.GetFrequencyNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        return res

    def GetChannelsCount(self):
        f = self.wm.GetChannelsCount
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(0))
        return res

    def GetTemperature(self):
        f = self.wm.GetTemperature
        f.restype = c_double
        f.argtypes = [c_double]
        res = f(c_double(0.0))
        return res

    def GetPressure(self):
        f = self.wm.GetPressure
        f.restype = c_double
        f.argtypes = [c_double]
        res = f(c_double(0.0))
        return res
        
    def SetSwitcherSignalStates(self, signal, use, show):
        f = self.wm.SetSwitcherSignalStates
        f.restype = c_long
        f.argtypes = [c_long, c_long, c_long]
        res = f(c_long(signal), c_long(use), c_long(show) )
        return res
        
    def GetSwitcherSignalStates(self, signal):
        f = self.wm.GetSwitcherSignalStates
        f.restype = c_long
        f.argtypes = [c_long, POINTER(c_long), POINTER(c_long)]
        use  = c_long(0)
        show = c_long(0)
        res = f(c_long(signal), byref(use), byref(show) )
        return res, use.value, show.value
        
    def Instantiate(self, RFC, mode, P1, P2):
        f = self.wm.Instantiate
        f.restype = c_long
        f.argtypes = [c_long, c_long, c_long, c_long]
        res = f(c_long(RFC), c_long(mode), c_long(P1), c_long(P2) )
        return res
    
    def GetWLMVersion(self, ver):
        f = self.wm.GetWLMVersion
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(ver))
        return res
         
    def GetSwitcherMode(self):
        f = self.wm.GetSwitcherMode
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(0))
        return res        

    def SetSwitcherMode(self, mode):
        f = self.wm.SetSwitcherMode
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(mode))
        return res        
       
    def ConvertUnit(self, val, uFrom, uTo):
        f = self.wm.ConvertUnit
        f.restype = c_double
        f.argtypes = [c_double, c_long, c_long]
        res = f(c_double(val), c_long(uFrom), c_long(uTo))
        return res        
    
    
# execute this if we started this file
if __name__ == "__main__":
    w = wavemeter()
    print w.GetWavelengthNum(0)
    print w.GetFrequencyNum(0)
    print w.GetChannelsCount()
    print w.GetTemperature()
    print w.GetPressure()
    print w.GetSwitcherSignalStates(0)
    print w.Instantiate(w.df.cInstCheckForWLM, 0, 0, 0)
    print w.GetWLMVersion(0)
    print w.GetSwitcherMode()
    print w.ConvertUnit(369.0, w.df.cReturnWavelengthVac, w.df.cReturnFrequency)
    print w.ConvertUnit(935.0, w.df.cReturnWavelengthVac, w.df.cReturnFrequency)
#    print w.SetSwitcherSignalStates(0, 1, 1)
    
    