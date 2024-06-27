"""
Текстовый файл состоит не более чем из 106 символов J, O, B, S.

Сколько раз встречаются комбинации «BOSS»
при этом до и после этого слова нет символа «J».

Например, комбинации «JBOSS», «BOSSJ» и «JBOSSJ» не должны учитываться.

Для выполнения этого задания следует написать программу.
"""
f = open('31.txt')
a = f.readline()
while 'JBOSS' in a or 'BOSSJ' in a or 'JBOSSJ' in a:
    a = a.replace('BOSSJ',' ')
    a = a.replace('JBOSSJ', ' ')
    a = a.replace('JBOSS', ' ')
print(a.count('BOSS'))