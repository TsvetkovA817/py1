# Tsvetkov Python UnitTest
class Calculator:

    version = '1.01'
    versionDate = '22.11.2023'

    def pls(self, a, b):
        return a + b

    def sbt(self, a, b):
        return a - b

    def mlt(self, a, b):
        return a * b

    def dvd(self, a, b):
        if b == 0:
            raise ValueError("Ошибка: Деление на ноль")
        return a / b

    #
    #   Вычисление среднего значения массива чисел.
    #   :param numbers: Список чисел.
    #   :return: Среднее значение.
    #
    @staticmethod
    def average_value(numbers):
        if not numbers:
            return 0  # Возвращаем 0, если список пустой
        total = sum(numbers)
        average = total / len(numbers)
        return average

    def compare_average(self, numbers1, numbers2):

        average1 = self.average_value(numbers1)
        average2 = self.average_value(numbers2)
        res = ""
        if average1 > average2:
            res = "Первый список имеет большее среднее значение"
        elif average1 < average2:
            res = "Второй список имеет большее среднее значение"
        else:
            res = "Средние значения равны"
        return res


def start_prg(name):
    print(f'Hi, {name}')  #
    cl = Calculator()
    r = cl.pls(3, 5)
    print(f'Сумма, {r}')  #
    arr1 = [10, 20, 30, 80, 50]
    arr2 = [10, 20, 30, 60, 50]
    result = cl.average_value(arr1)
    print(f"Среднее значение 1 массива: {result}")
    result = cl.average_value(arr2)
    print(f"Среднее значение 2 массива: {result}")
    result_compare = cl.compare_average(arr1, arr2)
    print(f"Сравнение средних 2х массивов: {result_compare}")


if __name__ == '__main__':
    start_prg('UnitTest')
