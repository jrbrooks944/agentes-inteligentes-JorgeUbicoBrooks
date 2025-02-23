# Agentes Inteligentes en Python 
 

1: Agente de Semáforo Inteligente (Reactivo)

  Simula un semáforo inteligente que cambia de estado (rojo, amarillo, verde) según la cantidad de vehículos detectados.

Atributos:
  estado: Almacena el estado actual del semáforo (rojo, amarillo, verde).
  ciclo: Lleva un conteo de los ciclos de la simulación.
  detener_simulacion: Bandera para controlar cuándo detener la simulación.
  
Métodos:
  percibir_trafico(): Simula la detección de tráfico generando un número aleatorio de vehículos (entre 0 y 10).
  cambiar_estado(vehiculos): Cambia el estado del semáforo y ajusta el tiempo de espera según la cantidad de vehículos detectados:
  Si hay más de 7 vehículos, el semáforo se pone en verde por 5 segundos.
  Si hay entre 3 y 7 vehículos, el semáforo se pone en amarillo por 2 segundos.
  Si hay menos de 3 vehículos, el semáforo se pone en rojo por 3 segundos.

Flujo del Programa

Inicio:
  Al ejecutar el programa, se muestra una ventana con el semáforo en estado "rojo", 0 vehículos detectados y el ciclo en 0
  .
Simulación:
  Al hacer clic en "Iniciar Simulación", el semáforo comienza a cambiar de estado según la cantidad de vehículos detectados.
  Los carros se dibujan en el Canvas en posiciones aleatorias.
  El ciclo aumenta en cada iteración.
  
Detener Simulación:
  Al hacer clic en "Detener Simulación", la simulación se detiene y el semáforo vuelve al estado "rojo".

  EJECUTAR 
  python agente_semaforo.py


2:  Agente Buscador de Objetos (Basado en Objetivos)
    
  Simula un agente (🤖) que busca un objetivo (🎯) en una cuadrícula de 20x20.

Atributos:
  size: Tamaño de la cuadrícula (20x20 en este caso).
  grid: Representa la cuadrícula como una matriz de celdas.
  pos_x, pos_y: Posición actual del agente.
  obj_x, obj_y: Posición del objetivo.
  prev_x, prev_y: Guarda la posición anterior del agente para actualizar la interfaz de manera eficiente.

Métodos:
  reiniciar(): Reinicia la posición del agente y el objetivo en la cuadrícula.
  mover(): Mueve al agente hacia el objetivo (arriba, abajo, izquierda o derecha).
  ejecutar(canvas, cell_size, label_mensaje): Ejecuta la búsqueda del agente y actualiza la interfaz gráfica.
  actualizar_interfaz(canvas, cell_size): Actualiza solo las celdas que cambian (la posición anterior y la nueva posición del agente).

Flujo del Programa

Inicio:
  Al ejecutar el programa, se muestra una ventana con una cuadrícula de 20x20.
  El agente (🤖) se coloca en la esquina superior izquierda (0, 0).
  El objetivo (🎯) se coloca en una posición aleatoria.

Búsqueda:
  Al hacer clic en "Iniciar Búsqueda", el agente comienza a moverse hacia el objetivo.
  El agente se mueve paso a paso (arriba, abajo, izquierda o derecha) hasta alcanzar el objetivo.
  Durante el movimiento, solo se actualizan las celdas que cambian (la posición anterior y la nueva posición del agente).

Objetivo Encontrado:
  Cuando el agente alcanza el objetivo, se muestra un mensaje: "¡Objeto encontrado! 🎉".

Reiniciar:
  Al hacer clic en "Reiniciar Búsqueda", el agente y el objetivo se colocan en nuevas posiciones aleatorias, y la búsqueda puede comenzar de nuevo.


EJECUTAR 
  python agente_buscador_objetos.py


3: Sistema Experto para Diagnóstico Simple (Basado en Conocimiento)














  
    
