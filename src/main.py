import flet as ft
import database

def main(page: ft.Page):
    page.title = "Мои Фильмы"
    database.film_db()

    name_film = ft.TextField(label="Название фильма")
    genre = ft.TextField(label="Жанр")
    year_of_release = ft.TextField(label="Год выпуска")

    film_list = ft.Column()

    def add_film(e):
        database.add_film(name_film.value, genre.value, year_of_release.value)

        name_film.value = ""
        genre.value = ""
        year_of_release.value = ""

        load_films()
        page.update()

    def clear_films(e):
        database.delete_all_films()
        load_films()

    def delete_film(film_id):
        database.delete_film_by_id(film_id)
        load_films()

    def load_films():
        film_list.controls.clear()
        films = database.get_films()
        for film in films:
            film_id, name, genre_, year = film
            film_text = f"ID: {film_id} | name: {name}, genre: {genre_}, release: {year}"

            delete_icon = ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.colors.RED,
                on_click=lambda e, fid=film_id: delete_film(fid)
            )

            film_row = ft.Row([
                ft.Text(film_text, size=20, weight="bold", color=ft.colors.BLACK),
                delete_icon
            ])
            film_list.controls.append(film_row)
        page.update()

    load_films()

    clear_button = ft.ElevatedButton(
        "Очистить все",
        on_click=clear_films,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED
    )
    button = ft.ElevatedButton("Добавить", on_click=add_film)

    page.add(name_film, genre, year_of_release, button, clear_button, film_list)

ft.app(target=main)
