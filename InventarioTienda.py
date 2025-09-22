class InventarioTienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  

    def agregar_producto(self):
        print("PRODUCTO NUEVO")
        nombre = str(input("Ingresa nombre producto nuevo: "))
        precio = float(input("Ingresa nuevo precio: "))
        cantidad = float(input("Cantidad de Stock: "))
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(producto)
        print("Se agregó al inventario\n")

    def vender_producto(self):
        nombre = input("Ingresa el nombre del producto a vender: ")
        producto_encontrado = None
        for i in self.productos:
            if i ["nombre"] == nombre:
                producto_encontrado = i
                break
        if not producto_encontrado:
            print("Producto no encontrado")
            return

        descuento = float(input("Cantidad que se descontará del stock: "))
        if descuento > producto_encontrado["cantidad"]:
            print("Cantidad no disponible")
        else:
            producto_encontrado["cantidad"] -= descuento
            print(f"Stock actualizado de {nombre}: {producto_encontrado['cantidad']} unidades")

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}:")
        if not self.productos:
            print("No hay productos registrados")
        else:
            for p in self.productos:
                print(f"NOMBRE: {p['nombre']}, Precio: ${p['precio']}, Cantidad: {p['cantidad']}")
        print()

    def producto_mas_caro(self):
        print("\nProducto más caro:")
        if not self.productos:
            print("No hay productos registrados\n")
            return
        mas_caro = self.productos[0]
        for i in self.productos:
            if i["precio"] > mas_caro["precio"]:
                mas_caro = i
        print(f"{mas_caro['nombre']} - ${mas_caro['precio']} (Stock: {mas_caro['cantidad']})\n")

    def MENU(self):
        while True:
            print("________________________________")
            print("MENU DE INICIO")
            print("________________________________")
            print("(1) Agregar producto")
            print("________________________________")
            print("(2) Vender Producto")
            print("________________________________")
            print("(3) Ver el inventario")
            print("________________________________")
            print("(4) Consultar producto más caro")
            print("________________________________")
            print("(5) Salir")
            print("________________________________")

            op = int(input("Elije una opción: "))
            
            if op == 1:
                self.agregar_producto()
            elif op == 2:
                self.vender_producto()
            elif op == 3:
                self.mostrar_inventario()
            elif op == 4:
                self.producto_mas_caro()
            elif op == 5:
                print("Salir del programa")
                break
            else:
                print("Opción no válida\n")


# Programa principal
nombre_tienda = input("Nombre de la tienda: ")
inventario1 = InventarioTienda(nombre_tienda)
inventario1.MENU()