import tkinter
from tkinter import *
from tkinter import ttk

#Definindo as cores da interface

cor0 = "#FFFFFF"  # branca 
cor1 = "#333333"  # preta pesado 
cor2 = "#fcc058"  # laranja 
cor3 = "#38576b"  # valor 
cor4 = "#3297a8"   # azul 
cor5 = "#fff873"   # amarela 
cor6 = "#fcc058"  # laranja 
cor7 = "#e85151"   # vermelha
cor8 = cor4   # + verde
cor10 ="#fcfbf7"
fundo = "#000000" # preta 

#Cria janela principal

janela = Tk()
janela.title('')
janela.geometry('280x400')
janela.configure(bg=fundo)

#Criando dois frames o de cima e de baixo

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0,column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=260, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1,column=0, sticky=NW)

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0,column=0, sticky=NW, padx=10, pady=10)

#Configurando frame de cima LADO DO X
app_x = Label(frame_cima, text='X', height=1, relief='flat',anchor='center', font=('Fixedsys 40 bold'), bg=cor1, fg=cor7)
app_x.place(x=27, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat',anchor='center', font=('Fixedsys 7 bold'), bg=cor1, fg=cor0)
app_x.place(x=15, y=65)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat',anchor='center', font=('Fixedsys 30 bold'), bg=cor1, fg=cor0)
app_x_pontos.place(x=80, y=20)

#Separador ":"
app_o = Label(frame_cima, text=':', height=1, relief='flat',anchor='center', font=('Fixedsys 25 bold'), bg=cor1, fg=cor0)
app_o.place(x=108, y=15)

#Configurando frame de cima LADO DO O
app_o = Label(frame_cima, text='O', height=1, relief='flat',anchor='center', font=('Fixedsys 40 bold'), bg=cor1, fg=cor4)
app_o.place(x=187, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat',anchor='center', font=('Fixedsys 7 bold'), bg=cor1, fg=cor0)
app_o.place(x=167, y=65)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat',anchor='center', font=('Fixedsys 30 bold'), bg=cor1, fg=cor0)
app_o_pontos.place(x=132, y=20)

#Configurando frame de baixo
#Linhas Verticais
app_= Label(frame_baixo, text='', height=15, width=2, relief='flat',pady=5, anchor='center', font=('Fixedsys 4 bold'), bg=cor0, fg=cor7)
app_.place(x=91, y=0)
app_= Label(frame_baixo, text='', height=15,width=2, relief='flat',pady=5, anchor='center', font=('Fixedsys 4 bold'), bg=cor0, fg=cor7)
app_.place(x=177, y=0)

#Linhas horizontal
app_= Label(frame_baixo, text='  ', width=203, height=1, relief='flat',padx=2, pady=1, anchor='center', font=('Fixedsys 1 bold'), bg=cor0, fg=cor7)
app_.place(x=30, y=70)
app_= Label(frame_baixo, text='  ', width=203, height=1, relief='flat',padx=2, pady=1, anchor='center', font=('Fixedsys 1 bold'), bg=cor0, fg=cor7)
app_.place(x=30, y=153) 

#Linha 0 
b_0= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_0.place(x=28, y=9)

b_1= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_1.place(x=115, y=10)

b_2= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_2.place(x=202, y=10)

#Linha 1
b_0= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_0.place(x=28, y=95)

b_1= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_1.place(x=115, y=95)

b_2= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_2.place(x=202, y=95)

#Linha 2
b_0= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_0.place(x=28, y=180)

b_1= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_1.place(x=115, y=180)

b_2= Button(frame_baixo, text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
b_2.place(x=202, y=180)

#Botão jogar
b_jogar= Button(frame_baixo, text='Jogar', width=10, font=('Fixedsys 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=cor0)
b_jogar.place(x=95, y=250)


janela.mainloop()