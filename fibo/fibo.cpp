#include <iostream>

using namespace std;

int fibo(int);
int fiboD(int);
void _fiboD(int&, int&);

int main()
{
  cout << fiboD(38) << endl;
  cout << fibo(38) << endl;
  return 0;
}

// Dumb fibo recursion
int fibo(int n)
{
   // This assumes n is positive
   if(n<2)
      return n; // Returns 1 or 0
   return fibo(n-1) + fibo(n-2);
}

// Container function for Dynamic recursion
int fiboD(int n)
{
  int b;
  _fiboD(n, b);
  return n;
}

// Actual Dynamic recursion function, note the parameters act as return varibles
void _fiboD(int &a, int &b)
{
   // Assumes a is positive
  if(a<2) {
    b = 0;
    return; // a==1 || a==0
  }
  a--;
  _fiboD(a,b);
  a+=b;
  b=a-b;
  return; // return a+b, a
}
