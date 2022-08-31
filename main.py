 #script principal
from mainFrame import DataEquipo
from tkinter import Tk

def main():
    root = Tk()
    root.wm_title("sensores con arduino")
    app = DataEquipo(root)
    app.mainloop()
    
if __name__=="__main__":
    main()