from ast import While
import turtle as t
from class_work import user_selected
from field import create_field
if __name__ == "__main__":
    while(True):
        print("Что ты хочешь сделать?\n1.перезапись в код\n2.создание поля с координатами\n(0 выход из программы)")
        chose = int(input())
        match chose:
            case 0:
                break
            case 1:
                user_selected()
            case 2:
                create_field()
            case _:
                print("такого варианта выбора нет! Выбери вариант из предложенных")
                chose = int(input())