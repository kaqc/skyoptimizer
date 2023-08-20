import qrcode
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('QR Generator | Version 1.0.0')
ws.geometry('400x200')
ws.config(bg='#18191a')


def generate():
    img = qrcode.make(msg.get())
    type(img) 
    img.save(f'{save_name.get()}.png')
    Label(ws, text='File Saved!', fg='green').pack()

frame = Frame(ws, bg='#242526')
frame.pack(expand=True)

Label(
    frame,
    text='Text/URL',
    font = ('Comic Sans MS', 18),
    bg='#242526'
    ).grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

Label(
    frame,
    text='File Name',
    font = ('Comic Sans MS', 18),
    bg='#242526',
).grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

btn = Button(
    ws, 
    text='Generate QR Code.',
    command=generate
    )
btn.pack()

ws.mainloop()