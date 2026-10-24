# Importamos la clase Usuario desde el módulo modelos
from modelos import Usuario

# Instanciamos (creamos) un objeto de la clase Usuario con datos de prueba
usuario1 = Usuario("Armando", "Desarrollador de Software")

# Imprimimos en consola el resultado del método
print(usuario1.presentacion())
