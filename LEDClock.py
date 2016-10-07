import tkinter as tk
import time

class Clock_Display():
    def __init__(self,x0, y0):
        # h1 h0 : m1 m0 : s1 s0
        #       p1      p2
        self.size = 5
        self.FarbeAn = 'blue'
        self.FarbeAus = 'white'
        self.x0 = x0
        self.y0 = y0
        self.mainpart()

    def mainpart(self):
        self.h0 = TimeLetter(self.x0 + (self.size*13), self.y0, self.FarbeAus, self.FarbeAn, self.size)
        self.h1 = TimeLetter(self.x0, self.y0, self.FarbeAus, self.FarbeAn, self.size)
        self.p1 = Clock_Points(self.x0 +(self.size*25),self.y0, self.FarbeAn, self.size)#125
        self.m1 = TimeLetter(self.x0 + (self.size*27), self.y0, self.FarbeAus, self.FarbeAn, self.size)#135
        self.m0 = TimeLetter(self.x0 + (self.size*40), self.y0, self.FarbeAus, self.FarbeAn, self.size)#200
        self.p2 = Clock_Points(self.x0 + (self.size*52),self.y0, self.FarbeAn, self.size) #260
        self.s1 = TimeLetter(self.x0 + (self.size*54), self.y0, self.FarbeAus, self.FarbeAn, self.size)#270
        self.s0 = TimeLetter(self.x0 + (self.size*67), self.y0, self.FarbeAus, self.FarbeAn, self.size)#335

    def changeColor(self,PrimColor,SecColor):
        self.FarbeAn = PrimColor
        self.FarbeAus = SecColor
        self.mainpart()

    def changeSize(self,size):
        self.size = size
        self.mainpart()

class Clock_Points():
    def __init__(self,x0,y0, farb, size):
        self.Lines = [{"x":x0,"y":y0 + (size * 4.5),"wide":size,"hight":size,"farbe":farb},
                      {"x":x0,"y":y0 + (size * 14.5),"wide":size,"hight":size,"farbe":farb}]

class TimeLetter():
    def __init__(self,x0,y0, farbe0, farbe1, gsize):
        self.farbeAn = farbe1
        self.farbeAus = farbe0
        self.gsize = gsize
        self.TimeLetter(x0,y0)

    def TimeLetter(self,X,Y):

        #   ___0___
        #   |     |
        # 1 |__3__| 2
        # 4 |     | 5
        #   |__6__|

        self.Lines = [{"x":X+(self.gsize),"y":Y+0,"wide":(self.gsize * 9),"hight":(self.gsize),"farbe":self.farbeAus},#0
                      {"x":X+0,"y":Y+(self.gsize),"wide":(self.gsize),"hight":(self.gsize * 9),"farbe":self.farbeAus},#1
                      {"x":X+(self.gsize * 10),"y":Y+(self.gsize),"wide":(self.gsize),"hight":(self.gsize * 9),"farbe":self.farbeAus},#2
                      {"x":X+(self.gsize),"y":Y+(self.gsize * 10),"wide":(self.gsize * 9),"hight":(self.gsize),"farbe":self.farbeAus},#3
                      {"x":X+0,"y":Y+(self.gsize * 11),"wide":(self.gsize),"hight":(self.gsize * 9),"farbe":self.farbeAus},#4
                      {"x":X+(self.gsize * 10),"y":Y+(self.gsize * 11),"wide":self.gsize,"hight":(self.gsize * 9),"farbe":self.farbeAus},#5
                      {"x":X+(self.gsize),"y":Y+(self.gsize * 20),"wide":(self.gsize * 9),"hight":(self.gsize),"farbe":self.farbeAus}]#6

    def SetNumber(self,zahl):
        self.Lines[0]["farbe"]= self.farbeAus
        self.Lines[1]["farbe"]= self.farbeAus
        self.Lines[2]["farbe"]= self.farbeAus
        self.Lines[3]["farbe"]= self.farbeAus
        self.Lines[4]["farbe"]= self.farbeAus
        self.Lines[5]["farbe"]= self.farbeAus
        self.Lines[6]["farbe"]= self.farbeAus

        if zahl == 0 :
            for i in [0,1,2,4,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 1:
            for i in [2,5]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 2:
            for i in [0,2,3,4,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 3:
            for i in [0,2,3,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 4:
            for i in [1,2,3,5]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 5:
            for i in [0,1,3,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 6:
            for i in [0,1,3,4,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 7:
            for i in [0,2,5]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 8:
            for i in [0,1,2,3,4,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn
        elif zahl == 9:
            for i in [0,1,2,3,5,6]:
                self.Lines[i]["farbe"] = self.farbeAn

class Application(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.geometry("500x500")
        self.addClock()
        #self.runClock()
        self.after(800,self.runClock)

    def addClock(self):
        self.Clock = Clock_Display(50,50)
        self.Clock.changeColor('#0096AD',"#A6E0DB")
        self.Clock.changeSize(3)
        #for i in range(0,6):
        self.h0arr = []
        self.h1arr = []
        self.m0arr = []
        self.m1arr = []
        self.s0arr = []
        self.s1arr = []
        self.p1arr = []
        self.p2arr = []

        for i in range(0,7):
            self.h0arr.append(tk.Label(self,bg=self.Clock.h0.Lines[i]["farbe"]))
            self.h0arr[i].place(x = self.Clock.h0.Lines[i]["x"], y = self.Clock.h0.Lines[i]["y"], width = self.Clock.h0.Lines[i]["wide"], height= self.Clock.h0.Lines[i]["hight"])

            self.h1arr.append(tk.Label(self,bg=self.Clock.h1.Lines[i]["farbe"]))
            self.h1arr[i].place(x = self.Clock.h1.Lines[i]["x"], y = self.Clock.h1.Lines[i]["y"], width = self.Clock.h1.Lines[i]["wide"], height= self.Clock.h1.Lines[i]["hight"])

            self.m0arr.append(tk.Label(self,bg=self.Clock.m0.Lines[i]["farbe"]))
            self.m0arr[i].place(x = self.Clock.m0.Lines[i]["x"], y = self.Clock.m0.Lines[i]["y"], width = self.Clock.m0.Lines[i]["wide"], height= self.Clock.m0.Lines[i]["hight"])

            self.m1arr.append(tk.Label(self,bg=self.Clock.m1.Lines[i]["farbe"]))
            self.m1arr[i].place(x = self.Clock.m1.Lines[i]["x"], y = self.Clock.m1.Lines[i]["y"], width = self.Clock.m1.Lines[i]["wide"], height= self.Clock.m1.Lines[i]["hight"])

            self.s0arr.append(tk.Label(self,bg=self.Clock.s0.Lines[i]["farbe"]))
            self.s0arr[i].place(x = self.Clock.s0.Lines[i]["x"], y = self.Clock.s0.Lines[i]["y"], width = self.Clock.s0.Lines[i]["wide"], height= self.Clock.s0.Lines[i]["hight"])

            self.s1arr.append(tk.Label(self,bg=self.Clock.s1.Lines[i]["farbe"]))
            self.s1arr[i].place(x = self.Clock.s1.Lines[i]["x"], y = self.Clock.s1.Lines[i]["y"], width = self.Clock.s1.Lines[i]["wide"], height= self.Clock.s1.Lines[i]["hight"])

        for i in [0,1]:
            self.p1arr.append(tk.Label(self,bg=self.Clock.p1.Lines[i]["farbe"]))
            self.p1arr[i].place(x = self.Clock.p1.Lines[i]["x"], y = self.Clock.p1.Lines[i]["y"], width = self.Clock.p1.Lines[i]["wide"], height= self.Clock.p1.Lines[i]["hight"])

            self.p2arr.append(tk.Label(self,bg=self.Clock.p2.Lines[i]["farbe"]))
            self.p2arr[i].place(x = self.Clock.p2.Lines[i]["x"], y = self.Clock.p2.Lines[i]["y"], width = self.Clock.p2.Lines[i]["wide"], height= self.Clock.p2.Lines[i]["hight"])

        self.Clock.h0.SetNumber(8)
        self.Clock.h1.SetNumber(8)
        self.Clock.m0.SetNumber(8)
        self.Clock.m1.SetNumber(8)
        self.Clock.s0.SetNumber(8)
        self.Clock.s1.SetNumber(8)
        self.refreshColor()

    def runClock(self):

        lt = time.localtime()

        hh, mm, ss = lt[3:6]
        h1 = hh //10
        h0 = hh %10
        m1 = mm //10
        m0 = mm %10
        s1 = ss //10
        s0 = ss %10

        self.Clock.h0.SetNumber(h0)
        self.Clock.h1.SetNumber(h1)
        self.Clock.m0.SetNumber(m0)
        self.Clock.m1.SetNumber(m1)
        self.Clock.s0.SetNumber(s0)
        self.Clock.s1.SetNumber(s1)
        self.refreshColor()

        self.after(1000,self.runClock)

    def refreshColor(self):
        for i in range(0,7):
            self.h0arr[i]["bg"] = self.Clock.h0.Lines[i]["farbe"]
            self.h1arr[i]["bg"] = self.Clock.h1.Lines[i]["farbe"]
            self.m0arr[i]["bg"] = self.Clock.m0.Lines[i]["farbe"]
            self.m1arr[i]["bg"] = self.Clock.m1.Lines[i]["farbe"]
            self.s0arr[i]["bg"] = self.Clock.s0.Lines[i]["farbe"]
            self.s1arr[i]["bg"] = self.Clock.s1.Lines[i]["farbe"]

        for i in [0,1]:
            self.p1arr[i]["bg"] = self.Clock.p1.Lines[i]["farbe"]
            self.p2arr[i]["bg"] = self.Clock.p2.Lines[i]["farbe"]

if __name__ == "__main__":
    app = Application(None)
    app.mainloop()
