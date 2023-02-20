from roman import*

greetings = ("Приветствую Вас в переводе цифр с латинских на римские и наоборот!")
greetings_input = int(input("Выберите вариант действия. \n 1 - с римских на латынские.\n 2 - с латынских на римские. \n"))
set_of_numbers = input("Наберите цифры которые хотите преобразить: ").split(" ")

if greetings_input == 1:    
    for i in set_of_numbers:
        print(i,"-->",roman_to_int(i))
elif greetings_input == 2:   
    set_of_numbers= [int(i) for i in set_of_numbers]
    for i in set_of_numbers:
        print(i,"-->",int_to_roman(i))
else:
    print("Ошибка в выборе варианта либо наборе цифр")