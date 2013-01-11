#include <iostream>
#include <math.h>
#include <time.h>

using namespace std;

#define DAYS_IN_YEAR 10000

struct data {
    int date;
    double AMD[DAYS_IN_YEAR];
    double INT[DAYS_IN_YEAR];
    double ARM[DAYS_IN_YEAR]; 
};

void setMarket(data &m);
void printMarket(const data &m, ostream &);
double investMarket(data &m, double fund, ostream &);
double investMarket2(data &m, double fund, ostream &);
double avgCom(double *);

int main()
{
    double fund, total;
    data market;
    
    cout << "Investor" << endl;
    cout << "Enter start: ";
    cin >> fund;
    
    for(int i=0; i<16; i++) {
         setMarket(market);
         total += investMarket2(market, fund, cout);
    }
    
    cout << "You have: " << total/16 << endl;
    
    system("pause");
    
    /*cout << endl << "Market" << endl;
    printMarket(market, cout);
    
    system("pause");*/
    return 0;
}

void setMarket(data &m)
{
     srand(time(0));
     m.AMD[0] = 500.0 + rand()%500;
     m.INT[0] = 500.0 + rand()%500;
     m.ARM[0] = 500.0 + rand()%500;
     
     for(int i=1; i<DAYS_IN_YEAR; i++)
          m.AMD[i] = 750;
     for(int i=1; i<DAYS_IN_YEAR; i++)
          m.INT[i] = 750;
     for(int i=1; i<DAYS_IN_YEAR; i++)
          m.ARM[i] = 750;     
     
     //cout << m.AMD[0] << endl << m.INT[0] << endl << m.ARM[0] << endl;
}

void printMarket(const data &m, ostream & out)
{
     for(int i=0; i<DAYS_IN_YEAR/2; i++) {
          out << i+1 << ":\t";
          out << m.AMD[i] << '\t';
          out << m.INT[i] << '\t';
          out << m.ARM[i] << endl;
     }
     
     system("pause");
     
     for(int i=DAYS_IN_YEAR/2; i<DAYS_IN_YEAR; i++) {
          out << i+1 << ":\t";
          out << m.AMD[i] << '\t';
          out << m.INT[i] << '\t';
          out << m.ARM[i] << endl;
     }

}

double investMarket(data &m, double fund, ostream & out)
{
      srand(time(0));
      
      int invAMD = 0;
      int invINT = 0;
      int invARM = 0;
      
      int numTrades = 0;
      
      m.AMD[0] = 500.0 + rand()%500;
      m.INT[0] = 500.0 + rand()%500;
      m.ARM[0] = 500.0 + rand()%500;
      
      for(int i=0; i<DAYS_IN_YEAR; i++) {
            m.AMD[i+1] = 500.0 + rand()%500 + invAMD + (m.AMD[i]-750);
            m.INT[i+1] = 500.0 + rand()%500 + invINT + (m.INT[i]-750);
            m.ARM[i+1] = 500.0 + rand()%500 + invARM + (m.ARM[i]-750);
            
            if(invAMD && m.AMD[i] >= avgCom(m.AMD)) {
                fund += 1*(m.AMD[i]/m.AMD[i-1]) * invAMD;
                m.AMD[i] -= 1*(m.AMD[i]/m.AMD[i-1]) * invAMD;
            }
            if(invINT && m.INT[i] >= avgCom(m.INT)) {
                fund += 1*(m.INT[i]/m.INT[i-1]) * invINT;
                m.INT[i] -= 1*(m.INT[i]/m.INT[i-1]) * invINT;
            }
            if(invARM && m.ARM[i] >= avgCom(m.ARM)) {
                fund += 1*(m.ARM[i]/m.ARM[i-1]) * invARM;
                m.ARM[i] -= 1*(m.ARM[i]/m.ARM[i-1]) * invARM;
            }
                
            if(invAMD && m.AMD[i] >= avgCom(m.AMD) || invAMD && m.AMD[i] >= avgCom(m.AMD) || invAMD && m.AMD[i] >= avgCom(m.AMD))
                 out << i+1 << ":\t" << fund << endl;
                 
           if(fund > 0) {
               if(m.AMD[i] < avgCom(m.AMD)*(3/4)) {
                    fund-=1.012; // Include broker fee
                    invAMD++;
                    numTrades++;
               } else 
                    invAMD = 0;
               
               if(m.INT[i] < avgCom(m.INT)*(3/4)) {
                    fund-=1.012; // Include broker fee
                    invINT++;
                    numTrades++;
               } else 
                    invINT = 0;
                    
               if(m.ARM[i] < avgCom(m.ARM)*(3/4)) {
                    fund-=1.012; // Include broker fee
                    invARM++;
                    numTrades++;
               } else 
                    invARM = 0;
           }
      }
      
      out << "LD:\t" << fund << endl;
      out << "# of trades: " << numTrades << "\tBroker fee: " << (numTrades*0.012) << endl;
      
      fund += 1*(m.AMD[DAYS_IN_YEAR-1]/m.AMD[DAYS_IN_YEAR-2]) * invAMD;
      fund += 1*(m.INT[DAYS_IN_YEAR-1]/m.INT[DAYS_IN_YEAR-2]) * invINT;
      fund += 1*(m.ARM[DAYS_IN_YEAR-1]/m.ARM[DAYS_IN_YEAR-2]) * invARM;
               
      out << "\nSell all\nAMD:\t" << (m.AMD[DAYS_IN_YEAR-1]/m.AMD[DAYS_IN_YEAR-2]) * invAMD << endl
          << "INT:\t" << (m.INT[DAYS_IN_YEAR-1]/m.INT[DAYS_IN_YEAR-2]) * invINT << endl
          << "ARM:\t" << (m.ARM[DAYS_IN_YEAR-1]/m.ARM[DAYS_IN_YEAR-2]) * invARM << endl;
      
      return fund;
}

double investMarket2(data &m, double fund, ostream & out)
{
      srand(time(0));
      
      int invAMD = 0;
      
      int numTrades = 0;
      
      m.AMD[0] = 500.0 + rand()%500;
      
      for(int i=0; i<DAYS_IN_YEAR; i++) {
            m.AMD[i+1] = 500.0 + rand()%500 + invAMD + (m.AMD[i]-750);
            
            if(invAMD && m.AMD[i] >= avgCom(m.AMD)) {
                fund += 1*(m.AMD[i]/m.AMD[i-1]) * invAMD;
                m.AMD[i] -= 1*(m.AMD[i]/m.AMD[i-1]) * invAMD;
                out << i+1 << ":\t" << fund << endl;
            }                 
                 
           if(fund > 0) {
               if(m.AMD[i] < avgCom(m.AMD)*(3/4)) {
                    fund-=1.012; // Include broker fee
                    invAMD++;
                    numTrades++;
               } else 
                    invAMD = 0;
           }
      }
      
      out << "LD:\t" << fund << endl;
      out << "# of trades: " << numTrades << "\tBroker fee: " << (numTrades*0.012) << endl;
      
      fund += 1*(m.AMD[DAYS_IN_YEAR-1]/m.AMD[DAYS_IN_YEAR-2]) * invAMD;
               
      out << "\nSell all\nAMD:\t" << (m.AMD[DAYS_IN_YEAR-1]/m.AMD[DAYS_IN_YEAR-2]) * invAMD << endl;
      
      return fund;
}

double avgCom(double *a)
{
     double sum = 0;
     for(int i=0; i<DAYS_IN_YEAR; i++)
          sum += a[i];
     return (sum/DAYS_IN_YEAR);
}
