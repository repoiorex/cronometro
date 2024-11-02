import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        
        # Establecer la ventana siempre en primer plano
        self.root.attributes('-topmost', True)

        # Configurar tamaño de la ventana (ancho x alto)
        self.root.geometry("250x150")  # Ajustar según la fuente y el tamaño

        self.tempo = 0
        self.corriendo = False

        self.label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.label.pack()

        self.boton_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar)
        self.boton_iniciar.pack()

        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack()

        self.actualizar()

    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.contar()

    def contar(self):
        if self.corriendo:
            self.tempo += 1
            self.actualizar()
            self.root.after(1000, self.contar)

    def reiniciar(self):
        self.tempo = 0
        self.corriendo = False
        self.actualizar()

    def actualizar(self):
        minutos, segundos = divmod(self.tempo, 60)
        self.label.config(text=f"{minutos:02}:{segundos:02}")

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
