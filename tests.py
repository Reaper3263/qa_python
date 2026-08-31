import pytest as pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        self.collector.add_new_book("Гордость и предубеждение и зомби")
        self.collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(self.collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_get_books_genre_add_specific_book(self):
        test_name = "Гордость и предубеждение и зомби"
        self.collector.add_new_book(test_name)
        assert list(self.collector.get_books_genre().keys())[0] == test_name

    @pytest.mark.parametrize("book_name, genre, good_result", [
        ["Гордость и предубеждение и зомби", "Ужасы", False],
        ["Что делать, если ваш кот хочет вас убить", "Детективы", False],
        ["Гарри Поттер", "Фантастика", True],
        ["Горько", "Комедии", True]])
    def test_get_books_for_children(self, book_name, genre, good_result):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)

        assert (book_name in self.collector.get_books_for_children()) == good_result

    def test_get_books_genre_no_genre(self):
        test_name = "Гордость и предубеждение и зомби"
        self.collector.add_new_book(test_name)
        assert list(self.collector.get_books_genre().values())[0] == ""

    def test_get_books_with_specific_genre_2_genres_1_book(self):
        self.collector.add_new_book("Гордость и предубеждение и зомби")
        self.collector.add_new_book("Гарри Поттер")
        self.collector.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
        self.collector.set_book_genre("Гарри Поттер", "Фантастика")

        assert self.collector.get_books_with_specific_genre("Ужасы")[0] == "Гордость и предубеждение и зомби"

    def test_get_list_of_favorites_books_add_one(self):
        test_name = "Гарри Поттер"
        self.collector.add_new_book(test_name)
        self.collector.add_book_in_favorites(test_name)

        assert self.collector.get_list_of_favorites_books()[0] == test_name

    def test_get_list_of_favorites_books_delete_one(self):
        test_name = "Гарри Поттер"
        self.collector.favorites = [test_name]
        self.collector.delete_book_from_favorites(test_name)

        assert len(self.collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize("name, genre", [
        ["Гарри Поттер", "Фантастика"],
        ["Звездные войны", "Фантастика"],
        ["Гордость и предубеждение и зомби", "Ужасы"]
    ])
    def test_get_book_genre(self, name, genre):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)

        assert self.collector.get_book_genre(name) == genre
