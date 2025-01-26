from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root = Tk()
root.geometry('1080x400')

root.resizable(0,0)
root.config(bg = 'lightpink')
root.title("SayHello")

Label(root, text = "SayHello", font = "arial 20 bold", width = 10, fg = 'white' ,bg='teal').pack()

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)

Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x =  600 , y = 100)

Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Output_text.place(x=30,y = 100)



language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =25)
src_lang.place(x=20,y=60)
src_lang.set('Choose input language')

dest_lang = ttk.Combobox(root, values= language, width =25)
dest_lang.place(x=800,y=70)
dest_lang.set('Choose output language')
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'lavender', activebackground = 'sky blue')

trans_btn.place(x = 490, y= 300 )
root.mainloop()

