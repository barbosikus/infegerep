#include "iostream"
using namespace std;
int a(int n, int m){
if (n == m) return n+1;
else return n;

}
int main() {
cout << a(34, 34);
}