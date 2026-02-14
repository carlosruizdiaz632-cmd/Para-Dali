import tkinter as tk
import math

# Crear ventana
ventana = tk.Tk()
ventana.title("Feliz día del amor y la amistad")
ventana.configure(bg="white")

# Lienzo
canvas = tk.Canvas(ventana, width=400, height=450, bg="white", highlightthickness=0)
canvas.pack()

# Texto arriba
canvas.create_text(
    200, 40,
    text="Feliz día del amor y la amistad",
    font=("Arial", 16, "bold"),
    fill="red"
)

# Función para crear puntos del corazón
def puntos_corazon(escala=10):
    puntos = []
    for i in range(0, 360):
        t = math.radians(i)
        x = 16 * math.sin(t)**3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        puntos.append((200 + x * escala, 250 + y * escala))
    return puntos

# Dibujar corazón inicial
escala = 8
corazon = canvas.create_polygon(puntos_corazon(escala), fill="red", outline="red")

# Animación de latido
def latir():
    global escala
    escala = 9 if escala == 8 else 8  # cambia tamaño
    canvas.coords(corazon, *sum(puntos_corazon(escala), ()))
    ventana.after(500, latir)  # repite cada 0.5 segundos

latir()

ventana.mainloop()
