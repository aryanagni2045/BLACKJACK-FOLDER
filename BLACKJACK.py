from tkinter import *
from PIL import Image,ImageTk
import random
root=Tk()
root.title("GAME-BlackJack")
img1=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\DEALER1.jpg"))
img2=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\PLAYER1.jpg"))
dict1={}
img2C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\2C.jpg"))
img2D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\2D.jpg"))
img2H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\2H.jpg"))
img2S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\2S.jpg"))
img3C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\3C.jpg"))
img3D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\3D.jpg"))
img3H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\3H.jpg"))
img3S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\3S.jpg"))
img4C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\4C.jpg"))
img4D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\4D.jpg"))
img4H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\4H.jpg"))
img4S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\4S.jpg"))
img5C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\5C.jpg"))
img5D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\5D.jpg"))
img5H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\5H.jpg"))
img5S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\5S.jpg"))
img6C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\6C.jpg"))
img6D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\6D.jpg"))
img6H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\6H.jpg"))
img6S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\6S.jpg"))
img7C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\7C.jpg"))
img7D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\7D.jpg"))
img7H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\7H.jpg"))
img7S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\7S.jpg"))
img8C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\8C.jpg"))
img8D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\8D.jpg"))
img8H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\8H.jpg"))
img8S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\8S.jpg"))
img9C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\9C.jpg"))
img9D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\9D.jpg"))
img9H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\9H.jpg"))
img9S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\9S.jpg"))
img10C=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\10C.jpg"))
img10D=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\10D.jpg"))
img10H=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\10H.jpg"))
img10S=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\10S.jpg"))
imgJC=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\JC.jpg"))
imgJD=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\JD.jpg"))
imgJH=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\JH.jpg"))
imgJS=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\JS.jpg"))
imgQC=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\QC.jpg"))
imgQD=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\QD.jpg"))
imgQH=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\QH.jpg"))
imgQS=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\QS.jpg"))
imgKC=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\KC.jpg"))
imgKD=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\KD.jpg"))
imgKH=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\KH.jpg"))
imgKS=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\KS.jpg"))
imgAC=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\AC.jpg"))
imgAD=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\AD.jpg"))
imgAH=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\AH.jpg"))
imgAS=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\AS.jpg"))
imglove=ImageTk.PhotoImage(Image.open(r"D:\documents\cardsp\love2.jpg"))
dict1['2C']=img2C
dict1['2D']=img2D
dict1['2H']=img2H
dict1['2S']=img2S
dict1['3C']=img3C
dict1['3D']=img3D
dict1['3H']=img3H
dict1['3S']=img3S
dict1['4C']=img4C
dict1['4D']=img4D
dict1['4H']=img4H
dict1['4S']=img4S
dict1['5C']=img5C
dict1['5D']=img5D
dict1['5H']=img5H
dict1['5S']=img5S
dict1['6C']=img6C
dict1['6D']=img6D
dict1['6H']=img6H
dict1['6S']=img6S
dict1['7C']=img7C
dict1['7D']=img7D
dict1['7H']=img7H
dict1['7S']=img7S
dict1['8C']=img8C
dict1['8D']=img8D
dict1['8H']=img8H
dict1['8S']=img8S
dict1['9C']=img9C
dict1['9D']=img9D
dict1['9H']=img9H
dict1['9S']=img9S
dict1['10C']=img10C
dict1['10D']=img10D
dict1['10H']=img10H
dict1['10S']=img10S
dict1['JC']=imgJC
dict1['JD']=imgJD
dict1['JH']=imgJH
dict1['JS']=imgJS
dict1['QC']=imgQC
dict1['QD']=imgQD
dict1['QH']=imgQH
dict1['QS']=imgQS
dict1['KC']=imgKC
dict1['KD']=imgKD
dict1['KH']=imgKH
dict1['KS']=imgKS
dict1['AC']=imgAC
dict1['AD']=imgAD
dict1['AH']=imgAH
dict1['AS']=imgAS
dict1['love']=imglove
list1=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
list2=['C','D','H','S']
l1=Label(root,height=190,width=120,image=img1)
l1.grid(row=0,column=0)
l2=Label(root,height=190,width=120,image=dict1['love'])
l2.grid(row=0,column=1)
l3=Label(root,height=190,width=120,image=dict1['love'])
l3.grid(row=0,column=2)
l4=Label(root,height=190,width=120,image=dict1['love'])
l4.grid(row=0,column=3)
l5=Label(root,height=190,width=120,image=dict1['love'])
l5.grid(row=0,column=4)
l6=Label(root,height=190,width=120,image=img2)
l6.grid(row=1,column=0)
l7=Label(root,height=190,width=120,image=dict1['love'])
l7.grid(row=1,column=1)
l8=Label(root,height=190,width=120,image=dict1['love'])
l8.grid(row=1,column=2)
l9=Label(root,height=190,width=120,image=dict1['love'])
l9.grid(row=1,column=3)
l10=Label(root,height=190,width=120,image=dict1['love'])
l10.grid(row=1,column=4)
button1=Button(root,text="BET-100")
button1.grid(row=2,column=0)
button2=Button(root,text="HIT")
button2.grid(row=2,column=1)
button3=Button(root,text="STAND")
button3.grid(row=2,column=2)
button4=Button(root,text="REFRESH")
button4.grid(row=2,column=3)
l15=Label(root,text="STATUS=NULL")
l16=Label(root,text="AMOUNT")
l15.grid(row=2,column=4)
l16.grid(row=3,column=0)
list3=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
class ab:
    def __init__(self):
        self.mainamount=0
        self.betting=0
        self.totalsum=0
        self.counter=0
        self.sent="null"
p=ab()
d=ab()
x=int(input("enter the total amount for player ="))
p.mainamount=x
l16['text']="AMOUNT={}".format(x)
def hitd():
    if p.betting!=0:
        while d.totalsum<=17 and d.counter<4:
            sent2=random.choice(list1)
            sent2+=random.choice(list2)
            if sent2[0]=='K' or sent2[0]=='J' or sent2[0]=='Q':
                d.totalsum+=10
            elif sent2[0]=='A':
                if d.totalsum<=10:
                    d.totalsum+=11
                else :
                    d.totalsum+=1
            elif len(sent2)==3:
                d.totalsum+=10
            else:
                d.totalsum+=int(sent2[0])
            print("dealer total sum is",d.totalsum)
            d.counter+=1
            list3[d.counter]['image']=dict1[sent2]
    else :
        pass
def hit():
    if p.betting!=0:
        if p.counter<4 and p.totalsum<=21:
            sent2=random.choice(list1)
            sent2+=random.choice(list2)
            if sent2[0]=='K' or sent2[0]=='Q' or sent2[0]=='J':
                p.totalsum+=10
            elif sent2[0]=='A':
                if p.totalsum<=10:
                    p.totalsum+=11
                else:
                    p.totalsum+=1
            elif len(sent2)==3:
                p.totalsum+=10
            else:
                p.totalsum+=int(sent2[0])
            print("player total sum ",p.totalsum)
            p.counter+=1
            list3[5+p.counter]['image']=dict1[sent2]
    else: pass

def bett():
    if d.totalsum==0:
        if p.mainamount>=100:
            p.mainamount-=100
            p.betting=100
            l16['text']="AMOUNT ={}".format(p.mainamount)
            hitd()
    else:
        pass
def stand():
    if d.totalsum>21:
        p.mainamount+=2*(p.betting)
        p.betting=0
        l15['text']="YOU WON !!!"
        l16['text']="AMOUNT={}".format(p.mainamount)
    else :
        if p.totalsum>21:
            p.betting=0
            l15['text']="YOU LOOSE !!!"
        else :
            if p.totalsum>d.totalsum:
                p.mainamount+=2*(p.betting)
                p.betting=0
                l15['text']="YOU WON !!!"
                l16['text']="AMOUNT={}".format(p.mainamount)
            elif p.totalsum<d.totalsum:
                p.betting=0
                l15['text']="YOU LOOSE !!!"
            else :
                p.mainamount+=p.betting
                p.betting=0
                l15['text']="DRAW !!!"
def refresh():
    p.betting=0
    p.totalsum=0
    p.counter=0
    p.sent="null"
    d.totalsum=0
    d.counter=0
    d.sent="null"
    l2['image']=dict1['love']
    l3['image']=dict1['love']
    l4['image']=dict1['love']
    l5['image']=dict1['love']
    l7['image']=dict1['love']
    l8['image']=dict1['love']
    l9['image']=dict1['love']
    l10['image']=dict1['love']
    l15['text']="null"
button1['command']=bett
button2['command']=hit
button3['command']=stand
button4['command']=refresh
root.mainloop()
