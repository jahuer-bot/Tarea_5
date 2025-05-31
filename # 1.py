#1.Crea una clase base llamada Animal con ...
class Animal:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def emitir_sonido(self):
    print("Este animal hace un sonido.")

#2. Crea tres clases hijas ...
class Perro(Animal):
  def emitir_sonido(self):
    print("Guau Guau")
class Gato(Animal):
  def emitir_sonido(self):
    print("Miau")
class Pajaro(Animal):
  def emitir_sonido(self):
    print("Pio pio")

#3 Define una funcion llmada ...
def hacer_emitir_sonido(lista_de_animales):
  print("llamando a emitir_sonido()")
  for animal in lista_de_animales:
    animal.emitir_sonido()

#0 Fin
mi_perro = Perro("Firulais", 5)
mi_gato = Gato("Pelusa", 3)
mi_pajaro = Pajaro("Piolin", 1)
animales_juntos = [mi_perro, mi_gato, mi_pajaro]
hacer_emitir_sonido(animales_juntos)
