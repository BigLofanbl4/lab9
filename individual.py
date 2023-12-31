# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

if __name__ == "__main__":
    # 14 вариант
    people = []

    while True:
        command = input("Введите команду (add, info, list, exit, help): ").strip().lower()

        match command:
            case "exit":
                break
            
            case "add":
                person = {}
                person["surname"] = input("Введите фамилию: ")
                person["name"] = input("Введите имя: ")
                person["zodiac"] = input("Введите знак зодиака: ")
                person["birthday"] = input("Дата рождения (число.месяц.год):").split(".")

                people.append(person)

                people.sort(
                    key=lambda x: datetime.strptime(".".join(x["birthday"]), "%d.%m.%Y")
                )

            case "info":
                last_name = input("Введите фамилию: ")
                count = 0
                line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 30,
                '-' * 20,
                '-' * 20
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^30} | {:^20} | {:^20} |'.format(
                        "№",
                        "Фамилия",
                        "Имя",
                        "Знак зодиака",
                        "Дата рождения")
                )
                print(line)
                for idx, person in enumerate(people, 1):
                    if person["surname"] == last_name:
                        count += 1
                        print(
                        '| {:>4} | {:<30} | {:<30} | {:<20} | {:>20} |'.format(
                            idx,
                            person.get('surname', ''),
                            person.get('name', ''),
                            person.get('zodiac', ''),
                            ".".join(person.get('birthday', ''))
                            )
                        )
                print(line)
                if count == 0:
                    print("Людей с такой фамилий нет в списке.")

            case "list":
                line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 30,
                '-' * 20,
                '-' * 20
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^30} | {:^20} | {:^20} |'.format(
                        "№",
                        "Фамилия",
                        "Имя",
                        "Знак зодиака",
                        "Дата рождения")
                )
                print(line)
                for idx, person in enumerate(people, 1):
                    print(
                        '| {:>4} | {:<30} | {:<30} | {:<20} | {:>20} |'.format(
                            idx,
                            person.get('surname', ''),
                            person.get('name', ''),
                            person.get('zodiac', ''),
                            ".".join(person.get('birthday', ''))
                        )
                    )
                print(line)

            case "help":
                print("add - добавление нового человека")
                print("info - данные о человеке по его фамилии")
                print("exti - завершение программы")
                print("list - вывод информации о всех людях")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)
