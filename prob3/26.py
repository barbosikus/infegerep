"""
Общественная организация готовит к отправке посылки для детского дома. Объём
кузова грузовика, на котором повезут посылки, известен, и он меньше, чем объём
всех посылок. По заданной информации об объёме посылок и кузова определите
максимальное количество посылок, которое может быть перевезено за один раз, а
также максимально возможный размер посылки, при условии, что требуется
перевезти наибольшее возможное количество посылок.

Входные данные

В первой строке входного файла находятся два числа: S — размер свободного
места (объём) в кузове грузовика (натуральное число,  
не превышающее 10 000) и N - количество посылок, которые надо перевезти
(натуральное число, не превышающее 1000).  
В следующих N строках находятся значения объёмов указанных посылок (все числа
натуральные, не превышающие 100), каждое в отдельной строке.

Выходные данные

Запишите в ответе два числа: сначала наибольшее число посылок, которые могут
быть перевезены за один раз, затем максимальный размер посылки, при условии,
что нужно перевезти наибольшее возможное количество посылок. Если вариантов
комплектации несколько, выберите тот, при котором будет доставлена посылка
наибольшего объёма.

Типовой пример организации данных во входном файле

100 4  
80  
30  
50  
40

При таких исходных данных можно перевезти максимум 2 посылки. Их возможные
объёмы: 30 и 40, 30 и 50 или 40 и 50. Наибольший объём посылки из
перечисленных пар — 50, поэтому ответ для приведённого примера: 2; 50.

Типовой пример имеет иллюстративный характер. Для выполнения задания
используйте данные из прилагаемых файлов.


"""