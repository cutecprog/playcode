;---------------------------------------------------------------------
; Author: (Andrew) Scott Grooms
; File:   usb_util
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

.section    	.text
		
				.global	delay_500ms

;---------------------------------------------------------------------
; Procedure:   	delay_500ms
; Parameters:  	none
; Returns:	   	none
; Description: 	This procedure delays for half a second in returns.
;---------------------------------------------------------------------	
delay_500ms:
			ldi     	r16, 20
dl1:
			ldi     	r18, 250
dl2:
			dec     	r16
			brne    	dl2
			dec     	r17
			brne    	dl1
			ret