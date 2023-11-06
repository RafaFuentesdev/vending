import tkinter as tk
from tkinter import PhotoImage


# Función que maneja la selección de un producto
def seleccionar_producto(product_id):
    print(f"Producto seleccionado: {product_id}")
    # Aquí iría la lógica para manejar la selección del usuario


# Configuración inicial de la ventana de Tkinter
root = tk.Tk()
root.title("Máquina Expendedora")

# Carga de imágenes de productos
imagen_producto_1 = PhotoImage(
    file="/Users/rafa/Developer/vending/580b57fbd9996e24bc43c109.png"
)
imagen_producto_2 = PhotoImage(
    file="/Users/rafa/Developer/vending/png-clipart-coca-cola-coca-cola.png"
)
# ... cargar más imágenes según sea necesario

# Creación de botones para los productos
boton_producto_1 = tk.Button(
    root, image=imagen_producto_1, command=lambda: seleccionar_producto("Producto 1")
)
boton_producto_2 = tk.Button(
    root, image=imagen_producto_2, command=lambda: seleccionar_producto("Producto 2")
)
# ... crear más botones para otros productos

# Colocación de los botones en la ventana
boton_producto_1.pack()
boton_producto_2.pack()
# ... colocar más botones

# Inicio del bucle principal de Tkinter
root.mainloop()
