#1.Crea una clase base llamada Animal con ...
class Animal:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def emitir_sonido(self):
    print("Este animal hace un sonido.")
