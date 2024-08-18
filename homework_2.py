from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        num, day = 100, 0
        while num > 0:
            num -= self.power
            day += 1
            sleep(1)
            if num >= 0:
                print(f'{self.name} сражается {day} день(дня)..., осталось {num} воинов\n')
            else:
                print(f'{self.name} сражается {day} день(дня)..., осталось 0 воинов\n')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 17)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')