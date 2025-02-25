"""Здесь хранятся полученные данные и функции их выдачи в требуемом виде
    При редактировании структуру не ломать! 
    Функции и процедуры завязаны на нынешней структуре. Можно только дополнять"""

def get_quantity_tarif(man, tariff) -> int:
    """Вернёт количество симок по конкретному тарифу у конкретного продавца"""
    return all[man][tariff]
    
def get_quantity_all(man: dict) -> int:
    """Возвращает количество всех симок продавца (принимает словарь из его симок)"""
    return sum(man.values())
    
def get_quantity_sims_seller(man: str) -> int:
    """Возвращает количество симок продавца по идентификатору продавца"""
    return get_quantity_all(all[man])
    
def get_man(man) -> dict:
    """Возвращает словарь из симок указанного продавца"""
    return all[man]
    
def get_name(man) -> str:
    """Возвращает имя продавца"""
    return names[man]
    
def get_all_men() -> tuple:
    """Возвращает идентификаторы продавцов как кортеж"""
    return tuple(all.keys())

def get_plan_sim() -> int:
    """Возвращает месячный план по сим"""
    return PLAN_SIM


BLACK = 'Black'
VO = 'ВО'
HVATIT = 'Хватит'

# План сим на текущий месяц
PLAN_SIM = 133

gusenko_sergey = {
    VO: 3,
    BLACK: 33,
    HVATIT: 16,
}

ivanov_anton = {
    VO: 2,
    BLACK: 10,
    HVATIT: 4
}

habibulina_alina = {
    BLACK: 1,
    HVATIT: 15
}

all = dict()    # факт выполнения по тарифам у всех продавцов
names = dict()  # имена продавцов

all['gusenko_sergey'] = gusenko_sergey
names['gusenko_sergey'] = 'Гусенко Сергей'

all['ivanov_anton'] = ivanov_anton
names['ivanov_anton'] = 'Иванов Антон'

all['habibulina_alina'] = habibulina_alina
names['habibulina_alina'] = 'Хабибулина Алина'

# Список личными бонусами тарифов. 
# По индексу 0 - при не выполненном плане
# По индексу 1 - при выполненном плане
kpi = {
   BLACK: [250, 600],
   VO: [75, 150],
   HVATIT: [10, 20]
}