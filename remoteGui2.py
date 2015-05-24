#!/usr/bin/env python

'''
Author: Oscar Koeroo
Description: This module will be the GUI for the Samsung Remote application.
'''

import wx
from remote import *
import time

#MAC : 0c-89-10-e8-ae-4d
#IP  : 192.168.1.41


class SmartTVRemote(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450, 400), style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        self.parent = parent

        #Main panel
        panel        = wx.Panel(self, 1)

        self.OFFSET_LEFT = 5
        self.OFFSET_TOP  = 5

        # Numerical keyboard
        panel_numpad = wx.Panel(panel, 2, pos=(0, 0), size=(110, 140),  style=wx.SUNKEN_BORDER)
        button_0 = wx.Button(panel_numpad, 40, '0', pos=(self.OFFSET_LEFT + 30, self.OFFSET_TOP + 90), size=(30, 30))
        button_1 = wx.Button(panel_numpad, 41, '1', pos=(self.OFFSET_LEFT +  0, self.OFFSET_TOP + 60), size=(30, 30))
        button_2 = wx.Button(panel_numpad, 42, '2', pos=(self.OFFSET_LEFT + 30, self.OFFSET_TOP + 60), size=(30, 30))
        button_3 = wx.Button(panel_numpad, 43, '3', pos=(self.OFFSET_LEFT + 60, self.OFFSET_TOP + 60), size=(30, 30))
        button_4 = wx.Button(panel_numpad, 44, '4', pos=(self.OFFSET_LEFT +  0, self.OFFSET_TOP + 30), size=(30, 30))
        button_5 = wx.Button(panel_numpad, 45, '5', pos=(self.OFFSET_LEFT + 30, self.OFFSET_TOP + 30), size=(30, 30))
        button_6 = wx.Button(panel_numpad, 46, '6', pos=(self.OFFSET_LEFT + 60, self.OFFSET_TOP + 30), size=(30, 30))
        button_7 = wx.Button(panel_numpad, 47, '7', pos=(self.OFFSET_LEFT +  0, self.OFFSET_TOP +  0), size=(30, 30))
        button_8 = wx.Button(panel_numpad, 48, '8', pos=(self.OFFSET_LEFT + 30, self.OFFSET_TOP +  0), size=(30, 30))
        button_9 = wx.Button(panel_numpad, 49, '9', pos=(self.OFFSET_LEFT + 60, self.OFFSET_TOP +  0), size=(30, 30))

        button_0.Bind(wx.EVT_BUTTON, self.On_0)
        button_1.Bind(wx.EVT_BUTTON, self.On_1)
        button_2.Bind(wx.EVT_BUTTON, self.On_2)
        button_3.Bind(wx.EVT_BUTTON, self.On_3)
        button_4.Bind(wx.EVT_BUTTON, self.On_4)
        button_5.Bind(wx.EVT_BUTTON, self.On_5)
        button_6.Bind(wx.EVT_BUTTON, self.On_6)
        button_7.Bind(wx.EVT_BUTTON, self.On_7)
        button_8.Bind(wx.EVT_BUTTON, self.On_8)
        button_9.Bind(wx.EVT_BUTTON, self.On_9)

        # Page Up/Down
        panel_updown = wx.Panel(panel, 3, pos=(150, 0), size=(175, 75), style=wx.SUNKEN_BORDER)
        button_up = wx.Button(panel_updown, 50, 'Channel Up', pos=(self.OFFSET_LEFT + 0, self.OFFSET_TOP + 0))
        button_down  = wx.Button(panel_updown, 50, 'Channel Down', pos=(self.OFFSET_LEFT + 0, self.OFFSET_TOP + 30))

        button_up.Bind(wx.EVT_BUTTON, self.OnPageUp)
        button_down.Bind(wx.EVT_BUTTON, self.OnPageDown)

        # Volume Up/Down
        panel_volupdown = wx.Panel(panel, 4, pos=(0, 150), size=(190, 75), style=wx.SUNKEN_BORDER)
        button_volup = wx.Button(panel_volupdown, 50, 'Volume Up', pos=(self.OFFSET_LEFT + 0, self.OFFSET_TOP + 0), size=(170, 30))
        button_voldown  = wx.Button(panel_volupdown, 50, 'Volume Down', pos=(self.OFFSET_LEFT + 0, self.OFFSET_TOP + 30), size=(170, 30))

        button_volup.Bind(wx.EVT_BUTTON, self.OnVolUp)
        button_voldown.Bind(wx.EVT_BUTTON, self.OnVolDown)

        # Presets
        panel_presets = wx.Panel(panel, 5, pos=(0, 250), size=(190, 75), style=wx.SUNKEN_BORDER)
        button_preset_1 = wx.Button(panel_presets, 50, '311 - Zappelin', pos=(self.OFFSET_LEFT + 0, self.OFFSET_TOP + 0), size=(170, 30))
        button_preset_1.Bind(wx.EVT_BUTTON, self.OnPreset_1)


        # Statusbar
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(2)

        # Centre frame
        self.Centre()

    def OnPreset_1(self, id):
        self.sb.SetStatusText('Last key: Preset 1 - 311', 0)

        # Send
        cc.SendKey('KEY_3')
        time.sleep(0.3)
        cc.SendKey('KEY_1')
        time.sleep(0.3)
        cc.SendKey('KEY_1')


    def OnPageUp(self, id):
        cc.SendKey('KEY_CHUP')
        self.sb.SetStatusText('Last key: channel up', 0)

    def OnPageDown(self, id):
        cc.SendKey('KEY_CHDOWN')
        self.sb.SetStatusText('Last key: channel down', 0)

    def OnVolUp(self, id):
        cc.SendKey('KEY_VOLUP')
        self.sb.SetStatusText('Last key: volume up', 0)

    def OnVolDown(self, id):
        cc.SendKey('KEY_VOLDOWN')
        self.sb.SetStatusText('Last key: volume down', 0)

    def On_0(self, id):
        cc.SendKey('KEY_0')
        self.sb.SetStatusText('Last key: num 0', 0)

    def On_1(self, id):
        cc.SendKey('KEY_1')
        self.sb.SetStatusText('Last key: num 1', 0)

    def On_2(self, id):
        cc.SendKey('KEY_2')
        self.sb.SetStatusText('Last key: num 2', 0)

    def On_3(self, id):
        cc.SendKey('KEY_3')
        self.sb.SetStatusText('Last key: num 3', 0)

    def On_4(self, id):
        cc.SendKey('KEY_4')
        self.sb.SetStatusText('Last key: num 4', 0)

    def On_5(self, id):
        cc.SendKey('KEY_5')
        self.sb.SetStatusText('Last key: num 5', 0)

    def On_6(self, id):
        cc.SendKey('KEY_6')
        self.sb.SetStatusText('Last key: num 6', 0)

    def On_7(self, id):
        cc.SendKey('KEY_7')
        self.sb.SetStatusText('Last key: num 7', 0)

    def On_8(self, id):
        cc.SendKey('KEY_8')
        self.sb.SetStatusText('Last key: num 8', 0)

    def On_9(self, id):
        cc.SendKey('KEY_9')
        self.sb.SetStatusText('Last key: num 9', 0)


class ConnectionCenter():
    def __init__(self):
        self.myremote = Remote('192.168.1.41','0C-89-10-E8-AE-4D','Samsung LED46')

    def Connect(self):
        self.myremote.connect()

    def SendKey(self, key):
        self.myremote.sendkey(key)

    def Disconnect(self):
        self.myremote.close()


class SmartTVRemoteApp(wx.App):
    def OnInit(self):
        frame = SmartTVRemote(None, -1, 'Samsung SmartTV Remote')
        frame.Show(True)
        return True

############### MAIN ##############
if __name__ == '__main__':
    cc = ConnectionCenter()
    app = SmartTVRemoteApp(0)
    try:
        cc.Connect()
        app.MainLoop()

    finally:
        cc.Disconnect()
