"""
На вход алгоритма подаётся натуральное число N. Алгоритм строит
по нему новое число R следующим образом.

1. Строится троичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:

   а) если число N делится на 3, то слева к нему приписывается «1»,
      а справа «02»;

   б) если число N на 3 не делится, то остаток от деления на 3
      умножается на 4, переводится в троичную запись и дописывается
      в конец числа.

   Полученная таким образом запись является троичной записью
   искомого числа R.

3. Результат переводится в десятичную систему и выводится на экран.

Например, для исходного числа 11 результатом является число 107,
а для исходного числа 12 это число 353.

Укажите максимальное число N, после обработки которого с помощью
этого алгоритма получается число R, меньшее 199.
"""
