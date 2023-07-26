class Animal:
    alive = True

    def eat(self):
        print('This animal Eats')
    def sleep(self):
        print("this animal sleeps")

class Rabbit(Animal):
    def run(self):
        print('The rabbit runs')
class Fish(Animal):
    def swim(self):
        print('The fish swims')


rabbit= Rabbit()
fish= Fish()

print(rabbit.eat())