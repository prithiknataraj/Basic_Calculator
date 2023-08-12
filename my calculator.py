from tkinter import *
from math import*

root=Tk()
bodmas=['+','-','*','/','%']

def operation():
    
    num3=e.get()
    
    for i in num3:
        
        if i in bodmas:
            sym=i
            n1,n2=num3.split(i)
            break
        
    if sym=='+':
        
        if '.' in n1 or '.' in n2:
            s=float(n1)+float(n2)
            
        else:
            s=int(n1)+int(n2)
            
    elif sym=='-':

        if '.' in n1 or '.' in n2:
            s=float(n1)-float(n2)

        else:
            s=int(n1)-int(n2)

    elif sym=='*':

        if '.' in n1 or '.' in n2:
            s=float(n1)*float(n2)

        else:
            s=int(n1)*int(n2)

    elif sym=='/':
        s=float(n1)/float(n2)

    elif sym=='%':
        
        if '.' in n1 or '.' in n2:
            s=float(n1)%float(n2)
            
        else:
            s=int(n1)%int(n2)
            
    e.delete(0,END)
    e.insert(0,s)

def click(num):
    num2=e.get()

    if num=='=':
        if num2=='' or num2.isdigit():
            e.insert(0,'')
        else:
            operation()
    
    elif num!='clear' and num!='remove':
            
        e.delete(0,END)
        e.insert(0,str(num2)+str(num))
        
    elif num=='clear':
        e.delete(0,END)
        
    elif num=='remove':
        e.delete(len(str(num2))-1,END)
                    
e=Entry(root,width=30,borderwidth=5)

e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

b0=Button(root,text="0",padx=60,pady=25,bg="white",command=lambda:click(0))
b1=Button(root,text="1",padx=25,pady=25,bg="white",command=lambda:click(1))
b2=Button(root,text="2",padx=25,pady=25,bg="white",command=lambda:click(2))
b3=Button(root,text="3",padx=25,pady=25,bg="white",command=lambda:click(3))
b4=Button(root,text="4",padx=25,pady=25,bg="white",command=lambda:click(4))
b5=Button(root,text="5",padx=25,pady=25,bg="white",command=lambda:click(5))
b6=Button(root,text="6",padx=25,pady=25,bg="white",command=lambda:click(6))
b7=Button(root,text="7",padx=25,pady=25,bg="white",command=lambda:click(7))
b8=Button(root,text="8",padx=25,pady=25,bg="white",command=lambda:click(8))
b9=Button(root,text="9",padx=25,pady=25,bg="white",command=lambda:click(9))

bp=Button(root,text=".",padx=26.49,pady=25,bg="white",command=lambda:click('.'))
br=Button(root,text="remove",fg="red",padx=10,pady=25,command=lambda:click('remove'))
be=Button(root,text="=",padx=26,pady=25,fg="green",command=lambda:click('='))
ba=Button(root,text="+",padx=26,pady=60,fg="blue",command=lambda:click('+'))
bs=Button(root,text="-",padx=27.4,pady=25,fg="blue",command=lambda:click('-'))
bm=Button(root,text="*",padx=26,pady=25,fg="blue",command=lambda:click('*'))
bd=Button(root,text="/",padx=26,pady=25,fg="blue",command=lambda:click('/'))
bmd=Button(root,text="%",padx=23,pady=25,fg="blue",command=lambda:click('%'))

bc=Button(root,text="clear",fg="red",bg="white",padx=10,pady=10,command=lambda:click('clear'))

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

b0.grid(row=5,column=0,columnspan=2)

bp.grid(row=5,column=2)
br.grid(row=5,column=3)
be.grid(row=4,column=3)
ba.grid(row=2,column=3,rowspan=2)
bs.grid(row=1,column=3)
bm.grid(row=1,column=2)
bd.grid(row=1,column=1)
bmd.grid(row=1,column=0)
bc.grid(row=0,column=3)

root.title("SIMPLE CALCULATOR")
root.mainloop()
