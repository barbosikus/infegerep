"""
Исполнитель Редактор получает на вход строку символов и 
преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки символов.

А) заменить (v, w).
    Эта команда заменяет в строке первое слева вхождение цепочки v 
    на цепочку w. Например, выполнение команды заменить (111, 27) 
    преобразует строку 05111150 в строку 0527150.

    Если в строке нет вхождений цепочки v, то выполнение команды
    заменить (v, w) не меняет эту строку.

Б) нашлось (v).
    Эта команда проверяет, встречается ли цепочка v в строке исполнителя 
    Редактор. Если встречается, команда возвращает логическое значение 
    «истина», в противном случае возвращает значение «ложь». Строка 
    исполнителя при этом не изменяется.

Цикл 

    ПОКА условие
        последовательность команд
    КОНЕЦ ПОКА

выполняется, пока условие истинно.

В конструкции

  ЕСЛИ условие
    ТО команда1
    ИНАЧЕ команда2
  КОНЕЦ ЕСЛИ

выполняется команда1 (если условие истинно) или 
команда2 (если условие ложно).

Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (111) ИЛИ нашлось (66)
    ЕСЛИ нашлось (6666)
        ТО заменить (6666, 1)
        ИНАЧЕ заменить (111, 3)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (66)
        ТО заменить (66, 6)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

На вход приведённой выше программе поступает строка, которая 
начинается с цифры «1», а затем содержит n цифр «6» (3 < n < 10 000).

Определите наименьшее значение n, при котором в строке, получившейся 
в результате выполнения программы, будет хотя бы 5 цифр «3».
"""
def f(x):
    while '111' in x or '66' in x:
        if '6666' in x:
            x = x.replace('6666','1',1)
        else:
            x = x.replace('111', '3', 1)
        if '66' in x:
            x = x.replace('66','6',1)
    return x
for n in range(4,10_000):
    a = f('1'+'6'*n)
    if a.count('3') >=5:
        print(n)
        break