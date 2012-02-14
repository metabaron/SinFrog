# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Tue Feb 14 15:38:25 2012

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class MainPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SectorStaticText = wx.StaticText(self, -1, "Postal sector:")
        self.SectorChoice = wx.Choice(self, -1, choices=["1"])
        self.IspStaticText = wx.StaticText(self, -1, "ISP:")
        self.IspChoice = wx.Choice(self, -1, choices=["2"])
        self.PlanStaticText = wx.StaticText(self, -1, "Plan:")
        self.PlanChoice = wx.Choice(self, -1, choices=["3"])
        self.Ok = wx.Button(self, wx.ID_APPLY, "")
        self.Cancel = wx.Button(self, wx.ID_EXIT, "")
        self.ConfigurationSizer_staticbox = wx.StaticBox(self, -1, "Configuration")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainPanel.__set_properties
        self.SectorChoice.SetSelection(0)
        self.IspChoice.SetSelection(0)
        self.PlanChoice.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainPanel.__do_layout
        self.ConfigurationSizer_staticbox.Lower()
        ConfigurationSizer = wx.StaticBoxSizer(self.ConfigurationSizer_staticbox, wx.VERTICAL)
        ButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
        PlanSizer = wx.BoxSizer(wx.HORIZONTAL)
        IspSizer = wx.BoxSizer(wx.HORIZONTAL)
        SectorSizer = wx.BoxSizer(wx.HORIZONTAL)
        SectorSizer.Add(self.SectorStaticText, 0, 0, 0)
        SectorSizer.Add(self.SectorChoice, 0, wx.ALL, 0)
        ConfigurationSizer.Add(SectorSizer, 1, wx.EXPAND, 0)
        IspSizer.Add(self.IspStaticText, 0, 0, 0)
        IspSizer.Add(self.IspChoice, 0, wx.ALL, 0)
        ConfigurationSizer.Add(IspSizer, 1, wx.EXPAND, 0)
        PlanSizer.Add(self.PlanStaticText, 0, 0, 0)
        PlanSizer.Add(self.PlanChoice, 0, wx.ALL, 0)
        ConfigurationSizer.Add(PlanSizer, 1, wx.EXPAND, 0)
        ButtonSizer.Add(self.Ok, 0, 0, 0)
        ButtonSizer.Add(self.Cancel, 0, 0, 0)
        ConfigurationSizer.Add(ButtonSizer, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(ConfigurationSizer)
        ConfigurationSizer.Fit(self)
        # end wxGlade

# end of class MainPanel