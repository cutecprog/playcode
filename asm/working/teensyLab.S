;---------------------------------------------------------------------
; Author: (Andrew) Scott Grooms
; File:   teensyLab
; Date:   04/25/2010
; Description:
; Blinks the LED on the teensy microcontroller in the sequence:
;   on for 1 second
;   off for 1/2 second
;   on for 1/2 second
;   off for 1 second
;   repeat continuously
;---------------------------------------------------------------------

.include "/Tools/lib/atmega32u4def.inc"

.section    	.data
		
trigger: 		.byte	0
		
.section    	.text
		
				.global	main
				.extern delay_500ms
				
			.org	    0x00
main:		jmp			start

start:
			ldi    		r16, 0x80
			ldi     	r17, 0x05
			sts     	CLKPR, r16
			sts     	CLKPR, r17
			sbi     	DDRD, 6
			cbi     	PORTD, 6
main_loop:
			sbi     	PORTD, 6
			rcall   	delay_500ms
			rcall   	delay_500ms
			cbi     	PORTD, 6
			rcall   	delay_500ms
			sbi			PORTD, 6
			rcall   	delay_500ms
			cbi			PORTD, 6
			rcall   	delay_500ms
			rcall   	delay_500ms
			rjmp    	main_loop
	
