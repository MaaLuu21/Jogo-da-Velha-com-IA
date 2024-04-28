import tkinter
from tkinter import *
from tkinter import ttk

#Definindo as cores da interface

cor0 = "#FFFFFF"  # branca 
cor1 = "#333333"  # preta pesado 
cor2 = "#00FF00"  # laranja 
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




#Logica
#Variaveis
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']] #3 listas, cada uma representa uma linha do jogo


jogando = 'X'
joga =''
contador = 0
contador_de_rodada = 0

def iniciar_jogo():
    b_jogar.place(x=800, y=300)
    #Controla o jogo
    def controlar(i):
            global jogando #qual jogador esta jogando no momento
            global contador  #conta o estado atual
            global jogar #quem sera o proximo a jogar



            #Comparar o valor recebido de i (i é o index e cada quadrado do jogo da velha)
            if i==str(1):#1
                    
                    #compara se a posição esta ocupada
                    if b_0['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_0['fg'] = cor         
                            b_0['text'] = jogando
                            tabela[0][0]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1                             
            if i==str(2):#2
                    #compara se a posição esta ocupada
                    if b_1['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_1['fg'] = cor         
                            b_1['text'] = jogando
                            tabela[0][1]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(3):#3
                    #compara se a posição esta ocupada
                    if b_2['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_2['fg'] = cor         
                            b_2['text'] = jogando
                            tabela[0][2]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(4):#4
                    #compara se a posição esta ocupada
                    if b_3['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_3['fg'] = cor         
                            b_3['text'] = jogando
                            tabela[1][0]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(5):#5
                    #compara se a posição esta ocupada
                    if b_4['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_4['fg'] = cor         
                            b_4['text'] = jogando
                            tabela[1][1]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(6):#6
                    #compara se a posição esta ocupada
                    if b_5['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_5['fg'] = cor         
                            b_5['text'] = jogando
                            tabela[1][2]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(7):#7
                    #compara se a posição esta ocupada
                    if b_6['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_6['fg'] = cor         
                            b_6['text'] = jogando
                            tabela[2][0]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(8):#7
                    #compara se a posição esta ocupada
                    if b_7['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_7['fg'] = cor         
                            b_7['text'] = jogando
                            tabela[2][1]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1
            if i==str(9):#9
                    #compara se a posição esta ocupada
                    if b_8['text']=='':
                            #Vereficando de quem é a vez e defini o simbolo e a cor
                            if jogando =='X':
                                cor=cor7
                            if jogando =='O':
                                    cor=cor8

                            # Defini a cor do texto do botão e marca a posição escolhida atual
                            b_8['fg'] = cor         
                            b_8['text'] = jogando
                            tabela[2][2]= jogando#primeira lista 0 posição 0

                            #Verifica quem está jogando X ou O para trocar de jogador
                            if jogando == 'X':
                                    jogando = 'O'
                                    joga = 'Jodador 1'
                            else:
                                    jogando = 'X'
                                    joga = 'Jodador 2'

                            #utilizando o contador para avançar para a proxima rodada
                            contador +=1

            #Quando contador for maior ou igual a 5
            #verefica se já há algum vencedor
            if contador>=5:
                #linhas
                if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                    vencedor(jogando)
                elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                    vencedor(jogando)
                elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                    vencedor(jogando)
                
                #colunas                                   
                if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                    vencedor(jogando)
                elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                    vencedor(jogando)

                #diagonais                                 
                if tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                    vencedor(jogando)

                #empate
                if contador >=9:
                        vencedor('Empate')

    
    #Decide o vencedor
    def vencedor(i):
            global score_1
            global score_2  
            global tabela
            global contador_de_rodada
            global contador


            #Desativa os botões
            b_0['state']='disable'
            b_1['state']='disable'
            b_2['state']='disable'
            b_3['state']='disable'
            b_4['state']='disable'
            b_5['state']='disable'
            b_6['state']='disable'
            b_7['state']='disable'
            b_8['state']='disable'

            app_vencedor= Label(frame_baixo, text='', width=18, relief='flat',pady=5, anchor='center', font=('Fixedsys 15 bold'), bg=cor1, fg=cor2)
            app_vencedor.place(x=55, y=200)


            if i == 'X':
                    score_1+=1
                    app_vencedor['text'] = 'Jogador 2 venceu !'
                    app_o_pontos['text'] = score_1

            if i == 'O':
                    score_2+=1
                    app_vencedor['text'] = 'Jogador 1 venceu !'
                    app_x_pontos['text'] = score_2

            if i == 'Empate':
                    app_vencedor['text'] = 'Empate'

            
                #Retorna os botões a condição normal
            def start():
                #Limpa a tela  quando a rodada acaba
                b_0['text']=''
                b_1['text']=''
                b_2['text']=''
                b_3['text']=''
                b_4['text']=''
                b_5['text']=''
                b_6['text']=''
                b_7['text']=''
                b_8['text']=''

                b_0['state']='normal'
                b_1['state']='normal'
                b_2['state']='normal'
                b_3['state']='normal'
                b_4['state']='normal'
                b_5['state']='normal'
                b_6['state']='normal'
                b_7['state']='normal'
                b_8['state']='normal'

                tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']]
                app_vencedor.destroy()
                b_jogar.destroy()
    
            #Botão jogar
            b_jogar= Button(frame_baixo, command=start, text='Jogar de novo', width=13, font=('Fixedsys 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=cor0)
            b_jogar.place(x=80, y=250)

            #Remove os botões de jogar e vencedor
            def jogo_acabou():
                    b_jogar.destroy()
                    app_vencedor.destroy()

                    terminar()

            if contador_de_rodada>=2:
                    jogo_acabou()
            else:
                    contador_de_rodada+=1
                    #reiniciando a tabela
                    tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']]
                    contador = 0
    
    #Terminar o jogo
    def terminar():
            global tabela
            global contador_de_rodada
            global score_1
            global score_2
            global contador


            tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']]#inicia a tabela na forma inicial
            contador_de_rodada = 0 #zera o contador
            score_1 = 0 
            score_2 = 0
            contador = 0

            b_0['state']='disable'
            b_1['state']='disable'
            b_2['state']='disable'
            b_3['state']='disable'
            b_4['state']='disable'
            b_5['state']='disable'
            b_6['state']='disable'
            b_7['state']='disable'
            b_8['state']='disable'

            app_fim= Label(frame_baixo, text='JOGO ACABOU', relief='flat',pady=5, anchor='center', font=('Fixedsys 15 bold'), bg=cor1, fg=cor2)
            app_fim.place(x=93, y=130)

            #Jogar de novo
            def jogar_denovo():
                app_x_pontos['text'] = '0'#########
                app_o_pontos['text'] = '0'#####
                app_fim.destroy()
                b_jogar.destroy()

                #Chama função iniciar jogo
                iniciar_jogo()

            b_jogar= Button(frame_baixo, command=jogar_denovo, text='Jogar', width=10, font=('Fixedsys 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=cor0)
            b_jogar.place(x=95, y=250)


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

    #Quadrados do jogo da velha i

    #Linha 0 
    b_0= Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_0.place(x=28, y=9)

    b_1= Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_1.place(x=115, y=10)

    b_2= Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_2.place(x=202, y=10)

    #Linha 1
    b_3= Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_3.place(x=28, y=95)

    b_4= Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_4.place(x=115, y=95)

    b_5= Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_5.place(x=202, y=95)

    #Linha 2
    b_6= Button(frame_baixo,command=lambda:controlar('7'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_6.place(x=28, y=180)

    b_7= Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_7.place(x=115, y=180)

    b_8= Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, font=('Fixedsys 18 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=cor7)
    b_8.place(x=202, y=180)

#Botão jogar
b_jogar= Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, font=('Fixedsys 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=cor0)
b_jogar.place(x=95, y=250)


#Logica
#Variaveis
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']] #3 listas, cada uma representa uma linha do jogo


janela.mainloop()