# Домашнее задание к теме 1.
# Выполнил Федотов Роман, Slack: @fedotov
# 11.09.2021

from random import randint

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. ',
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print('Утка не зря с собой зонт ☔ забрала ─ \n'
          f'Дождь закончился лишь через {randint(2,4)} дня!'
          )


def step2_no_umbrella():
    print('Зонт ☔ не взяла ─ прямо к бару пошла, \n'
          'Однако сухой целиком в бар зашла \n'
          'Удивляться не нужно, так было всегда \n'
          'ведь ливень для утки 🦆  ─ как с гуся вода.'
          )

if __name__ == '__main__':
    step1()
