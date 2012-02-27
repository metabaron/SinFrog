# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Wed Feb 15 11:40:44 2012

import wx, threading, configobj, os.path, urllib2
from AboutFrame import AboutFrame
from DisplayFrame import DisplayFrame
from ping import verbose_ping
from speed import SpeedClass


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class SinFrogMainWindow(wx.Frame):
    
    def __init__(self, *args, **kwds):
        # begin wxGlade: SinFrogMainWindow.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.SinFrogMainWindow_menubar = wx.MenuBar()
        self.File = wx.Menu()
        self.SaveName = wx.MenuItem(self.File, wx.NewId(), "Save", "Save preferences", wx.ITEM_NORMAL)
        self.File.AppendItem(self.SaveName)
        self.File.AppendSeparator()
        self.QuitName = wx.MenuItem(self.File, wx.NewId(), "Quit", "Quit application", wx.ITEM_NORMAL)
        self.File.AppendItem(self.QuitName)
        self.SinFrogMainWindow_menubar.Append(self.File, "File")
        wxglade_tmp_menu = wx.Menu()
        self.AboutName = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "About", "About application", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.AboutName)
        self.SinFrogMainWindow_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.SinFrogMainWindow_menubar)
        # Menu Bar end
        self.SinFrogMainWindow_statusbar = self.CreateStatusBar(1, 0)
        self.DistrictsLabel = wx.StaticText(self, -1, "District:")
        self.DistrictsCombobox = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        self.IspLabel = wx.StaticText(self, -1, "ISP name:")
        self.IspCombobox = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        self.PlanLabel = wx.StaticText(self, -1, "Plan name:")
        self.PlanCombobox = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        self.UserIdentificationLabel = wx.StaticText(self, -1, "Identification number")
        self.UserIdentificationValue = wx.StaticText(self, -1, "")
        self.SaveButton = wx.Button(self, wx.ID_SAVE, "")
        self.QuitButton = wx.Button(self, wx.ID_EXIT, "")
        self.RunButton = wx.Button(self, -1, "Run")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.saveMenu, self.SaveName)
        self.Bind(wx.EVT_MENU, self.quitMenu, self.QuitName)
        self.Bind(wx.EVT_MENU, self.aboutMenu, self.AboutName)
        self.Bind(wx.EVT_COMBOBOX, self.IspChanged, self.IspCombobox)
        self.Bind(wx.EVT_BUTTON, self.saveMenu, self.SaveButton)
        self.Bind(wx.EVT_BUTTON, self.quitMenu, self.QuitButton)
        self.Bind(wx.EVT_BUTTON, self.runButton, self.RunButton)
        # end wxGlade
        
        #Loading Combobox content
        self.DistrictsCombobox.AppendItems(["01 = Raffles Place, Cecil, Marina, People's Park", "02 = Anson, Tanjong Pagar", "03 = Queenstown, Tiong Bahru", "04 = Telok Blangah, Harbourfront", "05 = Pasir Panjang, Hong Leong Garden, Clementi New Town", "06 = High Street, Beach Road (part)", "07 = Middle Road, Golden Mile", "08 = Little India", "09 = Orchard, Cairnhill, River Valley", "10 = Ardmore, Bukit Timah, Holland Road, Tanglin", "11 = Watten Estate, Novena, Thomson", "12 = Balestier, Toa Payoh, Serangoon", "13 = Macpherson, Braddell", "14 = Geylang, Eunos", "15 = Katong, Joo Chiat,,Amber Road", "16 = Bedok, Upper East Coast, Eastwood, Kew Drive", "17 = Loyang, Changi", "18 = Simei, Tampines, Pasir Ris", "19 = Serangoon,Garden, Hougang, Ponggol", "20 = Bishan, Ang Mo Kio", "21 = Upper Bukit Timah, Clementi Park, Ulu Pandan", "22 = Jurong", "23 = Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang", "24 = Lim Chu Kang, Tengah", "25 = Kranji, Woodgrove, Woodlands", "26 = Upper Thomson, Springleaf", "27 = Yishun, Sembawang", "28 = Seletar"])
        self.IspCombobox.AppendItems(["ViewQwest", "Singtel", "StarHub", "M1", "MyRepublic", "SuperInternet"])

    def __set_properties(self):
        # begin wxGlade: SinFrogMainWindow.__set_properties
        self.SetTitle("SinFrog")
        self.SinFrogMainWindow_statusbar.SetStatusWidths([-1])
        # statusbar fields
        SinFrogMainWindow_statusbar_fields = ["SinFrogMainWindow_statusbar"]
        for i in range(len(SinFrogMainWindow_statusbar_fields)):
            self.SinFrogMainWindow_statusbar.SetStatusText(SinFrogMainWindow_statusbar_fields[i], i)
        self.DistrictsCombobox.SetMinSize((300, 21))
        self.UserIdentificationLabel.Hide()
        self.UserIdentificationValue.Hide()
        self.RunButton.Hide()
        # end wxGlade
        
        #Checking config.ini existence
        if os.path.exists(r'config.ini'):
            config = configobj.ConfigObj("config.ini")
            district = config['District']
            isp = config['ISP']
            plan = config['Plan']
            user = config['User']
            self.DistrictsCombobox.SetValue(district['name'])
            self.IspCombobox.SetValue(isp['name'])
            self.PlanCombobox.SetValue(plan['name'])
            self.userIdentification = user['identification']
            self.UserIdentificationValue.SetLabel(self.userIdentification)
            self.UserIdentificationValue.Show()
            self.UserIdentificationLabel.Show()
            self.RunButton.Show()
        else:
            self.DistrictsCombobox.SetValue("Select your district of residence please.")
            self.IspCombobox.SetValue("Select your optical fibre ISP please.")
            self.PlanCombobox.SetValue("Will be updated accordingly to ISP.")            

    def __do_layout(self):
        # begin wxGlade: SinFrogMainWindow.__do_layout
        SinFrogSizer = wx.BoxSizer(wx.VERTICAL)
        ButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
        PreferencesSizer = wx.GridSizer(3, 2, 0, 0)
        PreferencesSizer.Add(self.DistrictsLabel, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.DistrictsCombobox, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.IspLabel, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.IspCombobox, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.PlanLabel, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.PlanCombobox, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.UserIdentificationLabel, 0, wx.EXPAND, 0)
        PreferencesSizer.Add(self.UserIdentificationValue, 0, wx.EXPAND, 0)
        SinFrogSizer.Add(PreferencesSizer, 1, wx.EXPAND, 0)
        ButtonSizer.Add(self.SaveButton, 0, wx.EXPAND, 0)
        ButtonSizer.Add(self.QuitButton, 0, wx.EXPAND, 0)
        ButtonSizer.Add(self.RunButton, 0, wx.EXPAND, 0)
        SinFrogSizer.Add(ButtonSizer, 1, wx.EXPAND, 0)
        self.SetSizer(SinFrogSizer)
        SinFrogSizer.Fit(self)
        self.Layout()
        # end wxGlade

    #Click on a "Save" button
    def saveMenu(self, event):  # wxGlade: SinFrogMainWindow.<event_handler>
        if (self.DistrictsCombobox.GetCurrentSelection() > -1) and (self.IspCombobox.GetCurrentSelection() > -1) and (self.PlanCombobox.GetCurrentSelection() > -1):
            #New user so generating a userID
            url = ('http://sinfrog.metabaron.net/userID.php')
            f = urllib2.urlopen(url)
            self.userIdentification = f.read()
            f.close()
            
            config = configobj.ConfigObj()
            config.filename = "config.ini"
            config["District"] = {}
            config["District"]["name"] = self.DistrictsCombobox.GetValue()
            config["ISP"] = {}
            config["ISP"]["name"] = self.IspCombobox.GetValue()
            config["Plan"] = {}
            config["Plan"]["name"] = self.PlanCombobox.GetValue()
            config["User"] = {}
            config["User"]["identification"] = self.userIdentification
            config.write()
            self.UserIdentificationValue.SetLabel(self.userIdentification)
            self.UserIdentificationValue.Show()
            self.UserIdentificationLabel.Show()
            self.SinFrogMainWindow_statusbar.SetStatusText("Saved.")
            self.RunButton.Show()
            self.Layout()
        else:
            self.SinFrogMainWindow_statusbar.SetStatusText("ERROR: Please select both distric, IPS and plan name first.")

    def quitMenu(self, event):  # wxGlade: SinFrogMainWindow.<event_handler>
        self.Destroy()

    def aboutMenu(self, event):  # wxGlade: SinFrogMainWindow.<event_handler>
        about = AboutFrame(None)
        about.Show()

    #Trigger when you change the ISP
    def IspChanged(self, event):  # wxGlade: SinFrogMainWindow.<event_handler>
        if event.GetString() == "Singtel":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your Singtel plan please.")
            self.PlanCombobox.AppendItems(["exPress 50/25", "exPress 100/50", "exPress 150/50", "exPlore Home 50/25", "exPlore Home Sports 50/25", "exPlore Home 100/50", "exPlore Home Sports 100/50", "exPlore Home 200/100", "exPlore Home Sports 200/100", "exCiteHome 200/100"])
        elif event.GetString() == "ViewQwest":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your ViewQwest plan please.")
            self.PlanCombobox.AppendItems(["ViewQwest 60/50", "ViewQwest 100/50", "ViewQwest 150/75", "ViewQwest 200/100", "ViewQwest 500/200", "ViewQwest 1000/500", "ViewQwest 200/100 Static"])
        elif event.GetString() == "StarHub":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your StarHub plan please.")
            self.PlanCombobox.AppendItems(["MaxInfinity Premium Plus 50/25", "MaxInfinity Ultimate Plus 100/50", "MaxInfinity Elite Plus 150/75", "MaxInfinity Platinum Plus 200/100"])
        elif event.GetString() == "M1":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your M1 plan please.")
            self.PlanCombobox.AppendItems(["HomePac 25/25", "HomePac 50/50", "HomePac 100/50", "HomePac 150/75", "HomePac 200/100", "HomePac 1000/500"])
        elif event.GetString() == "MyRepublic":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your MyRepublic plan please.")
            self.PlanCombobox.AppendItems(["Pure 100", "Gamer 100", "Tutor 100"])
        elif event.GetString() == "SuperInternet":
            self.PlanCombobox.Clear()
            self.PlanCombobox.SetValue("Select your SuperInternet plan please.")
            self.PlanCombobox.AppendItems(["100Mbps Basic Residential Service / 12 months", "100Mbps Basic Residential Service / 24 months", "100Mbps Home Premium Service / 12 months", "100Mbps Home Premium Service / 24 months"])

    #Start ping and download tests
    def runButton(self, event):  # wxGlade: SinFrogMainWindow.<event_handler>
        self.SinFrogMainWindow_statusbar.SetStatusText("Running tests.")
        display = DisplayFrame(None)
        display.Show()
            
        display.DisplayFrame_statusbar.SetStatusText("Pinging yahoo.com")
        verbose_ping("yahoo.com", displayTarget = display)
        display.DisplayFrame_statusbar.SetStatusText("Pinging done")
            
        display.DisplayFrame_statusbar.SetStatusText("Speed testing")
        speedClass = SpeedClass('http://itc.conversationsnetwork.org/audio/download/ITC.SO-Episode69-2009.09.29.mp3', display)
        #speedClass.start()

# end of class SinFrogMainWindow