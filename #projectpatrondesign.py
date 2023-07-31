# Patrón Singleton
class Singleton:
    _instancia = None

    @classmethod
    def obtener_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

# Modelo (Datos y lógica de negocio)
class ModeloEmpleados(Singleton):
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def obtener_empleados(self):
        return self._empleados

# Vista (Interfaz de usuario)
class VistaEmpleados:
    def mostrar_empleados(self, empleados):
        print("Lista de empleados:")
        for empleado in empleados:
            print(f" - {empleado}")

    def obtener_nuevo_empleado(self):
        nombre = input("Ingrese el nombre del nuevo empleado: ")
        return nombre

# Controlador (Gestiona las interacciones entre Modelo y Vista)
class ControladorEmpleados:
    def __init__(self, modelo, vista):
        self._modelo = modelo
        self._vista = vista

    def agregar_empleado(self):
        nuevo_empleado = self._vista.obtener_nuevo_empleado()
        self._modelo.agregar_empleado(nuevo_empleado)
        self.actualizar_vista()

    def actualizar_vista(self):
        empleados = self._modelo.obtener_empleados()
        self._vista.mostrar_empleados(empleados)

# Ejemplo de uso
if __name__ == "__main__":
    modelo = ModeloEmpleados.obtener_instancia()
    vista = VistaEmpleados()
    controlador = ControladorEmpleados(modelo, vista)

    controlador.agregar_empleado()
    controlador.agregar_empleado()
    controlador.agregar_empleado()
