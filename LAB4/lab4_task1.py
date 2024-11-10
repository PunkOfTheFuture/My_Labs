# TODO решите задачу
def task() -> float:

    c1 = 0
    c2 = 0

    sumc = 0

    Open = open("input.json", "r")
    a = Open.readlines()

    for i in range(len(a)):
        if a[i].find("score") != -1:
            c1 = float(a[i] [((a[i].find("score")) + 8): len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            c2 = float(a[i] [((a[i].find("weight")) + 9): len(a[i])-1])
        if c1 != 0 and c2 != 0:
            sumc += c1 * c2
            c1, c2 = 0, 0
    Open.close()
    return round(sumc, 3)




print(task())
