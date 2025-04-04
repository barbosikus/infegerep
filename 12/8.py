"""
Исполнитель Редактор получает на вход строку цифр и
преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов.

заменить (v, w)
нашлось (v)

Первая команда заменяет в строке первое слева вхождение
цепочки v на цепочку w. Если цепочки v в строке нет, эта
команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор.

Дана программа для Редактора:

НАЧАЛО
    ПОКА нашлось(11)
       ЕСЛИ нашлось(112)
          ТО заменить(112, 7)
          ИНАЧЕ заменить(11,3)
       КОНЕЦ ЕСЛИ
    КОНЕЦ ПОКА
КОНЕЦ

Исходная строка содержит 12 единиц и 4 двойки, других
цифр нет, точный порядок расположения цифр неизвестен.
Какую наибольшую сумму цифр может иметь строка,
которая получится после выполнения программы?
"""
def f(x):
    while '11' in x:
        if '112' in x:
            x = x.replace('112', '7',1)
        else:
            x = x.replace('11', '3',1)
    return x
print(f('1121121121121111').count('7')*7+f('1121121121121111').count('3')*3 )
