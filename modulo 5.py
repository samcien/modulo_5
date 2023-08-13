import json

class Inventario:
    def __init__(self):
        self.items = []

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, "r") as file:
                self.items = json.load(file)
        except FileNotFoundError:
            self.items = []

    def guardar_inventario(self, archivo):
        with open(archivo, "w") as file:
            json.dump(self.items, file)

    def agregar_articulo(self, nombre, cantidad, precio_por_unidad):
        self.items.append({"nombre": nombre, "cantidad": cantidad, "precio_por_unidad": precio_por_unidad})
        print("Artículo agregado con éxito.")

    def buscar_articulo(self, nombre):
        for item in self.items:
            if item["nombre"] == nombre:
                return item
        return None

    def editar_articulo(self, nombre, cantidad, precio_por_unidad):
        for item in self.items:
            if item["nombre"] == nombre:
                item["cantidad"] = cantidad
                item["precio_por_unidad"] = precio_por_unidad
                print("Artículo editado con éxito.")
                return
        print("Artículo no encontrado.")

    def eliminar_articulo(self, nombre):
        for item in self.items:
            if item["nombre"] == nombre:
                self.items.remove(item)
                print("Artículo eliminado con éxito.")
                return
        print("Artículo no encontrado.")

def mostrar_inventario_con_valor_total(inventario):
    print("Inventario:")
    for item in inventario.items:
        valor_total = item["cantidad"] * item["precio_por_unidad"]
        print(f"Artículo: {item['nombre']}, Cantidad: {item['cantidad']}, Precio por Unidad: {item['precio_por_unidad']}, Valor Total: {valor_total}")

def mostrar_menu():
    print("Menu:"
          "\n1- Agregar Artículo"
          "\n2- Buscar Artículo"
          "\n3- Editar Artículo"
          "\n4- Eliminar Artículo"
          "\n5- Mostrar Inventario"
          "\n6- Salir")

def main():
    inventario = Inventario()
    inventario.cargar_inventario("inventario.json")

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre = input("Nombre del artículo: ")
            cantidad = int(input("Cantidad: "))
            precio_por_unidad = float(input("Precio por Unidad: "))
            inventario.agregar_articulo(nombre, cantidad, precio_por_unidad)
        elif opcion == 2:
            nombre = input("Nombre del artículo a buscar: ")
            articulo = inventario.buscar_articulo(nombre)
            if articulo:
                print("Artículo encontrado:", articulo)
            else:
                print("Artículo no encontrado.")
        elif opcion == 3:
            nombre = input("Nombre del artículo a editar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio_por_unidad = float(input("Nuevo precio por Unidad: "))
            inventario.editar_articulo(nombre, cantidad, precio_por_unidad)
        elif opcion == 4:
            nombre = input("Nombre del artículo a eliminar: ")
            inventario.eliminar_articulo(nombre)
        elif opcion == 5:
            mostrar_inventario_con_valor_total(inventario)
        elif opcion == 6:
            inventario.guardar_inventario("inventario.json")
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
