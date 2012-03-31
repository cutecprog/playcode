#include <iostream>
#include <time.h>

using namespace std;

void makeDiamond (int, int);

int main()
{
    int startTime;
    
    int size, numOfTimes;
    cin >> size >> numOfTimes;
    startTime = time(0);
    makeDiamond(size, numOfTimes);
    
    cout << "Time to complete task: " <<(time(0) - startTime) << " Seconds" << endl;
     
    system("pause");
}

void makeDiamond (int size, int numOfTimes)
{
    int spaces = size;
    int stars = 0;
    int m = 1;
    int c = 0;

    while (c <= ((size*2)*numOfTimes))
    {
        for (int i =0; i < spaces; i++)
            cout << ' ';
        for (int i=0; i < stars*2+1; i++)
            cout << '*';

        c+= (m + 1);
        
        m = (spaces==size || spaces==0 ? -m : m);

        spaces += m;
        stars -= m;
        cout << endl;
        
     }
}
