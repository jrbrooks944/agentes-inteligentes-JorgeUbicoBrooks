import tkinter as tk
from tkinter import messagebox

class SistemaExperto:
    def __init__(self):
        self.reglas = {
            ("dolor de garganta", "tos", "congestión nasal"): "Posible resfriado común.",
            ("diarrea", "sangre en las heces", "dolor abdominal intenso"): "Posible colitis o enfermedad inflamatoria intestinal. Busque atención médica inmediata.",
            ("diarrea", "escalofrios", "dolor de estomago", "debilidad", "vomitos"): "Posible infección viral o intoxicación. Consulte a un médico si los síntomas persisten.",
            ("fiebre alta", "dolor muscular", "dolor en las articulaciones"): "Posible dengue. Consulte a un médico de inmediato.",
        }
    
    def diagnosticar(self, sintomas):
        sintomas = set(sintomas)  
        mejor_coincidencia = None
        max_sintomas_encontrados = 0

        for claves, diagnostico in self.reglas.items():
            sintomas_encontrados = len(sintomas.intersection(claves))
            if sintomas_encontrados > max_sintomas_encontrados:
                max_sintomas_encontrados = sintomas_encontrados
                mejor_coincidencia = diagnostico

        return mejor_coincidencia if mejor_coincidencia else "No se encontró un diagnóstico claro. Consulte a un médico."


class AplicacionSistemaExperto:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Diagnóstico Médico 🩺")
        
        self.sistema = SistemaExperto()
        
        self.centrar_ventana()
        
        self.sintomas_disponibles = [
           "fiebre alta", "dolor muscular", "dolor en las articulaciones",
           "diarrea", "escalofrios", "dolor de estomago", "debilidad", "vomitos",
           "diarrea", "sangre en las heces", "dolor abdominal intenso",
           "dolor de garganta", "tos", "congestión nasal"
        ]
        
        self.sintomas_seleccionados = []
        
        self.label_instrucciones = tk.Label(root, text="Seleccione sus síntomas:", font=("Arial", 14))
        self.label_instrucciones.pack(pady=10)
        
        self.sintoma_seleccionado = tk.StringVar(value=self.sintomas_disponibles[0])
        self.menu_sintomas = tk.OptionMenu(root, self.sintoma_seleccionado, *self.sintomas_disponibles)
        self.menu_sintomas.pack(pady=10)
        
        self.boton_agregar = tk.Button(root, text="Agregar Síntoma", command=self.agregar_sintoma, font=("Arial", 12))
        self.boton_agregar.pack(pady=10)
        
        self.lista_sintomas = tk.Listbox(root, width=50, height=5, font=("Arial", 12))
        self.lista_sintomas.pack(pady=10)
        
        self.boton_diagnosticar = tk.Button(root, text="Obtener Diagnóstico", command=self.obtener_diagnostico, font=("Arial", 12))
        self.boton_diagnosticar.pack(pady=10)

        self.boton_nuevo_diagnostico = tk.Button(root, text="Nuevo Diagnóstico", command=self.nuevo_diagnostico, font=("Arial", 12))
        self.boton_nuevo_diagnostico.pack(pady=10)
        
        self.label_resultado = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.label_resultado.pack(pady=10)
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 1000
        alto_ventana = 600
        
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla =  self.root.winfo_screenheight()
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
    def agregar_sintoma(self):
        """Agrega el síntoma seleccionado a la lista de síntomas."""
        sintoma = self.sintoma_seleccionado.get()
        if sintoma not in self.sintomas_seleccionados:
            self.sintomas_seleccionados.append(sintoma)
            self.lista_sintomas.insert(tk.END, sintoma)
        else:
            messagebox.showwarning("Advertencia", "El síntoma ya ha sido agregado.")
    
    def obtener_diagnostico(self):
        """Obtiene el diagnóstico basado en los síntomas seleccionados."""
        if not self.sintomas_seleccionados:
            messagebox.showwarning("Advertencia", "Por favor, agregue al menos un síntoma.")
            return
        
        resultado = self.sistema.diagnosticar(self.sintomas_seleccionados)
        self.label_resultado.config(text=f"🩺 Diagnóstico: {resultado}")
    
    def nuevo_diagnostico(self):
        """Reinicia la aplicación para un nuevo diagnóstico."""
        self.sintomas_seleccionados = [] 
        self.lista_sintomas.delete(0, tk.END) 
        self.label_resultado.config(text="")  
        messagebox.showinfo("Nuevo Diagnóstico", "Listo para realizar un nuevo diagnóstico.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSistemaExperto(root)
    root.mainloop()