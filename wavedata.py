# -*- coding:utf-8 -*-
"""
Created on Aug 4, 2013

@author: Dima
"""

from wavemeter import wavemeter, GetFuncError, SetFuncError
import time
import threading

w = wavemeter()

WM_CHANNEL_TIMEOUT = 60

class ChannelData(object):
    def __init__(self, channel):
        self.channel    = channel
        self.use        = 0 # False
        self.show       = 0 # False
        self.autoexposure = 0 # False
        self.wavelength = 0.0
        self.exposure   = 0
        self.exposure2  = 0
        self.error      = 0
        self.error_msg  = "_"
        self.hasdata    = False
        self.geterr     = GetFuncError(0) # We are interested in the message text only
        self.oktime     = time.time()
        self.errtime    = self.oktime
    
    # Prints data for a web page
    def writeData(self, file):
        if (self.hasdata):
            message = str(self.channel) + ", " + str(self.wavelength) + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
        else:
            message = str(self.channel) + ", " + self.error_msg + \
                       ", " + str(self.exposure) + ", " + str(self.exposure2) + "<br>\n"
       
        file.write(message)
            
    # prints message for server side events
    def SSEMessage(self):
        message =  "event: channel\n" 
        message += "data: { \"ch\": " + str(self.channel) + ", "
        if (self.hasdata):
            message += "\"wavelength\": \"" + str(self.wavelength) + "\","
        else:
            message += "\"wavelength\": \"" + self.error_msg + "\","
        message += " \"exposure1\": " + str(self.exposure) + ","
        message += " \"exposure2\": " + str(self.exposure2) + " }\n\n"
#        print message
        return message

    def SSEControlMessage(self):
        message = "event: control\n"
        message += "data: { \"ch\": " + str(self.channel) + ", "
        message += "\"use\": " + str(self.use) + ", "
        message += "\"auto\": " + str(self.autoexposure) + ", "
        message += "\"exposure1\": " + str(self.exposure) + ", "
        message += "\"exposure2\": " + str(self.exposure2) + " }\n\n"
#        print message
        return message
        
    # 
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
            
    def setUse(self, use, show):
        self.use  = use
        self.show = show
        if (self.use != 0): # Update all the timestamps when we enable the channel
            self.oktime = time.time()
            self.errtime = self.oktime
        
    def setAuto(self, auto):
        self.autoexposure = auto

    # Tells if the channel has to be shut down because there is no light
    def checkAutoOff(self):
        current_time = time.time()
        if (self.use > 0) and (current_time - self.oktime > WM_CHANNEL_TIMEOUT):
            return True
        else:
            return False

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
 
        for i in range(1, self.nchannels+1):
            res, use, show = w.GetSwitcherSignalStates(i)
            self.ch[i].setUse(use, show)
            auto = w.GetExposureModeNum(i)
            self.ch[i].setAuto(auto)
            self.ch[i].readExposure()

        # Ask for callback function and wait for data
        self.InstantiateWaitFunc()
        self.sockets = [] # Sockets that are interested in data

        self.cur_channels  = []
        self.prev_channels = []

    # Class destructor, removes wait for event callback
    def __del__(self):
        w.Instantiate(w.df.cInstNotification, w.df.cNotifyRemoveWaitEvent, 0, 0)
    
    def run(self):
        self.WaitForData()
    
    def writeData(self, file):
        for i in range(1, self.nchannels+1):
            self.ch[i].writeData(file)
            
    def addSSEClient(self, file):
        for i in range(1,9):
            file.write(self.ch[i].SSEMessage())
            file.write(self.ch[i].SSEControlMessage())
        self.sockets.append(file)
        print len(self.sockets), " clients connected"
        
    # change the controls according to the user requests from the web
    def controlState(self, channel, action, value):  
#        print channel, action, value
        if (action == "use"):
            res, use, show = w.GetSwitcherSignalStates(channel)
            use = value
            res = w.SetSwitcherSignalStates(channel, use, show)
            self.ch[channel].setUse(use, show)
            if (use == 0):
                self.ch[channel].setWavelength(0)
                self.notifySSEData(channel)
#            print "SetSwitcherSignalStates ", res
        elif (action == "auto"):
            res = w.SetExposureModeNum(channel, value)
            self.ch[channel].setAuto(value)
#            print "SetExposureModeNum ", res
        elif (action == "exp1"):
            res = w.SetExposureNum(channel, 1, value)
            self.ch[channel].setExposure1(value)
        elif (action == "exp2"):
            res = w.SetExposureNum(channel, 2, value)
            self.ch[channel].setExposure2(value)
        else:
            print "Unknown action ", action
            return
        
        self.notifySSEControl(channel)

    # Called when the new wave length data from the wave meter are received
    # checks if the channel status was changed in the wavemeter program directly
    # and notifies the web clients
    # Disables the channel if the channel gives the error for too long
    def updateChannelState(self, channel):
        # We get the data from the channel that is labelled inactive, fix it
        self.trackActiveChannels(channel)
        # if the channel is under / over exposed for a long time
        if (self.ch[channel].checkAutoOff()):
            try:
#                res, use, show = w.GetSwitcherSignalStates(channel)
#                use = 0
                res = w.SetSwitcherSignalStates(channel, 0, 0)
                self.ch[channel].setWavelength(0)
                self.ch[channel].setUse(0, 0)
                self.notifySSEData(channel)
                self.notifySSEControl(channel)
                print channel, "switched off automatically"
            except SetFuncError as e:
                print "Error switching off a channel: ", res, e
             
    # Notify clients about the new measurement results 
    def notifySSEClients(self, channel, message):
#        print message
        sockets_new = []
        for f in self.sockets:
            try:
                f.write(message)
                sockets_new.append(f) # copy good socket to a temp. list
#                print "bytes sent to SSE client", f
            except:
#                self.sockets.remove(f)
                print "SSE client disconnects"
        # assign list without dead sockets back to the original list
        self.sockets = sockets_new
        
    def notifySSEData(self, channel):
        message = self.ch[channel].SSEMessage()
        self.notifySSEClients(channel, message)
        
    def notifySSEControl(self, channel):
        message = self.ch[channel].SSEControlMessage()
        self.notifySSEClients(channel, message)
            
    def InstantiateWaitFunc(self):
        # Ask wavemeter to call WaitForWLMEvent whenever new data are ready
        res = w.Instantiate(w.df.cInstNotification, w.df.cNotifyInstallWaitEvent, -1, 0)
        print "Instantiate = ", res


    # Keep track which channels are active, and update the settings
    def trackActiveChannels(self, channel):
        if (channel in self.cur_channels):
            changes = set(self.cur_channels).symmetric_difference(self.prev_channels) # finds which channels have changed
            for c in changes:
                res, use, show = w.GetSwitcherSignalStates(c)
                self.ch[c].setUse(use, show)
                if use == 0:
                    self.ch[c].setWavelength(0)
                    self.notifySSEData(c)
                self.notifySSEControl(c)
                print c
            self.prev_channels = self.cur_channels
            self.cur_channels  = [channel]
        else:
            self.cur_channels.append(channel)


    # Main function: gets data in a loop and updates  
    def WaitForData(self):
        while(True):
            # Wait for the new data forever
            (ret, mode, IntVal, DblVal) = w.WaitForWLMEvent()
            
            # No wavemeter, return 
            if (ret == 0):
                return
            elif (ret == -2):
#                print "Unknown event or error\n"
                pass
            
            # Long switch - case to process the data
            # Wavelength
            if(mode == w.df.cmiWavelength1): 
                self.ch[1].setWavelength(DblVal)
                self.notifySSEData(1)
                self.updateChannelState(1)
            elif (mode == w.df.cmiWavelength2):
                self.ch[2].setWavelength(DblVal)
                self.notifySSEData(2)
                self.updateChannelState(2)
            elif (mode == w.df.cmiWavelength3):
                self.ch[3].setWavelength(DblVal)
                self.notifySSEData(3)
                self.updateChannelState(3)
            elif (mode == w.df.cmiWavelength4):
                self.ch[4].setWavelength(DblVal)
                self.notifySSEData(4)
                self.updateChannelState(4)
            elif (mode == w.df.cmiWavelength5):
                self.ch[5].setWavelength(DblVal)
                self.notifySSEData(5)
                self.updateChannelState(5)
            elif (mode == w.df.cmiWavelength6):
                self.ch[6].setWavelength(DblVal)
                self.notifySSEData(6)
                self.updateChannelState(6)
            elif (mode == w.df.cmiWavelength7):
                self.ch[7].setWavelength(DblVal)
                self.notifySSEData(7)
                self.updateChannelState(7)
            elif (mode == w.df.cmiWavelength8):
                self.ch[8].setWavelength(DblVal)
                self.notifySSEData(8)
                self.updateChannelState(8)
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
            # Exposure
            elif (mode == w.df.cmiExposureMode):
                pass
#            else:
#                print mode, IntVal, DblVal
        
