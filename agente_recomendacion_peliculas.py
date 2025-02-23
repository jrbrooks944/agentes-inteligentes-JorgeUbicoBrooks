import random
import json
import tkinter as tk
from tkinter import messagebox

class AgenteRecomendador:

    def __init__(self, archivo_peliculas="agente_recomendacion_peliculas.txt"):
        with open(archivo_peliculas, "r", encoding="utf-8") as archivo:
            self.peliculas = json.load(archivo)
        self.recomendaciones_previas = {genero: [] for genero in self.peliculas.keys()}
    
    def recomendar(self, genero):
        genero = genero.lower()
        if genero in self.peliculas:
            peliculas_disponibles = [
                pelicula for pelicula in self.peliculas[genero]
                if pelicula["nombre"] not in self.recomendaciones_previas[genero]
            ]
            if peliculas_disponibles:
                pelicula_recomendada = random.choice(peliculas_disponibles)
                self.recomendaciones_previas[genero].append(pelicula_recomendada["nombre"])
                return pelicula_recomendada
            else:
                return {"nombre": "Ya no hay más películas", "anio": "", "resena": "Ya te he recomendado todas las películas de este género. ¡Espero que las disfrutes!"}
        return {"nombre": "Género no encontrado", "anio": "", "resena": "Lo siento, no tengo recomendaciones para ese género."}

class AplicacionRecomendador:

    def __init__(self, root):
        self.root = root
        self.root.title("Agente de Recomendación de Películas 🎬")
        # self.root.geometry("800x500")
        ancho_ventana = 800
        alto_ventana = 500
        
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        self.agente = AgenteRecomendador()
        
        self.label = tk.Label(root, text="Selecciona un género:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.generos = list(self.agente.peliculas.keys())
        self.genero_seleccionado = tk.StringVar(value=self.generos[0])
        
        self.menu_generos = tk.OptionMenu(root, self.genero_seleccionado, *self.generos)
        self.menu_generos.pack(pady=10)
        
        self.boton_recomendar = tk.Button(root, text="Obtener Recomendación", command=self.mostrar_recomendacion, font=("Arial", 12))
        self.boton_recomendar.pack(pady=20)
        
        self.recomendacion_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
        self.recomendacion_label.pack(pady=10)
        
        self.boton_salir = tk.Button(root, text="Salir", command=root.quit, font=("Arial", 12))
        self.boton_salir.pack(pady=10)
    
    def mostrar_recomendacion(self):
        genero = self.genero_seleccionado.get()
        recomendacion = self.agente.recomendar(genero)
        
        self.recomendacion_label.config(
            text=f"🎥 Te recomiendo ver: {recomendacion['nombre']} ({recomendacion['anio']})\n\n📝 Reseña: {recomendacion['resena']}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionRecomendador(root)
    root.mainloop()