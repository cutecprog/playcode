#include <iostream>

using namespace std;

double ln(double x);
bool isPrime(unsigned long x);
unsigned long fac(unsigned x);
unsigned long facRecur(unsigned x);
int random(int seed = 0);
double cosine(double angle, const int precision = 6);
double sine(double angle, const int precision = 6);
float lawOfCosine(float a, float b, float angle);

int main()
{
   int sum = 0;
   for(int i=0; i<=6; i++)
      sum += i;
   cout << sum << endl;
   
   /*const double PI = 3.14159;
   double a = PI;

   for(int i=1; i<=64; i++)
      cout << i << ": "<< ln(i) << endl;*/
   //cout << lawOfCosine(3,4,a) << endl;
   /*for(int i=-24; i<=24; i++)
      cout << i << (char)227 << "/12: " << sine(i*PI/12, 12) << endl;*/
   /*random(3254);
   for(int i=0; i<=24; i++)
      cout << random() << endl;*/
      
   //cout << fac(7) << endl << facRecur(7) << endl;
   /*for(int i=0; i<32; i++)
      cout << i << ": " << isPrime(i) << endl;*/

   system("pause");
   
   return 0;
}

double ln(double x)
{
   x = (x-1)/(x+1);
   double sum = x;
   for(int i=0; i<256; i++) {
      x *= x;
      x *= x;
      sum += x/(2*i+1);

   }
   return sum*2;
}

bool isPrime(unsigned long x)
{
   if(x < 2)
      return 0;
   
   for(int i=2; i < x; i++)
      if(x%i == 0)
         return 0;
   return 1;
}

unsigned long fac(unsigned x)
{
   if(x < 2)
      x = 1;
   
   for(int i = x; i>2 ; i--)
      x *= i-1;
   return x;
}

unsigned long facRecur(unsigned x)
{
   if(x < 2)
      return 1;
   return  x * facRecur(x-1);
}

int random(int seed)
{
   static int key = 1234;
   if(seed)
      key = seed;
   return key = ((6221*key+4013)/757)%7919;
}

double cosine(double angle, const int precision)
{
   // Version 3: Overflow problem fixed.
   double sum = 1;
   angle *= angle;
   double num = 1;
   
   for(unsigned i=1; i<=precision; i++) {
      num *= angle;
      num /= ((i<<1)-1);
      num /= (i<<1);
      
      if(i%2) 
         sum -= num;
      else 
         sum += num;
   }
   /* Version 2: Works great from -pi/2 and pi/2 
   unsigned long int factorial = 1; 
   double sum = 1;
   angle *= angle;
   double num = 1;
   
   for(unsigned i=1; i<=6; i++) {
      factorial *= ((i<<1)-1);
      factorial *= (i<<1);
      num *= angle;
      
      if(i%2) 
         sum -= num/factorial;
      else 
         sum += num/factorial;
   }*/
   /* Version 1: Works but just so.
   inline unsigned long int factorial(unsigned long int x)
   {
      return (x == 1) ? x : x * factorial(x - 1);
   }

   inline double powIE(double x, int n)
   {
      if(n > 0)
		   return powIE(x, n-1) * x;
	   if(n < 0)
		   return powIE(x, n+1) / x;
	   return 1;
   }
   
   double sum = 1;
   double num, den;
   
   cout << " + 1";
   
   for(unsigned long int i=1; i<=6; i++) {
      num = powIE(angle, i<<1);
      den = factorial(i<<1);
      if(i%2) {
         sum -= num/den;
         cout << " - ";
      } else {
         sum += num/den;
         cout << " + ";
      }
      cout << num << "/" << den;
   }
   cout << endl;*/
   
   return sum;
}

double sine(double angle, const int precision)
{
   double sum = angle;
   double num = angle;
   angle *= angle;
   
   
   for(unsigned i=1; i<=precision; i++) {
      num *= angle;
      num /= (i<<1);
      num /= ((i<<1)+1);
      
      if(i%2) 
         sum -= num;
      else 
         sum += num;
   }
   
   return sum;
}

float lawOfCosine(float a, float b, float angle)
{
   return (a*a) + (b*b) - (2*a*b*cosine(angle));
}
