# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла

    a = open(INPUT_FILENAME, "r")
    b = open(OUTPUT_FILENAME, "w")
    c = []


    read = csv.DictReader(a)

    for i in read:
        c.append(i)



    # TODO Сериализовать в файл с отступами равными 4


    json.dump(c, b, indent = 4)
    a.close()
    b.close()



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
