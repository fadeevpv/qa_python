
def test_add_new_book_add_four_books(collection_box):
    assert list(collection_box.get_books_rating().keys()) == ['Полная Ж - Радислав Гандапас', 'Мотивация к Работе - Ф.ХерцБерг', 'Генрих Альштуллер «Найди идею. Введение в ТРИЗ', 'Таунсенд «Сломай систему! Лекарство от управленческой изжоги»']
    # Проверка что добавилось 4 новые книги


def test_add_new_book_cannot_add_same_book(collection_box):
    books = list(collection_box.get_books_rating().keys())  # получаем название всех книг
    collection_box.add_new_book(books[0])  # пытаемся добавить первую книгу из списка кторая уже есть
    assert list(collection_box.get_books_rating().keys()) == ['Полная Ж - Радислав Гандапас', 'Мотивация к Работе - Ф.ХерцБерг', 'Генрих Альштуллер «Найди идею. Введение в ТРИЗ', 'Таунсенд «Сломай систему! Лекарство от управленческой изжоги»']
    # Проверка что книгу кторую мы получили первой из спика еще раз добавить не удалось

def test_set_book_rating_impossible_set_rating_for_non_exist_book(collection_box):
    collection_box.set_book_rating('Чебурашка', 9)  # добавляем рэйтинг не существующей книге
    assert collection_box.get_book_rating('Чебурашка') == None  # проверяем что рэйтинг для несуцществующей книги не доавился
    # Провека что нельзя добовлять рэйтинг не существующей книге

def test_set_book_rating_impossible_set_rating_lees_teh_one(collection_box):
    collection_box.set_book_rating('Полная Ж - Радислав Гандапас', 0)  # добовляем уже существующей книге рэйтинг ==0
    assert collection_box.get_book_rating('Полная Ж - Радислав Гандапас') == 1  # проверяем что рэйтинг у книги не изменился и != 0
    # Проверка что нельзя выставить книге из списка рэйтинг меньше еденицы

def test_set_book_rating_impossible_set_rating_more_than_ten(collection_box):
    books = list(collection_box.get_books_rating().keys())  # получаем сиписок всех книг
    set_rating = 12  # переменная с значением рэйтинга больше 10 будем добовлять ее для существующей книги
    collection_box.set_book_rating(books[1], set_rating)  # выбираем вторую книгу в списке и выставляем ей рэйтинг 12
    assert collection_box.get_book_rating(books[1]) != set_rating  # проверяем что рэйтинг книги не изменился
    # Проверка что нельзя выставить книге из списка рэйтинг больше 10


def test_get_books_rating_no_rating_for_a_non_existent_book(collection_box):
    get_rating = collection_box.get_book_rating('Джидайские техники или как воспитать свою обезъяну')  # запрашиваем рэйтинг книги кторой нет в списке
    assert get_rating is None  # проверяем что нет рэйтинга у несущуствующей книги
    # Проверка что у не добавленной книги нет рейтинга

def test_add_book_in_favorites_add_new_book(collection_box):
    books = list(collection_box.get_books_rating().keys())   # получаем список книг
    collection_box.add_book_in_favorites(books[3])          # добовляем четвертую  книги из списка книг в сипосок фаворитов
    assert collection_box.get_list_of_favorites_books() == [books[3]]  #проверяем что именно четвертая книга из писка довавилась в список фаваритов
    # Провека добовления новой книги в список фаворитов

def test_add_book_in_favorites_cant_add_same_book_in_favorit(collection_box):
    books = list(collection_box.get_books_rating().keys())  # получаем список книг
    collection_box.add_book_in_favorites(books[2])          # добовляем третью книгу в сисок фаваритов
    len_of_favorint = len(collection_box.get_list_of_favorites_books())  # вносим в переменную длинну  списка фаворитов, после добовляения новой книги
    collection_box.add_book_in_favorites(books[2])         # повторно добовляем туже книгу в список фаворитов
    assert collection_box.get_list_of_favorites_books() == [books[2]]  # проверяем что длина списка не увеличилась а соталось прежней книга недобавлена
    # Проверка что нельзя добавить одну и туже книгу в список фаворитов

def test_add_book_in_favorites_cant_add_in_favorites_if_book_not_in_books_rating(collection_box):
    books = list(collection_box.get_books_rating().keys())    # получаем весь список книг из books_rating
    collection_box.add_book_in_favorites('Элли в изумрудном городе') # добовляем книгу кторой нет в books_rating
    assert 'Элли в изумрудном городе' not in books   #что добовляемой книги нет в books_rating
    assert 'Элли в изумрудном городе' not in collection_box.get_list_of_favorites_books() #проверяем что книга не попала в фавориты
    # Проверка нельзя добавить книгу кторой нет в books_rating

def test_delete_book_from_favorites_delete_book(collection_box):
    books = list(collection_box.get_books_rating().keys())  # получаем список книг из books_rating
    collection_box.add_book_in_favorites(books[1])  # добовляем вторую книгу из списка books_rating в список book_in_favorites - 'Мотивация к Работе - Ф.ХерцБерг'
    collection_box.add_book_in_favorites(books[3])  # добовляем еще одну книгу из списка books_rating в список book_in_favorites - Таунсенд «Сломай систему! Лекарство от управленческой изжоги»
    collection_box.delete_book_from_favorites(books[1])     # удаляем одну книгу из списка фаворитов - 'Мотивация к Работе - Ф.ХерцБерг'
    assert collection_box.get_list_of_favorites_books() == [books[3]] # проверяем что всписке осталась одна книга
    # Проверка удаления книги из списка фаворитов

def test_set_book_rating_add_specific_rating(collection_box):
    collection_box.set_book_rating('Мотивация к Работе - Ф.ХерцБерг', 8)  # выставляем имеющейся книге в списке books_rating новый рэйтинг
    assert collection_box.get_book_rating('Мотивация к Работе - Ф.ХерцБерг') == 8  # проверяем что рэйтинг установлен
    # Проверка установки нового рэйтинга для книги имеющегося в списке books_rating

def test_get_books_with_specific_rating(collection_box):
    collection_box.set_book_rating('Мотивация к Работе - Ф.ХерцБерг', 8)  # добовляем имеющейся книге новый рэйтинг
    assert collection_box.get_books_with_specific_rating(8) == ['Мотивация к Работе - Ф.ХерцБерг']  # провряем что книга в списке
    # Проверка вывода списка с определенным рэйтиногом


