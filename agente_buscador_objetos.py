import tkinter as tk
import random
import time
import threading

class AgenteBuscador:
    def __init__(self, size=20):
        self.size = size
        self.grid = [["⬜" for _ in range(size)] for _ in range(size)]
        self.pos_x, self.pos_y = 0, 0
        self.obj_x, self.obj_y = random.randint(0, size-1), random.randint(0, size-1)
        self.grid[self.obj_x][self.obj_y] = "🎯"
        self.prev_x, self.prev_y = self.pos_x, self.pos_y  

    def reiniciar(self):
        """Reinicia la posición del agente y el objetivo."""
        self.pos_x, self.pos_y = 0, 0
        self.obj_x, self.obj_y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        self.grid = [["⬜" for _ in range(self.size)] for _ in range(self.size)]
        self.grid[self.obj_x][self.obj_y] = "🎯"
        self.prev_x, self.prev_y = self.pos_x, self.pos_y  

    def mover(self):
        """Mueve al agente hacia el objetivo."""
        if self.pos_x < self.obj_x:
            self.pos_x += 1
        elif self.pos_x > self.obj_x:
            self.pos_x -= 1
        elif self.pos_y < self.obj_y:
            self.pos_y += 1
        elif self.pos_y > self.obj_y:
            self.pos_y -= 1

    def ejecutar(self, canvas, cell_size, label_mensaje):
        """Ejecuta la búsqueda y actualiza la interfaz."""
        while (self.pos_x, self.pos_y) != (self.obj_x, self.obj_y):

            self.actualizar_interfaz(canvas, cell_size)
            self.mover()
            time.sleep(0.2) 
            canvas.update() 
        
        label_mensaje.config(text="¡Objeto encontrado! 🎉", fg="green")

    def actualizar_interfaz(self, canvas, cell_size):
        """Actualiza solo las celdas que cambian en el Canvas."""

        x0_prev, y0_prev = self.prev_y * cell_size, self.prev_x * cell_size
        x1_prev, y1_prev = x0_prev + cell_size, y0_prev + cell_size
        canvas.create_rectangle(x0_prev, y0_prev, x1_prev, y1_prev, outline="black", fill="white")
        canvas.create_text((x0_prev + x1_prev) // 2, (y0_prev + y1_prev) // 2, text="⬜", font=("Arial", 12))

        x0_new, y0_new = self.pos_y * cell_size, self.pos_x * cell_size
        x1_new, y1_new = x0_new + cell_size, y0_new + cell_size
        canvas.create_rectangle(x0_new, y0_new, x1_new, y1_new, outline="black", fill="white")
        canvas.create_text((x0_new + x1_new) // 2, (y0_new + y1_new) // 2, text="🤖", font=("Arial", 12))
        if (self.pos_x, self.pos_y) == (self.obj_x, self.obj_y):
            canvas.create_text((x0_new + x1_new) // 2, (y0_new + y1_new) // 2, text="🎯", font=("Arial", 12))

        self.prev_x, self.prev_y = self.pos_x, self.pos_y


class AplicacionBuscador:
    def __init__(self, root, size=20, cell_size=40):  
        self.root = root
        self.root.title("Agente Buscador 🤖")

        self.size = size
        self.cell_size = cell_size
        
        self.agente = AgenteBuscador(size)
        
        self.ancho_ventana = self.size * self.cell_size + 150 
        self.alto_ventana = self.size * self.cell_size + 200  
        self.root.geometry(f"{self.ancho_ventana}x{self.alto_ventana}")
        
        self.root.resizable(True, True)

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_principal, width=self.size * self.cell_size, height=self.size * self.cell_size, bg="white")
        self.canvas.pack(pady=20)
        
        self.dibujar_cuadricula()
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(fill=tk.X, padx=20, pady=10)

        self.label_mensaje = tk.Label(self.frame_controles, text="", font=("Arial", 14))
        self.label_mensaje.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        self.boton_iniciar = tk.Button(self.frame_controles, text="Iniciar Búsqueda", command=self.iniciar_busqueda, font=("Arial", 12))
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)
        
        self.boton_reiniciar = tk.Button(self.frame_controles, text="Reiniciar Búsqueda", command=self.reiniciar_busqueda, font=("Arial", 12))
        self.boton_reiniciar.pack(side=tk.LEFT)
    
    def dibujar_cuadricula(self):
        """Dibuja la cuadrícula inicial en el Canvas."""
        for i in range(self.size):
            for j in range(self.size):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                if (i, j) == (self.agente.obj_x, self.agente.obj_y):
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="🎯", font=("Arial", 12))
                elif (i, j) == (self.agente.pos_x, self.agente.pos_y):
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="🤖", font=("Arial", 12))
                else:
                    self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="⬜", font=("Arial", 12))
    
    def iniciar_busqueda(self):
        """Inicia la búsqueda del agente."""
        self.label_mensaje.config(text="", fg="black")

        self.boton_iniciar.config(state=tk.DISABLED)
        self.boton_reiniciar.config(state=tk.DISABLED)
        
        threading.Thread(target=self.ejecutar_busqueda, daemon=True).start()
    
    def ejecutar_busqueda(self):
        """Ejecuta la búsqueda en un hilo separado."""
        self.agente.ejecutar(self.canvas, self.cell_size, self.label_mensaje)
        
        self.boton_iniciar.config(state=tk.NORMAL)
        self.boton_reiniciar.config(state=tk.NORMAL)
    
    def reiniciar_busqueda(self):
        """Reinicia la búsqueda."""
        self.agente.reiniciar()
        self.canvas.delete("all")  
        self.dibujar_cuadricula() 
        self.label_mensaje.config(text="", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionBuscador(root)
    root.mainloop()