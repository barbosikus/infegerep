/*
Даны 4 числа типа int

Написать функцию, которая ищет некоторое число
А (А - одно из 4 данных) по следующему критерию:

Разность двух из 3 чисел (кроме А) равна А

Если такое число найдено вернуть номер, на котором оно стоит
(нумерация с 1).
Если таких чисел несколько, вернуть подходящий наименьший номер.
Если такое число не найдено вернуть 0.

Циклы использовать не нужно.

Примеры:
1. 1 2 3 4 -> 1 (3-2 = 1)
2. 3 -3 -3 6 -> 2 (3-6 = -3)

Дополнительно:
1. Разработать пример входных данных, чтобы на выходе получить 3
   или доказать, что таких входных данных нет
2. Разработать пример входных данных, чтобы на выходе получить 4
   или доказать, что таких входных данных нет
3. (Hard) Разработать решение задачи в котором будет два
   оператора ветвления (ИЛИ в C++ записывается как || или or)
*/

#include <iostream>
using namespace std;
double areDoubleEqual(double a, double b){
if (a == b) return a;
else return abs(a-b);

}
// Тут должна быть функция areDoubleEqual

int main(){
    cout << areDoubleEqual(0.999, 0.998);
    return 0;
}