import tkinter as tk
from tkinter.filedialog import askopenfilename

def matrix_action(number):
    # wszystkie dzialania na macierzach
    # funkcja edytuje GUI w tkinter

    # 1. czyszczenie okienka

    # 2. dzialania na macierzach


def button_1_action(text):
    # możesz wybrać takie i takie
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # do wczytywania plików zewnetrznych
    filename = askopenfilename(
        title ='Open a file',
        # initial folder z którego użytkownikowi wolno wybrać pliki
        initialdir ='/',
        filetypes = filetypes)
    with open(filename, 'r') as f:
        for line in f:
            text.insert(tk.END, line + '\n')    # tk.END pokazuje gdzie ma być kursor

def button_2_action(text):
    # możesz wybrać takie i takie
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # do wczytywania plików zewnetrznych
    filename = askopenfilename(
        title ='Open a file',
        # initial folder z którego użytkownikowi wolno wybrać pliki
        initialdir ='/',
        filetypes = filetypes)
    with open(filename, 'r') as f:
        for line in f:
            text.insert(tk.END, line + '\n')    # tk.END pokazuje gdzie ma być kursor


def open_file(text):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = filetypes)
    with open(filename, 'r') as f:
        for line in f:
            text.insert(tk.END, line + '\n')

# to do
# [] sprawdź jak wyłączyć pisanie w polu tekstowym tkinter
if __name__ == "__main__":
    # obiekt klasy TK
    window = tk.Tk()
    window.title('Twoj Stary 123 apka')
    window.geometry('500x500')

    frame_1 = tk.Frame(master=window, width=200, height=100, bg='blue')
    label_1 = tk.Label(master=frame_1, text="Testowa labelka.", font=30, fg='red')
    label_1.pack()

    frame_2 = tk.Frame(master=window, width='200', height='20', bg='yellow')
    label_2 = tk.Label(master=frame_2, text="labelka w drugiej ramce", font='20', fg='black')
    label_2.pack()

    text = tk.Text(master=frame_2, width=80, height=15)
    text.pack()

    # PRZYCISKI
    button_1 = tk.Button(master=frame_1, text="wczytaj plik", width=20)
    button_1.pack()
    button_1.config(command=lambda: button_1_action(text))
    button_1.config(command=lambda:nazwa_funkcji(9, text))

    button_2 = tk.Button(master=frame_1, text="1", width=20)
    button_2.pack()
    button_2.config(command=lambda: button_2_action(text))
    button_2.config(command=lambda:nazwa_funkcji(9, text))



    menubar = tk.Menu(master=window)
    filemenu = tk.Menu(master=menubar, tearoff=0)
    filemenu.add_command(label='Open', command=lambda: open_file(text))
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    menubar.add_cascade(label='File', menu=filemenu)

    frame_1.pack(fill=tk.BOTH, expand=True)
    frame_2.pack(fill=tk.BOTH, expand=True)
    window.config(menu=menubar)
    window.mainloop()
