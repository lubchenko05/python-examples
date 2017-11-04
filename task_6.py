"""
Написать функцию, которая принимает словарь с рецептом и словарь с количеством доступных ингридиентов
и возвращает количество порций, которые мы можем приготовить.

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
count(recipe, available) -> 2
"""


def get_count(recipe: dict, available: dict) -> int:
    max_count = -1
    for k, v in recipe.items():
        a = available.get(k, 0)
        if max_count != -1:
            max_count = a // v if a // v < max_count else max_count
        else:
            max_count = a // v
    return max_count