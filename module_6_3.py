import random # для генерации случ. числа в методе lay_eggs

class Animal:  # зададим класс Животные
    live = True # живой
    sound = None # звук
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed): # зададим метод с параметрами
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа

    def move(self, dx, dy, dz):  # зададим метод для изменения координат
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        # если значение new_z меньше нуля, то вывод надписи
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:  # иначе изменения будут внесены
            self._cords = [new_x, new_y, new_z]

    def get_cords(self): # вывод координат с пояснением
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self): # метод для степени опасности
        if self._DEGREE_OF_DANGER < 5: # если меньше 5:
            print("Sorry, i'm peaceful :)")
        else: # иначе вывод надписи-предупреждения:
            print("Be careful, i'm attacking you 0_0")

    def speak(self): # метод для вывода строки со звуком
        print(self.sound)



class Bird(Animal): # зададим класс-наследник
    beak = True    # наличие клюва

    def lay_eggs(self):  # зададим метод для вывода рандомного числа от 1 до 4 - кол-во яиц
        eggs_count = random.randint(1, 4)
        print(f"Here are(is) {eggs_count} eggs for you")



class AquaticAnimal(Animal): # зададим класс-наследник
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):  # зададим метод для уменьшения z
        dz = abs(dz) # берем по модулю
        # нов. координата: третий элемент из списка _cords минус скорость, кот. уменьш. в 2 р
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0: # если нов. коорд. меньше нуля, то
            print("It's too deep, i can't dive :(")
        else: # иначе - изменится
            self._cords[2] = new_z

class PoisonousAnimal(Animal): # зададим класс-наследник
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal): # зададим класс-наследник
    sound = "Click-click-click" # зададим звук для этого класса

# пример
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()