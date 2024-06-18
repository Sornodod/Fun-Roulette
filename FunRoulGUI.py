import os
import random
import shutil
import flet as ft

def hihihaha(directory, output, page):
    if not os.path.exists(directory):
        page.add(ft.Text("Ты мне наврал. Нет такой папки."))
    else:
        files_and_dirs = os.listdir(directory)
        if not files_and_dirs:
            page.add(ft.Text("В этой папке нехуй удалять"))
        else:
            if random.choice([0, 0, 0, 0, 0, 1]) == 1:
                file_or_dir_to_delete = random.choice(files_and_dirs)
                file_or_dir_path = os.path.join(directory, file_or_dir_to_delete)
                try:
                    if os.path.isfile(file_or_dir_path):
                        os.remove(file_or_dir_path)
                        page.add(ft.Text(f"Удален файл: {file_or_dir_to_delete}"))
                    elif os.path.isdir(file_or_dir_path):
                        shutil.rmtree(file_or_dir_path)
                        page.add(ft.Text(f"Удалена папка с содержимым: {file_or_dir_to_delete}"))
                except Exception as e:
                    page.add(ft.Text(f"Не удалось удалить {file_or_dir_to_delete}. Ошибка: {e}"))
            else:
                page.add(ft.Text("Считай увернулся"))
    page.update()



def RusRoul(output, page, result_text):
    if random.choice([0, 0, 0, 0, 0, 1]) == 1:
        result_text.value = "В нокаут нахуй"
        os.system("shutdown /s /f /t 0")
    else:
        result_text.value = "Повезло-повезло"
    page.update()



def main(page: ft.Page):
    page.title = "ЦИФРОВАЯ РУССКАЯ РУЛЕТКА"
    page.theme_mode = 'dark'
    page.window_width = 600
    page.window_height = 870
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def show_first_page():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src="clown.gif"),
                        alignment=ft.alignment.center
                    ),
                    ft.Text('ЦИФРОВАЯ РУССКАЯ РУЛЕТКА', size=24, text_align=ft.TextAlign.CENTER,
                            width=page.window_width),
                    ft.Text('by Sornodod', size=16, text_align=ft.TextAlign.CENTER, width=page.window_width),
                    ft.Text('Автор программы не несёт ответственности за последствия.', size=10),
                    ft.ElevatedButton(text="НАЧАТЬ", on_click=show_second_page)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def show_second_page(e):
        page.controls.clear()
        output = ft.Column()
        difficulty_dropdown = ft.Dropdown(
            options=[
                ft.TextField(label="Выбор сложности"),
                ft.dropdown.Option(key="hard", text="По харду"),
                ft.dropdown.Option(key="easy", text="Со смазкой")
            ],
            width=200
        )

        def on_start_clicked(e):
            if difficulty_dropdown.value == "hard":
                show_hard_page(output)
            elif difficulty_dropdown.value == "easy":
                show_easy_page(output)

        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            difficulty_dropdown,
                            ft.ElevatedButton(text="ПОГНАЛИ", on_click=on_start_clicked)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.ElevatedButton(text="Офнуть", on_click=lambda e: page.window_close())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def show_hard_page(output):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("По хардкору", text_align=ft.TextAlign.CENTER),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Струлять боевыми",
                                                  on_click=lambda e: show_drive_input("hard", output)),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Струлять не боевыми",
                                                  on_click=lambda e: show_russian_roulette_page(output, page)),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Назад", on_click=lambda e: show_first_page()),
                        alignment=ft.alignment.center
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def show_russian_roulette_page(output, page):
        page.controls.clear()
        result_text = ft.Text()

        def on_spin_clicked(e):
            RusRoul(output, page, result_text)

        page.add(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("КРУТИ БАРАБАН", text_align=ft.TextAlign.CENTER),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Image(src="gun.gif"),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=result_text,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="КРУТИ БАРАБАН", on_click=on_spin_clicked),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Назад", on_click=lambda e: show_second_page(output)),
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    #def on_spin_clicked(e):
     #   RusRoul(output, page, result_text)

    def show_easy_page(output):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Со смазкой", text_align=ft.TextAlign.CENTER),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Струлять боевыми",
                                                  on_click=lambda e: show_path_input("easy", output)),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Струлять не боевыми",
                                                  on_click=lambda e: show_russian_roulette_page(output, page)),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="Вернуться в самое начало", on_click=lambda e: show_first_page()),
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def show_drive_input(mode, output):
        page.controls.clear()
        drive_input = ft.TextField(label="Укажи букву локального диска (например, C, D, E)")

        def on_drive_submit(e):
            if mode == "hard":
                directory = f"{drive_input.value}:\\"
                hihihaha(directory, output, page)
                page.update()

        page.add(
            ft.Column(
                [
                    drive_input,
                    ft.ElevatedButton(text="Подтвердить", on_click=on_drive_submit),
                    ft.ElevatedButton(text="Назад", on_click=lambda e: show_hard_page(output))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    def show_path_input(mode, output):
        page.controls.clear()
        path_input = ft.TextField(label="Укажи путь")

        def on_path_submit(e):
            if mode == "easy":
                directory = path_input.value
                hihihaha(directory, output, page)
                page.update()

        page.add(
            ft.Column(
                [
                    path_input,
                    ft.ElevatedButton(text="Подтвердить", on_click=on_path_submit),
                    ft.ElevatedButton(text="Назад", on_click=lambda e: show_easy_page(output))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        page.update()

    show_first_page()
ft.app(target=main)
