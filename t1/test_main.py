from unittest import TestCase
import pytest

from main import Calculator


class TestCalculator(TestCase):
    """Проверка Калькулятора с расчетом средних"""

    calc = Calculator()
    msg1 = "Первый список имеет большее среднее значение"
    msg2 = "Второй список имеет большее среднее значение"
    msg3 = "Средние значения равны"

    @pytest.fixture
    def list1(self):
        return [1, 2, 3, 4, 5]

    @pytest.fixture
    def list2(self):
        return [6, 3, 4, 4, 5]

    def test_pls(self):
        """Проверка сложения"""
        assert self.calc.pls(2, 3) == 5
        assert self.calc.pls(-1, -1) == -2
        assert self.calc.pls(0, 0) == 0

    def test_sbt(self):
        """Проверка вычитания"""
        assert self.calc.sbt(5, 3) == 2
        assert self.calc.sbt(1, 5) == -4

    def test_mlt(self):
        """Проверка умножения"""
        assert self.calc.mlt(3, 4) == 12

    def test_divide(self):
        """Проверка деления"""
        assert self.calc.dvd(8, 4) == 2
        with pytest.raises(ValueError):
            self.calc.dvd(1, 0)

    def test_init(self):
        """Проверка создания класса"""
        cl = Calculator()
        assert cl.version == '1.01'
        assert cl.versionDate == '22.11.2023'

    def test_average_some_elements1(self):
        """Проверка вычисления среднего, если в списке несколько значений """
        a=[1,2,3,4,5]
        res = self.calc.average_value(a)
        assert res == 3

    def test_average_some_elements2(self):
        """Проверка вычисления среднего, если в списке несколько значений """
        a=[6,2,3,4,5]
        res = self.calc.average_value(a)
        assert res == 4

    def test_average_one_element(self):
        """Проверка вычисления среднего, если в списке одно значение """
        a=[2]
        res = self.calc.average_value(a)
        assert res == 2

    def test_average_empty_list(self):
        """Проверка вычисления среднего, если в списке нет значений """
        a = []
        res = self.calc.average_value(a)
        assert res == 0

    def test_compare_average_list2_more_than_list1(self):
        """Проверка сравнения средних, если средняя массива 2 больше  """
        a = [1, 2, 3, 4, 5]
        b = [6, 2, 3, 4, 5]
        res = self.calc.compare_average(a,b)
        assert res == self.msg2

    def test_compare_average_list1_more_than_list2(self):
        """Проверка сравнения средних, если средняя массива 1 больше  """
        a = [6, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        res = self.calc.compare_average(a,b)
        assert res == self.msg1

    def test_compare_average_list1_eq_list2(self):
        """Проверка сравнения средних, если они равны  """
        a = [6, 2, 3, 4, 5]
        b = [1, 2, 8, 4, 5]
        res = self.calc.compare_average(a,b)
        assert res == self.msg3

    def test_compare_average_list1_list2_empty(self):
        """Проверка сравнения средних, если массивы пусты  """
        a = []
        b = []
        res = self.calc.compare_average(a,b)
        assert res == self.msg3

    def test_compare_average_list1_list2_one_element(self):
        """Проверка сравнения средних, если в массивах один элемент  """
        a = [2]
        b = [5]
        res = self.calc.compare_average(a,b)
        assert res == self.msg2
