from tkinter import *
from tkinter import messagebox

topframe=Tk()

topframe.geometry('500x300')
topframe.title('calculator')
topframe.configure(bg="light blue")
#buttons 
a1=Button(topframe,text='1',height=3,width=15,command=lambda: keyLog(1))
a1.place(x=5,y=50)

a2=Button(topframe,text='2',height=3,width=15,command=lambda: keyLog(2))
a2.place(x=125,y=50)

a3=Button(topframe,text='3',height=3,width=15,command=lambda: keyLog(3))
a3.place(x=245,y=50)

a4=Button(topframe,text='4',height=3,width=15,command=lambda: keyLog(4))
a4.place(x=5,y=110)

a5=Button(topframe,text='5',height=3,width=15,command=lambda: keyLog(5))
a5.place(x=125,y=110)

a6=Button(topframe,text='6',height=3,width=15,command=lambda: keyLog(6))
a6.place(x=245,y=110)

a7=Button(topframe,text='7',height=3,width=15,command=lambda: keyLog(7))
a7.place(x=5,y=170)

a8=Button(topframe,text='8',height=3,width=15,command=lambda: keyLog(8))
a8.place(x=125,y=170)

a9=Button(topframe,text='9',height=3,width=15,command=lambda: keyLog(9))
a9.place(x=245,y=170)

a0=Button(topframe,text='0',height=3,width=15,command=lambda: keyLog(0))
a0.place(x=125,y=230)
asum=Button(topframe,text='+',height=3,width=15,command=lambda: keyLog('+'))
asum.place(x=365,y=50)

asub=Button(topframe,text='-',height=3,width=15,command=lambda: keyLog('-'))
asub.place(x=365,y=110)

adiv=Button(topframe,text='%',height=3,width=15,command=lambda: keyLog('/'))
adiv.place(x=365,y=230)

amul=Button(topframe,text='x',height=3,width=15,command=lambda: keyLog('*'))
amul.place(x=365,y=170)

aclear=Button(topframe,text='clear',height=3,width=15,command=lambda: keyLog('clear'))
aclear.place(x=5,y=230)

aresult=Button(topframe,text='=',height=3,width=15,command=lambda: keyLog('='))
aresult.place(x=245,y=230)



#calculation
ep =0
l1=[]
def keyLog(k):
    global ep
    if k==0 or k==1 or k==2 or k==3 or k==4 or k==5 or k==6 or k==7 or k==8 or k==9:
        ep = ep*10 + int(k)
    elif k=='+':
        l1.append(ep)
        l1.append('a')

        ep=0
    elif k=='-':
        l1.append(ep)
        l1.append('b')
        ep=0

    elif k=='/':
        l1.append(ep)
        l1.append('c')
        ep=0

    elif k=='*':
        l1.append(ep)
        l1.append('d')
        ep=0

    elif k=='clear':
        ep=0
        l1.clear()

    elif k=='=':
        l1.append(ep)
        print(l1)

        if l1[1]=='a':
            ep=l1[0]+l1[2]
            l1.clear()

        elif l1[1]=='b':          
            ep=l1[0]-l1[2]
            l1.clear()

        elif l1[1]=='c':           
            ep=l1[0]/l1[2]
            l1.clear()

        elif l1[1]=='d':
            ep=l1[0]*l1[2]
            l1.clear()

    actn.set(ep)

actn = StringVar()

Entry(topframe, textvariable=actn,width=79).place(x=3,y=20)

topframe.mainloop()
