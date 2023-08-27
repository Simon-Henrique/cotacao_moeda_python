import requests
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image

def pegar_cotacao():
    requesicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    API = requesicao.json()

    dolar= API['USDBRL']['bid']
    euro = API['EURBRL']['bid']
    bitcoin = API['BTCBRL']['bid']
    data = datetime.now()
    data_formatada = str(data)
    dolar_formatado = float(dolar)
    euro_formatado = float(euro)
    bitcoin_formatado = float(bitcoin)
    texto = f'''
            Valor do Dolar: R$ {dolar_formatado:.2f}
            Valor do Euro: R$ {euro_formatado:.2f}
            Valor do Bitcoin: R$ {bitcoin_formatado:,.2f}

            Consulta feita em: {data_formatada[:19]}
            '''
    
    resultado['text'] = texto


janela = Tk()
janela.title('Cotação Moeda')
janela.geometry('280x350')
#-----------------------teste de imagem
frame = Frame(janela, width=10, height=10)
frame.pack()
frame.place(anchor=CENTER, relx=0.5, rely=0.7)
imagem = ImageTk.PhotoImage(Image.open('money.png'))
image_label = Label(frame, image=imagem)
image_label.pack()
#----------------------
titulo = Label(janela, text='Cotação atual das moedas')
titulo.grid(column=0, row=2, padx=70, pady=20, columnspan=3)
botao = Button(janela, text='Gerar informação', command=pegar_cotacao,)
botao.grid(column=0, row=3, padx=10, pady=1, columnspan=3)
resultado = Label(janela, text='', justify=LEFT)
resultado.grid(column=0, row=4, padx=15, pady=10, columnspan=3,)
janela.mainloop()

