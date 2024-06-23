"""
По каналу связи передаются сообщения, содержащие только десять букв:
А, Б, Е, И, К, Л, Р, С, Т, У. Для передачи используется неравномерный
двоичный код. Для кодирования букв используются кодовые слова.

Буква	Код
    А	00
    Б	1000
    Е	010
    И	011
    К	1011
    Л	1001
    Р	1100
    С	1010
    Т	1101
    У	?
Укажите кратчайшее кодовое слово для буквы У, при котором код
удовлетворяет условию Фано. Если таких кдов несколько, укажите
код с наименьшим числовым значением.

Примечание. Условие Фано означает, что никакое кодовое слово не
является началом другого кодового слова.
Это обеспечивает возможность однозначной расшифровки закодированных сообщений.
"""