"""Здесь хранятся функции обработки"""

import data

def find_kpi(is_plan = True) -> dict:
    """Возвращает словарь значений KPI по выполненности плана
        словарём с элементами образца 'Black': 600"""

    index = 1 if is_plan else 0
    kpi = dict()
    for item in data.kpi:
        kpi[item] = data.kpi[item][index]
    return kpi
    
def find_profit(man: str, is_plan = True):
    """Возвращает премию продавца по сим с учётом выполненности плана"""
    result = 0
    kpi = find_kpi(is_plan)
    sim_cards = data.get_man(man)
    for tarif in sim_cards:
        result += kpi[tarif] * sim_cards[tarif]
    return result
    
def find_fact_sims() -> int:
    """Подсчитывает факт выполнения по симкам"""
    quantity_sims = 0
    for man in data.all:
        quantity_sims += data.get_quantity_all(data.all[man])
    return quantity_sims

def check_completed_plan() -> bool:
    """Сравнивает факт выполнения сим с планом"""
    if find_fact_sims() >= data.get_plan_sim():
        return True
    return False
    