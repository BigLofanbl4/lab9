# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

if __name__ == "__main__":
    # 14 вариант
    people = []

    while True:
        command = input("Введите команду (add, info, exit): ").strip().lower()

        if command == "exit":
            break
        elif command == "add":
            person = {}
            person["surname"] = input("Введите фамилию: ")
            person["name"] = input("Введите имя: ")
            person["zodiac"] = input("Введите знак зодиака: ")
            person["birthday"] = input("Дата рождения (число.месяц.год):").split(".")

            people.append(person)

            people.sort(
                key=lambda x: datetime.strptime(".".join(x["birthday"]), "%d.%m.%Y")
            )
        elif command == "info":
            last_name = input("Введите фамилию: ")
            found = False
            for i in people:
                if i["surname"] == last_name:
                    print(f"Фамилия:  {i['surname']}")
                    print(f"Имя: {i['name']}")
                    print(f"Знак зодиака: {i['zodiac']}")
                    print(f"Дата рождения: {i['birthday']}")
                    found = True
                    break

            if not found:
                print("Человка с такой фамилий нет в списке.")

        elif command == "help":
            print("add - добавление нового человека")
            print("info - данные о человеке по его фамилии")
            print("exti - завершение программы")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
