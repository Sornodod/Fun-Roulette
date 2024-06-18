import os
import random
import shutil

def hihihaha():
    print("Зря")

    drive_letter = input("Укажи букву локального диска (например, C, D, E): ")

    directory = f"{drive_letter}:\\"

    if not os.path.exists(directory):
        print(f"Такого диска '{drive_letter}:' не бывает.")
        return

    all_files_and_dirs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files_and_dirs.append(os.path.join(root, file))
        for dir in dirs:
            all_files_and_dirs.append(os.path.join(root, dir))

    if not all_files_and_dirs:
        print(f"На диске '{drive_letter}:' нет нихуя.")
        return

    huy = [0, 0, 0, 0, 0, 1]
    if random.choice(huy) == 1:
        print("Лови маслину")
        print("----------------")

        file_or_dir_to_delete = random.choice(all_files_and_dirs)

        try:
            if os.path.isfile(file_or_dir_to_delete):
                os.remove(file_or_dir_to_delete)
                print(f"Удален файл: {file_or_dir_to_delete}")
            elif os.path.isdir(file_or_dir_to_delete):
                shutil.rmtree(file_or_dir_to_delete)
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
        print("4. Выход")
        print("============")
        choice = input("Писуй цифру: ")

        if choice == "1":
            hihihaha()
        elif choice == "2":
            RusRoul()
        elif choice == "3":
            print("Правильный выбор")
            break
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Цифру мне назови, ёкарный бабай. ЦИФРУ!")

if __name__ == "__main__":
    main()
