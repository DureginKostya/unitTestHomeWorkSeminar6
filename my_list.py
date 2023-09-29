"""Модуль предназначен для сравнения двух списков чисел по
их средним значениям"""


class My:
    """Класса объекта. Позволяет проводить манипуляции
    со строкой и списком"""

    def __init__(self, user_string) -> None:
        self._user_string = user_string

    def get_my(self) -> str:
        """Геттер класса. Позволяет получить значение объекта
        данного класса."""
        return self._user_string

    def set_my(self, user_string) -> None:
        """Сеттер класса. Позволяет изменить объект данного
        класса"""
        self._user_string = user_string


class Examination(My):
    """Класс Examination наследует свойства класса My.
    Основная задача класса преобразовать строку в список из чисел"""

    def _user_list(self) -> list[float] | str:
        """Функция проверяет возможность преобразовать строку из строки в
        список из чисел.
        Если возможно, то осуществляет преобразование, иначе возвращает
        сообщение о не возможности это сделать."""
        if self._user_string != '':
            try:
                return list(map(float, self._user_string.strip().split(' ')))
            except ValueError:
                return '!!!Обнаружено: недопустимые символ/(-ы) в списке!!!'
        return '!!!Обнаружено: пустой/(-ые) список/(-ки)!!!'


class Average(Examination):
    """Класс Average наследует свойства класса Examination.
    Основная задача класса осуществить расчет среднего значения
    списка чисел."""

    def _average_number(self) -> float | str:
        """Функция рассчитывает среднее значение списка чисел"""
        value_after_examination = Examination._user_list(self)
        if not isinstance(value_after_examination, str):
            return sum(value_after_examination) / len(value_after_examination)
        return value_after_examination

    @staticmethod
    def get_comparison_result(first_list, second_list) -> str:
        """Функция сравнивает два списка по их средним значениям"""
        first_number = Average._average_number(My(first_list))
        if not isinstance(first_number, str):
            second_number = Average._average_number(My(second_list))
            if not isinstance(second_number, str):
                if first_number == second_number:
                    return (f'Средние значения равны:'
                            f' {first_number:.2f} = {second_number:.2f}')
                if first_number > second_number:
                    return (f'Первый список имеет большее среднее значение:'
                            f' {first_number:.2f} > {second_number:.2f}')
                return (f'Второй список имеет большее среднее значение:'
                        f' {first_number:.2f} < {second_number:.2f}')
            return second_number
        return first_number


if __name__ == '__main__':
    first_values = input(
        'Введите первую последовательность чисел через пробел: ')
    second_values = input(
        'Введите вторую последовательность чисел через пробел: ')
    print(Average.get_comparison_result(first_values, second_values))
