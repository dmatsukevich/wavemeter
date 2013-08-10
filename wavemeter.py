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
    cReturnWavelengthVac = 0
    cReturnWavelengthAir = 1
    cReturnFrequency = 2
    cReturnWavenumber = 3
    cReturnPhotonEnergy = 4

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
    ErrNoValue = 0
    ErrNoSignal = -1
    ErrBadSignal = -2
    ErrLowSignal = -3
    ErrBigSignal = -4
    ErrWlmMissing = -5
    ErrNotAvailable = -6
    InfNothingChanged = -7
    ErrNoPulse = -8
    ErrDiv0 = -13
    ErrOutOfRange = -14
    ErrUnitNotAvailable = -15
    ErrMaxErr = ErrUnitNotAvailable

    # Return errorvalues of GetTemperature and GetPressure
    ErrTemperature = -1000
    ErrTempNotMeasured = ErrTemperature + ErrNoValue
    ErrTempNotAvailable = ErrTemperature + ErrNotAvailable
    ErrTempWlmMissing = ErrTemperature + ErrWlmMissing

    # Return errorvalues of GetDistance
    # real errorvalues are ErrDistance combined with those of GetWavelength
    ErrDistance = -1000000000
    ErrDistanceNotAvailable = ErrDistance + ErrNotAvailable
    ErrDistanceWlmMissing = ErrDistance + ErrWlmMissing
    
    # Mode Constants for Callback-Export and WaitForWLMEvent-function
    cmiResultMode = 1
    cmiRange = 2
    cmiPulse = 3
    cmiPulseMode = cmiPulse
    cmiWideLine = 4
    cmiWideMode = cmiWideLine
    cmiFast = 5
    cmiFastMode = cmiFast
    cmiExposureMode = 6
    cmiExposureValue1 = 7
    cmiExposureValue2 = 8
    cmiDelay = 9
    cmiShift = 10
    cmiShift2 = 11
    cmiReduce = 12
    cmiReduced = cmiReduce
    cmiScale = 13
    cmiTemperature = 14
    cmiLink = 15
    cmiOperation = 16
    cmiDisplayMode = 17
    cmiPattern1a = 18
    cmiPattern1b = 19
    cmiPattern2a = 20
    cmiPattern2b = 21
    cmiMin1 = 22
    cmiMax1 = 23
    cmiMin2 = 24
    cmiMax2 = 25
    cmiNowTick = 26
    cmiCallback = 27
    cmiFrequency1 = 28
    cmiFrequency2 = 29
    cmiDLLDetach = 30
    cmiVersion = 31
    cmiAnalysisMode = 32
    cmiDeviationMode = 33
    cmiDeviationReference = 34
    cmiDeviationSensitivity = 35
    cmiAppearance = 36
    cmiAutoCalMode = 37
    cmiWavelength1 = 42
    cmiWavelength2 = 43
    cmiLinewidth = 44
    cmiLinewidthMode = 45
    cmiLinkDlg = 56
    cmiAnalysis = 57
    cmiAnalogIn = 66
    cmiAnalogOut = 67
    cmiDistance = 69
    cmiWavelength3 = 90
    cmiWavelength4 = 91
    cmiWavelength5 = 92
    cmiWavelength6 = 93
    cmiWavelength7 = 94
    cmiWavelength8 = 95
    cmiVersion0 = cmiVersion
    cmiVersion1 = 96
    cmiDLLAttach = 121
    cmiSwitcherSignal = 123
    cmiSwitcherMode = 124
    cmiExposureValue11 = cmiExposureValue1
    cmiExposureValue12 = 125
    cmiExposureValue13 = 126
    cmiExposureValue14 = 127
    cmiExposureValue15 = 128
    cmiExposureValue16 = 129
    cmiExposureValue17 = 130
    cmiExposureValue18 = 131
    cmiExposureValue21 = cmiExposureValue2
    cmiExposureValue22 = 132
    cmiExposureValue23 = 133
    cmiExposureValue24 = 134
    cmiExposureValue25 = 135
    cmiExposureValue26 = 136
    cmiExposureValue27 = 137
    cmiExposureValue28 = 138
    cmiPatternAverage = 139
    cmiPatternAvg1 = 140
    cmiPatternAvg2 = 141
    cmiAnalogOut1 = cmiAnalogOut
    cmiAnalogOut2 = 142
    cmiMin11 = cmiMin1
    cmiMin12 = 146
    cmiMin13 = 147
    cmiMin14 = 148
    cmiMin15 = 149
    cmiMin16 = 150
    cmiMin17 = 151
    cmiMin18 = 152
    cmiMin21 = cmiMin2
    cmiMin22 = 153
    cmiMin23 = 154
    cmiMin24 = 155
    cmiMin25 = 156
    cmiMin26 = 157
    cmiMin27 = 158
    cmiMin28 = 159
    cmiMax11 = cmiMax1
    cmiMax12 = 160
    cmiMax13 = 161
    cmiMax14 = 162
    cmiMax15 = 163
    cmiMax16 = 164
    cmiMax17 = 165
    cmiMax18 = 166
    cmiMax21 = cmiMax2
    cmiMax22 = 167
    cmiMax23 = 168
    cmiMax24 = 169
    cmiMax25 = 170
    cmiMax26 = 171
    cmiMax27 = 172
    cmiMax28 = 173
    cmiAvg11 = cmiPatternAvg1
    cmiAvg12 = 174
    cmiAvg13 = 175
    cmiAvg14 = 176
    cmiAvg15 = 177
    cmiAvg16 = 178
    cmiAvg17 = 179
    cmiAvg18 = 180
    cmiAvg21 = cmiPatternAvg2
    cmiAvg22 = 181
    cmiAvg23 = 182
    cmiAvg24 = 183
    cmiAvg25 = 184
    cmiAvg26 = 185
    cmiAvg27 = 186
    cmiAvg28 = 187
    cmiPatternAnalysisWritten = 202
    cmiSwitcherChannel = 203
    cmiAnalogOut3 = 237
    cmiAnalogOut4 = 238
    cmiAnalogOut5 = 239
    cmiAnalogOut6 = 240
    cmiAnalogOut7 = 241
    cmiAnalogOut8 = 242
    cmiIntensity = 251
    cmiPower = 267
    cmiActiveChannel = 300
    cmiPIDCourse = 1030
    cmiPIDUseTa = 1031
    cmiPIDUseT = cmiPIDUseTa
    cmiPID_T = 1033
    cmiPID_P = 1034
    cmiPID_I = 1035
    cmiPID_D = 1036
    cmiDeviationSensitivityDim = 1040
    cmiDeviationSensitivityFactor = 1037
    cmiDeviationPolarity = 1038
    cmiDeviationSensitivityEx = 1039
    cmiDeviationUnit = 1041
    cmiPIDConstdt = 1059
    cmiPID_dt = 1060
    cmiPID_AutoClearHistory = 1061
    cmiDeviationChannel = 1063
    cmiAutoCalPeriod = 1120
    cmiAutoCalUnit = 1121
    cmiServerInitialized = 1124
    cmiWavelength9 = 1130
    cmiExposureValue19 = 1155
    cmiExposureValue29 = 1180
    cmiMin19 = 1205
    cmiMin29 = 1230
    cmiMax19 = 1255
    cmiMax29 = 1280
    cmiAvg19 = 1305
    cmiAvg29 = 1330
    cmiWavelength10 = 1355
    cmiWavelength11 = 1356
    cmiWavelength12 = 1357
    cmiWavelength13 = 1358
    cmiWavelength14 = 1359
    cmiWavelength15 = 1360
    cmiWavelength16 = 1361
    cmiWavelength17 = 1362
    cmiExternalInput = 1400
    cmiPressure = 1465
    cmiBackground = 1475
    cmiDistanceMode = 1476
    cmiInterval = 1477
    cmiIntervalMode = 1478
    cmiCalibrationEffect = 1480
    cmiLinewidth1 = cmiLinewidth
    cmiLinewidth2 = 1481
    cmiLinewidth3 = 1482
    cmiLinewidth4 = 1483
    cmiLinewidth5 = 1484
    cmiLinewidth6 = 1485
    cmiLinewidth7 = 1486
    cmiLinewidth8 = 1487
    cmiLinewidth9 = 1488
    cmiLinewidth10 = 1489
    cmiLinewidth11 = 1490
    cmiLinewidth12 = 1491
    cmiLinewidth13 = 1492
    cmiLinewidth14 = 1493
    cmiLinewidth15 = 1494
    cmiLinewidth16 = 1495
    cmiLinewidth17 = 1496
    cmiTriggerState = 1497

#   WLM Control Mode Constants
    cCtrlWLMShow = 1
    cCtrlWLMHide = 2
    cCtrlWLMExit = 3
    cCtrlWLMWait = 0x0010
    cCtrlWLMStartSilent = 0x0020
    cCtrlWLMSilent = 0x0040

#  Operation Mode Constants (for "Operation" and "GetOperationState" functions)
    cStop = 0
    cAdjustment = 1
    cMeasurement = 2



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
        # double GetWavelengthNum(long num, double WL)
        f = self.wm.GetWavelengthNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetFrequencyNum(self, ch):
        # double GetFrequencyNum(long num, double WL)
        f = self.wm.GetFrequencyNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0) )
        if (res <= 0):
            raise GetFuncError(res)
        return res

    def GetExposureNum(self, ch, ccd):
        # double GetFrequencyNum(long num, double WL)
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
        if (res < 0):
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
    
    def GetPowerNum(self, ch):
        f = self.wm.GetPowerNum
        f.restype = c_double
        f.argtypes = [c_long, c_double]
        res = f(c_long(ch), c_double(0.0))
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

    def SetExposureNum(self, ch, ccd, exposure):
        f = self.wm.SetExposureNum
        f.restype = c_long
        f.argtypes = [c_long, c_long, c_long]
        res = f(c_long(ch), c_long(ccd), c_long(exposure) )
        if (res < 0):
            raise SetFuncError(res)
        return res        
    
    def SetExposureModeNum(self, ch, mode):
        f = self.wm.SetExposureModeNum
        f.restype = c_long
        f.argtypes = [c_long, c_long]
        res = f(c_long(ch), c_long(mode) )
        if (res < 0):
            raise SetFuncError(res)
        return res        
       
    def GetExposureModeNum(self, ch):
        f = self.wm.SetExposureModeNum
        f.restype = c_long
        f.argtypes = [c_long, c_long]
        res = f(c_long(ch), c_long(0))
        if (res < 0):
            raise GetFuncError(res)
        return res        
       
    def ConvertUnit(self, val, uFrom, uTo):
        f = self.wm.ConvertUnit
        f.restype = c_double
        f.argtypes = [c_double, c_long, c_long]
        res = f(c_double(val), c_long(uFrom), c_long(uTo))
        return res        
    
    def WaitForWLMEvent(self):
        f = self.wm.WaitForWLMEvent
        f.restype  = c_long
        f.argtypes = [POINTER(c_long), POINTER(c_long), POINTER(c_double)]
        mode    = c_long(0)
        int_val = c_long(0)
        dbl_val = c_double(0.0)
        res = f(byref(mode), byref(int_val), byref(dbl_val) )
#        print "WaitForWLMEvent", res, mode.value, int_val.value, dbl_val.value
        return res, mode.value, int_val.value, dbl_val.value
        
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
        
    