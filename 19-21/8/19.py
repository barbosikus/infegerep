"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками
лежат две кучи камней. Игроки ходят по очереди, первый ход делает
Петя. За один ход игрок может убрать из одной из куч один камень
или уменьшить количество камней в куче в два раза (если количество
камней в куче нечётно, остаётся на 1 камень больше, чем убирается).
Например, пусть в одной куче 6, а в другой 9 камней; такую позицию
мы будем обозначать (6, 9). За один ход из позиции (6, 9) можно
получить любую из четырёх позиций: (5, 9), (3, 9), (6, 8), (6, 5).
Игра завершается в тот момент, когда суммарное количество камней
в кучах становится не более 20. Победителем считается игрок,
сделавший последний ход, то есть первым получивший позицию,
в которой в кучах будет 20 или меньше камней. В начальный
момент в первой куче было 10 камней,
во второй куче – S камней, S > 10.

Найдите значение S, при котором Ваня выигрывает своим первым ходом
при любой игре Пети.
"""
