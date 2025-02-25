"""Главный сценарий программы, функции для удобного чтения инфы в консоли"""

import data
from services import *

import math


def report_about_sellers(is_plan) -> None:
    """Выводит отчёт оценки продаж сим каждого продавца точки"""
    for worker in data.get_all_men():
        name = data.get_name(worker)
        
        profit = find_profit(worker, is_plan)
        print(f'На текущий момент {name} заработал за продажи сим {profit} рублей.')
        
        if not is_plan:
            maybe_profit = find_profit(worker)
            difference = maybe_profit - profit
            print('К сожалению, план по сим не закрыт ((')
            print(f'А можно было получить: {maybe_profit} рублей.')
            print(f'Т.е. на {difference} рублей больше.')
        else:
            print('План по сим закрыт! Отличная работа ))')
        print()
        
    print('-' * 80)
    print()
    
def tell_how_complete_plan():
    """Описывает, как закрыть план акцией тарифа Хватит"""
    print('Самый дешёвый способ закрыть план:')
    add_hvatit = data.get_plan_sim() - find_fact_sims()
    print(f'Надо закинуть в план {add_hvatit} симок с тарифом "Хватит"')
    
    three_packs_hvatit = math.ceil(add_hvatit / 3)
    invest = three_packs_hvatit * 500
    print('При условии, что акция из 3 симок Хватит будет работать:')
    print(f'Нужно вложить {invest} рублей ({three_packs_hvatit * 3} сим)')


print('Расчёт личного бонуса для всех продавцов ТТ Горки-10 Теле2\n')
is_plan = check_completed_plan()
report_about_sellers(is_plan)
if not is_plan:
    tell_how_complete_plan()
