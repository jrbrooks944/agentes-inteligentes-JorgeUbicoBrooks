import tkinter as tk
import random
import time
import threading

class SemaforoInteligente:
    def __init__(self):
        self.estado = "rojo"
        self.ciclo = 0
        self.detener_simulacion = False

    def percibir_trafico(self):
        """Simula la detección de tráfico con un número aleatorio de vehículos."""
        return random.randint(0, 10)

    def cambiar_estado(self, vehiculos):
        """Cambia el estado del semáforo y ajusta el tiempo según el tráfico."""
        if vehiculos > 7:
            self.estado = "verde"
            tiempo = 5  
        elif 3 <= vehiculos <= 7:
            self.estado = "amarillo"
            tiempo = 2
        else:
            self.estado = "rojo"
            tiempo = 3
        return tiempo


class AplicacionSemaforo:
    def __init__(self, root):
        self.root = root
        self.root.title("Semáforo Inteligente 🚦")

        self.semaforo = SemaforoInteligente()
        
        self.centrar_ventana()
        
        self.label_estado = tk.Label(root, text="Estado: ROJO", font=("Arial", 24), fg="red")
        self.label_estado.pack(pady=10)

        self.label_vehiculos = tk.Label(root, text="Vehículos detectados: 0", font=("Arial", 18))
        self.label_vehiculos.pack(pady=10)
        
        self.label_ciclo = tk.Label(root, text="Ciclo: 0", font=("Arial", 18))
        self.label_ciclo.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=400, height=150, bg="lightgray")
        self.canvas.pack(pady=20)

        self.boton_simular = tk.Button(root, text="Iniciar Simulación", command=self.toggle_simulacion, font=("Arial", 14))
        self.boton_simular.pack(pady=10)
        
        self.simulacion_activa = False
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 500
        alto_ventana = 450
        
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
    def toggle_simulacion(self):
        """Inicia o detiene la simulación."""
        if not self.simulacion_activa:
            self.simulacion_activa = True
            self.boton_simular.config(text="Detener Simulación")
            self.semaforo.detener_simulacion = False
            threading.Thread(target=self.ejecutar_simulacion, daemon=True).start()
        else:
            self.simulacion_activa = False
            self.boton_simular.config(text="Iniciar Simulación")
            self.semaforo.detener_simulacion = True
    
    def ejecutar_simulacion(self):
        """Ejecuta la simulación del semáforo en un hilo separado."""
        while not self.semaforo.detener_simulacion:
            self.semaforo.ciclo += 1
            vehiculos = self.semaforo.percibir_trafico()
            tiempo = self.semaforo.cambiar_estado(vehiculos)
            
            color = "green" if self.semaforo.estado == "verde" else "yellow" if self.semaforo.estado == "amarillo" else "red"
            self.label_estado.config(text=f"Estado: {self.semaforo.estado.upper()}", fg=color)
            self.label_vehiculos.config(text=f"Vehículos detectados: {vehiculos}")
            self.label_ciclo.config(text=f"Ciclo: {self.semaforo.ciclo}")
            
            self.dibujar_carros(vehiculos)
            
            time.sleep(tiempo)

        self.label_estado.config(text="Estado: ROJO", fg="red")
        self.label_vehiculos.config(text="Vehículos detectados: 0")
        self.label_ciclo.config(text="Ciclo: 0")
        self.canvas.delete("all")  
    
    def dibujar_carros(self, vehiculos):
        """Dibuja los carros detectados en el Canvas."""
        self.canvas.delete("all")  
        for i in range(vehiculos):
            x = random.randint(10, 380) 
            y = random.randint(10, 130) 
            self.canvas.create_text(x, y, text="🚗", font=("Arial", 20)) 

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSemaforo(root)
    root.mainloop()