/*
Даны 2 числа типа double (тип с плавающей точкой,
произвольно задать в программе)

Написать функцию, которая проеряет равны ли эти числа с точностью
до третьего знака (т.е. 0.9998 == 0.999; 0.999 != 0.998;
0.999 == 0.9981)

Если числа равны, то вернуть первое число, если числа не равны
вернуть их разность по модулю.
*/

#include <iostream>
using namespace std;
double areDoubleEqual(double a, double b){
if (abs(a-b)<0.001) return a;
else return abs(a-b);

}
// Тут должна быть функция areDoubleEqual

int main(){
    cout << areDoubleEqual(0.999, 0.998);
    return 0;
}