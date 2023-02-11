import pytest

from main import BooksCollector


# создаем фикстуру кторая будет нам добавлять 4 книги
@pytest.fixture(scope='function')
def collection_box():
    collector = BooksCollector()
    collector.add_new_book('Полная Ж - Радислав Гандапас')
    collector.add_new_book('Мотивация к Работе - Ф.ХерцБерг')
    collector.add_new_book('Генрих Альштуллер «Найди идею. Введение в ТРИЗ')
    collector.add_new_book('Таунсенд «Сломай систему! Лекарство от управленческой изжоги»')

    return collector