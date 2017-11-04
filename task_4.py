"""
Написать функцию, принимающую последовательность словарей, содержащих имена и возвращающую имена через запятую,
кроме последнего, присоединённого через амперсанд.

[{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}] -> 'John, Jack & Joe'
[{'name': 'John'}, {'name': 'Jack'}] -> 'John & Jack'
[{'name': 'John'}] -> 'John'
"""


def string_names(l: list) -> str:
    names = [i['name'] for i in l]
    if len(names) > 1:
        return ', '.join(names[:-1]) + ' & ' + names[-1]
    else:
        return names[0]
