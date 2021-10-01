#importing modules
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
proton = Tk()
proton.title('Zeb-Sat')

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

# opening a file
def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
# save as feature
def save_as():
    '''it will ask us to choose the file location and file extention similar to when we save a file in notepad'''
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def execute():
    '''This function checks the file path and if the file path is black then it will execute the Toplevel() then it will prompt to save the file'''
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code, before executing it')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

menu_bar = Menu(proton) # creating the menu bar

#menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

#run
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Execute', command=execute) #It will run the execute function.
menu_bar.add_cascade(label='Execute', menu=run_bar) 



#configuration
proton.config(menu=menu_bar)

#initialisations
editor = Text()
editor.pack()

code_output = Text(height=8)
code_output.pack()



proton.mainloop() #The window will remain open because of the mainloop till we manually exit the program.
=======
#execution
proton.mainloop()
