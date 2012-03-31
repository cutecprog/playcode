;---------------------------------------------------------------------
; Author: (Andrew) Scott Grooms
; File:	  button_hold.S
; Date:   05/09/2010
; Description:
; This file is a simple hold button example, hardware setup:
; 	Connect switch or button to pin c0 and ground.
;---------------------------------------------------------------------

.include "/Tools/lib/atmega32u4def.inc"

.equ		LED_PIN,	6					; Pin for LED.
.equ		SWIT_PIN,	0					; Pin for switch.
	
.section    .text

			.org	    0x00
			jmp			start

start:
			sbi     	DDRD, LED_PIN		; Sets the LED pin to be an output.
			cbi     	PORTD, LED_PIN		; Turns off LED.
			cbi			DDRC, SWIT_PIN		; Sets the switch pin to be an input.
			sbi			PORTC, SWIT_PIN		; Sets input mode to pull resistor.
			
main_loop:
			sbis		PINC, SWIT_PIN		; Skips if switch pin is high.
			sbi     	PORTD, LED_PIN		; Turns on LED.
			cbi			PORTD, LED_PIN		; Turns off LED.
			rjmp    	main_loop