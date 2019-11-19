#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# pip install --user --requirement requirements.txt


import wx
import writer2
import reader2
import fitz #pip install --upgrade pymupdf /PDF
import pdfviewer

class BiasRemovalGUI(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(BiasRemovalGUI, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        openF = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open')
        fileMenu.Append(openF)
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        Quit = wx.Menu()


        qmi = wx.MenuItem(Quit, wx.ID_EXIT, '&Quit\tCtrl+W')
        Quit.Append(qmi)



        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        panel.SetSizer(vbox)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
		
        self.t3 = wx.TextCtrl(panel,size = (1000,600),style = wx.TE_MULTILINE) 
        self.t3.SetBackgroundColour ((255,255,255))
        self.t3.SetForegroundColour((0,0,0))
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox3) 

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        self.Bind(wx.EVT_MENU, self.OnOpen, openF)
        menubar.Append(fileMenu, '&File')
        menubar.Append(Quit, '&Options')
        self.SetMenuBar(menubar)

        self.SetSize((1000, 600))
        self.SetTitle('CS489-Bias-Removal')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    def OnOpen(self, event):
        """
        if self.contentNotSaved:
            if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
                            wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return
        """
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open PDF file", wildcard="PDF files (*.pdf)|*.pdf",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    writer = writer2.WriteFile()
                    reader = reader2.ReadFile()
                    target_name_list = ["Andrew ", "Tomkins",
                        "Min ", "Zhang", "William ", " D.", "Heavlin" ]

                  
                    doc = writer.Marker(pathname, target_name_list)
                    doc.save("output.pdf", garbage=4, deflate=True, clean=True)
                    dlg = pdfviewer.PDFdisplay(wx.Panel(self), "output.pdf")
                    rc = dlg.ShowModal()
                    text = reader.read(pathname)
                   # self.t3.AppendText(text)
 


            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)


def main():

    app = wx.App()
    ex = BiasRemovalGUI(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()