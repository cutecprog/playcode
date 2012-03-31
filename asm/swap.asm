;--------------------------------------------------------------------
; File:     lab4.asm
; Author:   (Andrew) Scott Grooms
; Date:     Feb 21, 2010
; Class:    COSC2425
;
;	data validation isn't perform in these program
;   this program will only work with integers and will take up to 4
;	user can simply end program before entering 4 integers by entering
;	CR.
;--------------------------------------------------------------------
%include "/tools/lib/asm_io.inc"

segment         .data

segment         .text

                global           _asm_main
				
_asm_main:
            enter           0, 0				;
			push 			eax
			push 			ebx
			
			mov				eax, 7
			mov				ebx, 10
			
			call			print_int
			call			print_nl
			
			XOR				eax, ebx
			XOR				ebx, eax
			XOR				eax, ebx
			
			
			call			print_int
			call			print_nl
			
			pop 			ebx
     		pop 			eax
            leave
            ret

