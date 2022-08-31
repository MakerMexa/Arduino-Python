#tkinter
from tkinter import *
#libreria de hilos
import threading

#comunicacion serial con arduino
import serial
import time

class DataEquipo(Frame):
    db_name = 'BDIot.db'
       
#Constructor de la app y VENTANA PRINCIPAL
    def __init__(self, master= None):        
        super().__init__(master, width=420, height=270)    
    #inicializacion de puerto arduino    
        self.serialArduino = serial.Serial("COM3", 9600)
        time.sleep(1)           
        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.askQuit)
        self.pack()
    #hilo comunicacion serial arduino
        self.hilo1 = threading.Thread(target=self.getSensorValues, daemon=True)
        self.val_temp = StringVar()
        self.val_humedad = StringVar()
        #self.Fecha = StringVar() 
        self.create_widgets()
        self.isRun=True
        self.hilo1.start()
    
    def askQuit(self):
        self.isRun=False
        self.serialArduino.close()
        self.hilo1.join(0.1)
        self.master.quit()
        self.master.destroy()
        print("Cerrando App...........")
         
#conexion serial arduino
    def getSensorValues(self):   
        while self.isRun:
          cad = self.serialArduino.readline().decode('ascii').strip()
          if cad:
              pos=cad.index(":")
              label=cad[:pos]
              value=cad[pos+1:]
              if label == 'Temp':
                  self.val_temp.set(value)         
              if label == 'Humedad':
                  self.val_humedad.set(value)
                    


    #elementos de la ventana de lectura
    def create_widgets(self):
        Label(self, text="Temp: ").place(x=30, y=20)
        Label(self, width=6, textvariable=self.val_temp).place(x=120, y=20)
        Label(self, text="Humedad: ").place(x=30, y=50)
        Label(self, width=6, textvariable=self.val_humedad).place(x=120, y=50)

    