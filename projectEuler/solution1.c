#include <stdio.h>

int sumOfMultBelow(int max, int mult1, int mult2);

main()
{
   printf("%i\n",sumOfMultBelow(1000, 3, 5));
}

int sumOfMultBelow(int max, int mult1, int mult2)
{
   int i, sum=0;
   for(i=0; i<1000; i++)
      if(i%mult1==0 || i%mult2==0){
         sum += i;
         printf("%i ", i);
      }
         
   return sum;
}

