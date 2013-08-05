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

    # enum for Set ... functions
    ResERR_NoErr = 0
    ResERR_WlmMissing = -1
    ResERR_CouldNotSet = -2
    ResERR_ParmOutOfRange = -3
    ResERR_WlmOutOfResources = -4
    ResERR_WlmInternalError = -5
    ResERR_NotAvailable = -6
    ResERR_WlmBusy = -7
    ResERR_NotInMeasurementMode = -8
    ResERR_OnlyInMeasurementMode = -9
    ResERR_ChannelNotAvailable = -10
    ResERR_ChannelTemporarilyNotAvailable = -11
    ResERR_CalOptionNotAvailable = -12
    ResERR_CalWavelengthOutOfRange = -13
    ResERR_BadCalibrationSignal = -14
    ResERR_UnitNotAvailable = -15
    ResERR_FileNotFound = -16
    ResERR_FileCreation = -17
    ResERR_TriggerPending = -18
    ResERR_TriggerWaiting = -19

    # enum for Get ... functions
    ErrNoValue = 0;
    ErrNoSignal = -1;
    ErrBadSignal = -2;
    ErrLowSignal = -3;
    ErrBigSignal = -4;
    ErrWlmMissing = -5;
    ErrNotAvailable = -6;
    InfNothingChanged = -7;
    ErrNoPulse = -8;
    ErrDiv0 = -13;
    ErrOutOfRange = -14;
    ErrUnitNotAvailable = -15;
    ErrMaxErr = ErrUnitNotAvailable;

    # Return errorvalues of GetTemperature and GetPressure
    ErrTemperature = -1000;
    ErrTempNotMeasured = ErrTemperature + ErrNoValue;
    ErrTempNotAvailable = ErrTemperature + ErrNotAvailable;
    ErrTempWlmMissing = ErrTemperature + ErrWlmMissing;

    # Return errorvalues of GetDistance
    # real errorvalues are ErrDistance combined with those of GetWavelength
    ErrDistance = -1000000000;
    ErrDistanceNotAvailable = ErrDistance + ErrNotAvailable;
    ErrDistanceWlmMissing = ErrDistance + ErrWlmMissing;


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class SetFuncError(Error):
    def __init__(self, value):
        self.value = value
        self.msg = self.message(value)

    def message(self, value):
        return {
        wavemeter_defs.ResERR_NoErr: "No Error",
        wavemeter_defs.ResERR_WlmMissing: "Wavemeter is missing",
        wavemeter_defs.ResERR_CouldNotSet: "Could not set",
        wavemeter_defs.ResERR_ParmOutOfRange: "Parameter out of range",
        wavemeter_defs.ResERR_WlmOutOfResources: "Wavemeter is out of resources",
        wavemeter_defs.ResERR_WlmInternalError: "Wavemeter internal error",
        wavemeter_defs.ResERR_NotAvailable: "Not avalible",
        wavemeter_defs.ResERR_WlmBusy: "Wavemeter is busy",
        wavemeter_defs.ResERR_NotInMeasurementMode: "Not in measurement mode",
        wavemeter_defs.ResERR_OnlyInMeasurementMode: "Only in measurement mode",
        wavemeter_defs.ResERR_ChannelNotAvailable: "Channel is not avalible",
        wavemeter_defs.ResERR_ChannelTemporarilyNotAvailable: "Channel is temprorary not avalible",
        wavemeter_defs.ResERR_CalOptionNotAvailable: "Call option is not avalible",
        wavemeter_defs.ResERR_CalWavelengthOutOfRange: "Calibration wavelength is out of range",
        wavemeter_defs.ResERR_BadCalibrationSignal: "Bad calibration signal",
        wavemeter_defs.ResERR_UnitNotAvailable: "Unit is not avalible",
        wavemeter_defs.ResERR_FileNotFound: "File not found",
        wavemeter_defs.ResERR_FileCreation: "File creation",
        wavemeter_defs.ResERR_TriggerPending: "Trigger pending",
        wavemeter_defs.ResERR_TriggerWaiting: "Trigger waiting"
        }.get(value, "Unknown error")

class GetFuncError(Error):
    def __init__(self, value):
        self.value = value
        self.msg = self.message(value)

    def message(self, value):
        return {
        wavemeter_defs.ErrNoValue: "No value",
        wavemeter_defs.ErrNoSignal: "No signal",
        wavemeter_defs.ErrBadSignal: "Bad signal",
        wavemeter_defs.ErrLowSignal: "Low signal",
        wavemeter_defs.ErrBigSignal: "Big signal",
        wavemeter_defs.ErrWlmMissing: "Wavemeter is missing",
        wavemeter_defs.ErrNotAvailable: "Not avalible",
        wavemeter_defs.InfNothingChanged: "Nothing changed",
        wavemeter_defs.ErrNoPulse: "No pulse",
        wavemeter_defs.ErrDiv0: "Divide by 0",
        wavemeter_defs.ErrOutOfRange: "Out of range",
        wavemeter_defs.ErrUnitNotAvailable: "Unit not avalible" ,
        wavemeter_defs.ErrMaxErr: "Unit not avalible",

        # Return errorvalues of GetTemperature and GetPressure
        wavemeter_defs.ErrTempNotMeasured: "Temperature not measured",
        wavemeter_defs.ErrTempNotAvailable: "Temperature not avalible",
        wavemeter_defs.ErrTempWlmMissing: "Wavemeter is missing",

        # Return errorvalues of GetDistance
        # real errorvalues are ErrDistance combined with those of GetWavelength
        wavemeter_defs.ErrDistance: "Error distance",
        wavemeter_defs.ErrDistanceNotAvailable: "Distance not avalible",
        wavemeter_defs.ErrDistanceWlmMissing: "Wavemeter is missing"       }.get(value, "Unknown error")
        
        

class wavemeter(object):
    """Wrapper for wavemeter function calls"""
    def __init__(self):
#        self.wm = CDLL("C:\Windows\System32\wlmData.dll")
        try:
            self.wm = WinDLL("C:\Windows\System32\wlmData.dll")
        except:
            self.wm = None
            
        self.df = wavemeter_defs()

    def GetWavelengthNum(self, ch):
        # double GetWavelengthNum(long num, double WL);
        f = self.wm.GetWavelengthNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetFrequencyNum(self, ch):
        # double GetFrequencyNum(long num, double WL);
        f = self.wm.GetFrequencyNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetExposureNum(self, ch, ccd):
        # double GetFrequencyNum(long num, double WL);
        f = self.wm.GetExposureNum
        f.restype = c_long
        f.argtypes = [c_long, c_long, c_long]
        res = f(c_long(ch), c_long(ccd), c_long(0))
        if (res < 0):
            raise GetFuncError(res)
        return res

    def GetChannelsCount(self):
        f = self.wm.GetChannelsCount
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(0))
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetTemperature(self):
        f = self.wm.GetTemperature
        f.restype = c_double
        f.argtypes = [c_double]
        res = f(c_double(0.0))
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetPressure(self):
        f = self.wm.GetPressure
        f.restype = c_double
        f.argtypes = [c_double]
        res = f(c_double(0.0))
        if (res <= 0):
            raise GetFuncError(res)
        return res
        
    def SetSwitcherSignalStates(self, signal, use, show):
        f = self.wm.SetSwitcherSignalStates
        f.restype = c_long
        f.argtypes = [c_long, c_long, c_long]
        res = f(c_long(signal), c_long(use), c_long(show) )
        if (res < 0):
            raise SetFuncError(res)
        return res
        
    def GetSwitcherSignalStates(self, signal):
        f = self.wm.GetSwitcherSignalStates
        f.restype = c_long
        f.argtypes = [c_long, POINTER(c_long), POINTER(c_long)]
        use  = c_long(0)
        show = c_long(0)
        res = f(c_long(signal), byref(use), byref(show) )
        if (res <= 0):
            raise GetFuncError(res)
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
        if (res <= 0):
            raise GetFuncError(res)
        return res
         
    def GetSwitcherMode(self):
        f = self.wm.GetSwitcherMode
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(0))
        if (res <= 0):
            raise GetFuncError(res)
        return res        

    def SetSwitcherMode(self, mode):
        f = self.wm.SetSwitcherMode
        f.restype = c_long
        f.argtypes = [c_long]
        res = f(c_long(mode))
        if (res < 0):
            raise SetFuncError(res)
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
    try:
        print w.GetExposureNum(1, 1)
        print w.GetExposureNum(1, 2)
        print w.GetChannelsCount()
        print w.GetTemperature()
        print w.GetPressure()
        print w.GetSwitcherSignalStates(0)
        print w.Instantiate(w.df.cInstCheckForWLM, 0, 0, 0)
        print w.GetWLMVersion(0)
        print w.GetSwitcherMode()
        print w.ConvertUnit(369.0, w.df.cReturnWavelengthVac, w.df.cReturnFrequency)
        print w.ConvertUnit(935.0, w.df.cReturnWavelengthVac, w.df.cReturnFrequency)
        print w.GetWavelengthNum(0)
        print w.GetFrequencyNum(0)
#        print w.SetSwitcherSignalStates(0, 1, 1)
    except (GetFuncError, SetFuncError) as e:
        print "Error ", e.value, "  ", e.msg
        
    