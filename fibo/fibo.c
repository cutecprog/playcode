#include <stdio.h>

int fibo(int);
int fiboD(int);
void _fiboD(int*, int*);

main()
{
  printf("%i\n", fiboD(38));
  printf("%i\n", fibo(38));
}

/* Dumb fibo recursion */
int fibo(int n)
{
   /* This assumes n is positive  */
   if(n<2)
      return n; // Returns 1 or 0  */
   return fibo(n-1) + fibo(n-2);
}

/* Container function for Dynamic recursion */
int fiboD(int n)
{
  int b;
  _fiboD(&n, &b);
  return n;
}

/* Actual Dynamic recursion function, note the parameters act as return varibles */
void _fiboD(int *a, int *b)
{
  if(*a<2) {
    *b = 0;
    return; /* a=1,b=0 or a=0,b=0 */
  }
  --*a; 
  _fiboD(a,b);
  
  *a += *b; 
  *b = *a - *b;
  return; /* a=a+b, b=a */
}
