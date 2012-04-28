#include <stdio.h>

int fibo(int);
void _fibo(int*, int*);

main()
{
   int i, n, sum=0;
   for(i=0,n=0; n<=4000000; i+=3,n=fibo(i))
      sum +=n;
   
   printf("%i\n", sum);
}

int fibo(int n)
{
   int b;
   _fibo(&n, &b);
   return n;
}

void _fibo(int *a, int *b)
{
   switch(*a){
      case 0: *b=0; *a=0; return;
      case 1: *b=0; *a=1; return;
      case 2: *b=1; *a=1; return;
      default: break;
   }
   *a = *a - 1;
   _fibo(a,b);
   int t = *b;
   *b = *a;
   *a += t;
   return;
}
