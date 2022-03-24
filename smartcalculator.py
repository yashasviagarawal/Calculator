from tkinter import *
screen = Tk()
screen.title("Calculator")
screen.iconbitmap('calculator.ico')
screen.geometry("240x305")

def click(number):
    global operator
    operator += str(number)
    num.set(operator)

def clear():
    global operator
    operator = ''
    num.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator = str(result)
    num.set(result)


num = StringVar()
operator = ''
entry1 = Entry(screen, bg = 'white',font=('arial',15,'italic bold'),bd=10, justify='right',textvariable=num)

entry1.grid(row=0,column=0,columnspan=4)

btn1 = Button(screen,text = "1",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(1), activebackground='white', activeforeground='red')
btn2 = Button(screen,text = "2",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(2), activebackground='white', activeforeground='red')
btn3 = Button(screen,text = "3",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(3), activebackground='white', activeforeground='red')
btn4 = Button(screen,text = "4",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(4), activebackground='white', activeforeground='red')
btn5 = Button(screen,text = "5",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(5), activebackground='white', activeforeground='red')
btn6 = Button(screen,text = "6",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(6), activebackground='white', activeforeground='red')
btn7 = Button(screen,text = "7",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(7), activebackground='white', activeforeground='red')
btn8 = Button(screen,text = "8",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(8), activebackground='white', activeforeground='red')
btn9 = Button(screen,text = "9",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(9), activebackground='white', activeforeground='red')
btnadd = Button(screen,text = "+",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click('+'), activebackground='white', activeforeground='red')
btnmin = Button(screen,text = "-",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click('-'), activebackground='white', activeforeground='red')
btndiv = Button(screen,text = "/",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click('/'), activebackground='white', activeforeground='red')
btnmul = Button(screen,text = "x",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click('*'), activebackground='white', activeforeground='red')
btn0 = Button(screen,text = "0",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:click(0), activebackground='white', activeforeground='red')
btncan = Button(screen,text = "C",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:clear(), activebackground='white', activeforeground='red')
btnequal = Button(screen,text = "=",bg="light blue", font=("arial",15),bd=10,padx = 8,pady = 5, command=lambda:equal(), activebackground='white', activeforeground='red')

btnadd.grid(row=1,column=3)
btnmin.grid(row=2,column=3)
btndiv.grid(row=3,column=3)
btnmul.grid(row=4,column=3)
btn0.grid(row=4,column=0)
btncan.grid(row=4,column=2)
btnequal.grid(row=4,column=1)
btn9.grid(row=1,column=2)
btn8.grid(row=1,column=1)
btn7.grid(row=1,column=0)
btn6.grid(row=2,column=2)
btn5.grid(row=2,column=1)
btn4.grid(row=2,column=0)
btn3.grid(row=3,column=2)
btn2.grid(row=3,column=1)
btn1.grid(row=3,column=0)


screen.mainloop()