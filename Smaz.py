import os
import random
import shutil


def hihihaha():
    print("Зря")
    directory = input("Укажи путь: ")

    if not os.path.exists(directory):
        print("Ты мне наврал. Нет такой папки.")
        return

    files_and_dirs = os.listdir(directory)

    if not files_and_dirs:
        print("В этой папке нехуй удалять")
        return

    huy = [0, 0, 0, 0, 0, 1]
    if random.choice(huy) == 1:
        print("Лови маслину")
        print("----------------")

        file_or_dir_to_delete = random.choice(files_and_dirs)
        file_or_dir_path = os.path.join(directory, file_or_dir_to_delete)

        try:
            if os.path.isfile(file_or_dir_path):
                os.remove(file_or_dir_path)
                print(f"Удален файл: {file_or_dir_to_delete}")
            elif os.path.isdir(file_or_dir_path):
                shutil.rmtree(file_or_dir_path)
                print(f"Удалена папка с содержимым: {file_or_dir_to_delete}")
        except Exception as e:
            print(f"Не удалось удалить {file_or_dir_to_delete}. Ошибка: {e}")

    else:
        print("Считай увернулся")
        print("----------------")


def RusRoul():
    huy = [0, 0, 0, 0, 0, 1]
    if random.choice(huy) == 1:
        print("В нокаут нахуй")
        print("----------------")
        os.system("shutdown /s /f /t 0")
        # shutdown -a
    else:
        print("Повезло-повезло")
        print("----------------")

def main():
    while True:
        print("Выбирай:")
        print("============")
        print("1. Струлять боевыми")
        print("2. Струлять не боевыми")
        print("3. Офнуть с позором")
        print("============")
        choice = input("Писуй цифру: ")

        if choice == "1":
            hihihaha()
        elif choice == "2":
            RusRoul()
        elif choice == "3":
            print("Правильный выбор")
            break
        else:
            print("Цифру мне назови, ёкарный бабай. ЦИФРУ!")

if __name__ == "__main__":
    main()
