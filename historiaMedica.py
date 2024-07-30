import tkinter as tk
from paciente.gui import Frame
def main():
    root = tk.Tk()
    root.title('REGISTROS MÉDICOS BETTERLAND v1.0')
    root.resizable(0,0)
    root.iconbitmap('img/logo-circular.ico')
    frame = Frame(root)
    frame.mainloop()

if __name__ == '__main__':
    main()