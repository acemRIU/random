import tkinter
import tkinter as tk
from tkinter import Tk,Label
from PIL import Image,ImageTk
from PIL import *
import requests
import matplotlib.pyplot as plt
import tkinter.font as font
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

#root window
root = tkinter.Tk()
root.title('Bitcoin')
root.configure(width = 800,height = 460)

#canvas
canvas = tk.Canvas(root)
canvas.configure(bg ='black')
canvas.place(relwidth =1,relheight=1)

#image
imag = ImageTk.PhotoImage(file ='bitcoin.png')
image_label = Label(canvas,image = imag)
image_label.place(relwidth=1,relheight=1)

#format function
def format(response):
    try:
        btc = response['BTC']
    except:
        final_str = 'There was an error'
    final_str = 'BTC: %s'%(btc)
    return(final_str)
def Nepal(response):
    us = response['USD']
    nep = (117.22)*us
    final = 'NRs: %s'%nep

    return(final)

#tracker function
def tracker():
    global canvas
    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR'
    response = requests.get(url).json()
    frame2 = Label(canvas,text = format(response),font=('arial',15,'bold'))
    frame2.place(relx=0.05, rely=0.4, relheight=0.1, relwidth=0.2)
    frame3 =Label(canvas,text = Nepal(response),font=('arial',15,'bold'))
    frame3.place(relx=0.05, rely=0.55, relheight=0.1, relwidth=0.32)
    time = datetime.now().strftime('%H:%M:%S')
    frame4 = Label(canvas, text='Updated at: %s' % (time), font=('arial', 15, 'bold'))
    frame4.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.32)
    frame5 = tk.Frame(canvas)
    frame5.place(relx=0.65, rely=0.3, relheight=0.5, relwidth=0.3)

    data = {'Value':[response['BTC']]}
    df = DataFrame(data,columns = response['BTC'])

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure,frame5)
    chart_type.get_tk_widget().pack()
    df = df[['Value']].groupby('Value').sum()
    df.plot(kind='line', legend=True, ax=ax)
    ax.set_title('Bitcoin')

    # graph = plt.plot(time,response['BTC'])
    # graph.place(frame5)


    # label1 = Label(canvas,text = format(response),font = ('Arial',15,'bold'))
    # label1.place(relx = 0.05,rely=0.3,relheight=0.2,relwidth=0.2)

#frame1
frame1 = tk.Frame(canvas)
frame1.place(relx = 0.35,rely=0.1,relheight=0.1,relwidth=0.25)
btn = tk.Button(frame1,text ='Start',font =('Arial',25,'bold'),bd = 5,command = tracker)
btn.place(relheight=1,relwidth=1)

# #frame2


root.mainloop()
