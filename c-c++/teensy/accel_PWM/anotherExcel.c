/*
* ----------------------------------------------------------------------------
* Simple ADXL reading, connected to ICP pin
* ----------------------------------------------------------------------------
*/

#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/signal.h>
//#include "delay.h"

volatile int up = 0x01;
volatile uint16_t duration;
volatile int GForce;
int ZEROVALUE = 3789;

//Timer has overflowed - takes 8ms
SIGNAL (SIG_OVERFLOW1)
{
   // Shouldn't happen in the range the ADXL is spitting out
}

// Rising edge detected
SIGNAL (SIG_INPUT_CAPTURE1 )
{
   if(up ==1)
   {
      // 1/8 Prescaler, rising edge detected
      TCCR1B =  _BV (CS11);   
      up = 0;
      TCNT1 = 0;
   }
   else
   {
      // 1/8 Prescaler, falling edge detected
      TCCR1B =  _BV (CS11) | _BV (ICES1);
      up = 1;
      duration = TCNT1;
   }

}

void ioinit (void)
{
   // Timer 1 is setup at 1/8 prescaler, with input capture enabled.
   // 1/8 Prescaler, input capture + noise cancelling
   TCCR1B =  _BV (CS11) | _BV (ICES1) | _BV (ICNC1);	

   // enable timer 1
   timer_enable_int (_BV (TOIE1) | _BV (TICIE1)); 

   // enable interrupts
   sei();											
}

int main (void)
{
   ioinit();
   PORTB = 0xFF;

   // loop forever, the interrupts are doing the rest
   while(1)
   {
      if(duration < 5000)               	// Only if the value has changed
      {
         GForce = duration - ZEROVALUE;   	// Zero value is the value the ADXL is putting out at 0g
											// Ideally this should be set through some sort of calibration sequence
         duration = 5000;            		// Using a ADXL202, the acceleration should never read this high,
											// so it's a good invalid value to indicate whether the value has changed
      }
   }
   return (0);
}