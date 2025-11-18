# from dotenv import load_dotenv
# import os

# load_dotenv()
# my_variable = os.getenv('MY_KEY')
# print(my_variable)

# def main():
#     print("Hi gitler ")

# name = "Tom"

# if __name__ == "__main__":
#     main()


# class Gypsy:
  
#     def __init__(self,name,skin):
#        self.name = name
#        self.skin = skin
#     def deception(self):
#         print(f"{self.name} Цыган обманывает")

# gypsy1 = Gypsy(name="Дута", skin="кэкэщка")

# print(gypsy1.name, gypsy1.skin)
# gypsy1.deception()


# def main():
#   print("Hi frim hi")

# class Npc:
     
#   def __init__(self, name="Gaymer", body_color="brown", hp=100):
#         self.name = name
#         self.body_color = body_color
#         self.hp = hp

# def get_dmg(self, damage):
#     self.hp -= damage

# class Npc:
#     def __init__(self, name ="Gay", body_color = "black", hp = 100):
#         self.name = name
#         self.body_color = body_color
#         self.hp = hp

#     def get_dmg(self, dmg):
#         self.hp -= dmg
#         print(f"-{dmg} HP")
    

#     def regen(self, regen):
#         self.hp += regen
#         print(f"+{regen} HP")

#     def get_dmg(self, dmg):
#         self.hp -= dmg
#         print(f"-{dmg} HP")
    

#     def regen(self, regen):
#         self.hp += regen
#         print(f"+{regen} HP")
   
#     def __del__(self):
#         print("Удаление персонажa")



# npc = Npc()
# npc.get_dmg(12) 
# npc.regen(2)   


# print(npc.hp)
# def main():
#    print("Hi from hi")

# if __name__ == "__main__":
#    main()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
 
#     # сеттер для установки возраста
#     def set_age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
 
#     # геттер для получения возраста
#     def get_age(self):
#         return self.__age
 
#     # геттер для получения имени
#     def get_name(self):
#         return self.__name
     
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom.print_person()  # Имя: Tom  Возраст: 39
# tom.set_age(-3486)  # Недопустимый возраст
# tom.set_age(25)
# tom.print_person()  # Имя: Tom  Возраст: 25

class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст

    # свойство-геттер
    @property
    def age(self):
        return self.__age
    # свойство-сеттер
    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name
     
    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.age = -3486     # Недопустимый возраст  обращение к сеттеру
print(tom.age)      # Обращение к геттеру
tom.age = 25        # Обращение к сеттеру
tom.print_person() 