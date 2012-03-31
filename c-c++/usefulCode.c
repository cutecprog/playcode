/*-------------------------------------------------------------
   Auther: Andi Grooms
  Version: 11.03.18
	Description:
	The following code are some "useful" C functions:
	swap()
	gcm()
	gcm_r()
	fibo()
	fibo_r()
	copyString()
  printInBinary()
  floatBitsAsInt()
-------------------------------------------------------------*/

#include <stdio.h>

void swap(int *a, int *b);
/* Swaps two ints, function should get two addresses of ints.*/

int gcm(int a, int b);
/*-------------------------------------------------------------
My source for Euclid's algorithm is Elements Book VII
Proposition 2 by Euclid. The emperical Algorithm as
defined by Euclid and paraphrased by me is as follows:

Book VII Proposition 2 (Paraphrased):

	To find the greatest common measure of two given
numbers not prime to one another. Let A and B be the
two given numbers. In fact, if B measures A, (then) B
is thus the greatest common measure.
	If B does not measure A then some number will remain
from A and B, the lesser being continually subtracted,
in turn, from the greater, which will measure the
(number) preceding it. (The number the is currently
lesser subtract from the greater until they are equal.
This also assumes that these are natural numbers and
Euclid's application was with two distances so this
went without saying. If you'd like to read the full
algorithm I included Elements by Euclid in the zip
file.)

Here is a formal recursive relation inspired by the
algorithm above:

given x and y are non-zero integers
f(x,y) = f(|x|-|y|, |y|) if |x| > |y|
f(x,y) = f(|y|-|x|, |x|) if |y| > |x|
f(x,y) = |x| if |x| = |y|

From here it's pretty easy to write this recursive
algorithm in c-syntax. I choose to make it iterative
because iteration is faster and uses less memory.
-------------------------------------------------------------*/

int gcm_r(int a, int b);
/* This is the recursive version of gcm() that is described in
   the comment above. Note the recursive version does not do
   type checking and the iterative one does. */

int fibo(int n);
/* This function, with iteration, finds a given element in the
   fibonaucci sequence. */

int fibo_r(int n);
/* This function, with recursion, finds a given element in the
   fibonaucci sequence. */

void copyString(char *str, char *in);
/* Copies the string in into the string str. */

void printInBinary(long unsigned int n);
/* Prints out a int in binary(little endian) with printf(). */

long unsigned int floatBitsAsInt(float r);
/* Returns an int containing the bits of a float(IEEE). */

main()
{
  // Some sloppy test code.
  int n=32, d=4;
  printf("%i\n%i\n", n, d);
  swap(&n, &d);
  printf("%i\n%i\n", n, d);

  printf("%i\n%i\n", gcm(n,d), gcm_r(n,d));

  int i;
  for(i=0; i<10; i++)
    printf("%i: %i %i\n", i, fibo(i), fibo_r(i));

  char a[5] ="cat";
  char b[5];
  copyString(b,a);
  printf("%s\n%s\n", b, a);

  printInBinary(floatBitsAsInt(3.14159));
  printInBinary(10);
}

void swap(int *a, int *b)
{
  *a ^= *b;
  *b ^= *a;
  *a ^= *b;
}

int gcm(int a, int b)
{
	// Finds the absolute values of n and d.
	if(a < 0)
		a = -a;
	if(b < 0)
		b = -b;

	// If numerator is zero then gcd = denominator.
	if(!a)
		a = b;

	//Actually iterative algorithm.
	while(a != b)
		if(a > b)
			a -= b;
		else
			b -= a;

	return a; // n and d are equal so which one we return doesn't matter.
}

int gcm_r(int a, int b)
{
  if(a==b)
    return a;
  if(a>b)
    return gcm_r(a-b,b);
  return gcm_r(b-a,a);
}

int fibo(int n)
{
  // Starts with 0 and 1.
  int last=0, current = (n) ? 1 : 0;
  int temp, i;

  // Sums the last two number to get the current.
  for(i=1; i<n; i++) {
    temp = current;
    current += last;
    last = temp;
  }

  return current;
}

int fibo_r(int n)
{
  if(n<2)
    return n;
  return fibo_r(n-1)+fibo_r(n-2);
}

void copyString(char *str, char *in)
{
  while(*str++=*in++)
    ;
}

void printInBinary(long unsigned int n)
{
  char b[64] = "";
  int i;

	for(i=0; i < 63; i++, n >>= 1)
		b[i] = ((n%2) ? '1' : '0');

	//b = (b.substr(0,1) + " " + b.substr(1, 8) + " " + b.substr(9));
	printf("%s\n",b);
}


long unsigned int floatBitsAsInt(float r)
{
	void *ptr = &r;
	long unsigned int n = (*(long unsigned int*)ptr);

	return n;
}

