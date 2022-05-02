from tkinter import *

root = Tk()
root.title("CSUMB APP")
root.geometry("450x500")
root.config(bg="red")

def extract_data():
    print(textbox.get('1.0', 'end'))

message = '''
Hello everyone,
My dog loves running around
he is a good dog
he is getting old
but he still like going out
12
22


333
22
233

stuff here
stuff there
stuff everywhere

you know
'''

frame = Frame(root)

textbox = Text(frame, height=15, width=30, wrap='word')
textbox.pack(side = LEFT, expand=True)
textbox.insert("end", message)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH, pady=1)

textbox.config(yscrollcommand=sb.set)
sb.config(command= textbox.yview)
frame.pack(expand=True)



root.mainloop()