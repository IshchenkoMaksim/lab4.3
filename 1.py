#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

from random import randint, choice


class Unit:
    id = 0

    def __init__(self, team):
        self.team = team
        self.id = Unit.id
        Unit.id += 1


class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        return f"Уровень героя {self.id} увеличен и равен: {self.level}"


class Soldier(Unit):

    def follow_to(self, hero):
        return f'Солдат {self.id}  идет за героем {hero.id}'


if __name__ == "__main__":
    hero1 = Hero("team1")
    hero2 = Hero("team2")
    team1, team2 = [], []

    for i in range(50):
        unit = Soldier(randint(0, 1))
        if unit.team == 0:
            team1.append(unit)
        else:
            team2.append(unit)

    print(f"Число солдат первой команды: {len(team1)}")
    print(f"Число солдат второй команды: {len(team2)}")

    if len(team1) > len(team2):
        print(hero1.level_up())
        print(choice(team1).follow_to(hero1))
    else:
        print(hero2.level_up())
        print(choice(team2).follow_to(hero2))
