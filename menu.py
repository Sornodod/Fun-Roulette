import os
def Hard():
    print("----------------")
    print("По харду, так по харду.")
    print("ОСТАВЬ НАДЕЖДУ ВСЯК СЮДА ВХОДЯЩИЙ")
    print("----------------")
    os.system("python Hard.py")
def Smaz():
    print("----------------")
    print("Бережённого Бог бережёт")
    print("Тише едешь - тише едешь")
    print("----------------")
    os.system("python Smaz.py")
def main():
    while True:
        print("Выбери сложность:")
        print("1. По хардкору")
        print("2. Со смазкой")
        print("3. Выход")
        choice = input("Думай шустрее: ")
        if choice == "1":
            Hard()
        elif choice == "2":
            Smaz()
        elif choice == "3":
            print("Бай-бай")
            break
        else:
            print("Идиот.")
if __name__ == "__main__":
    main()
