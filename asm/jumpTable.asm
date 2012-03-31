;--------------------------------------------------------------------
; File:     jumpTable.asm
; Author:   (Andrew) Scott Grooms
; Date:     Mar 19, 2010
; Class:    COSC2425
;--------------------------------------------------------------------
%include "/tools/lib/asm_io.inc"

segment         .data

startMessage	db			'Enter a number between 1 and 4',0dh,0ah,0	
jumpTable		dd			item1
				dd			item2
				dd			item3
				dd			item4
tableSize		equ			$ - jumpTable
message1		db			'In command1',0dh,0ah,0
message2 		db      	'In command2',0dh,0ah,0
message3  		db     		'In command3',0dh,0ah,0
message4	  	db      	'In command4',0dh,0ah,0

segment         .text

				global          _asm_main
				extern			menu
				
_asm_main:

			push 			eax								;Saves values of registers
			push			ebx
			push			ecx
			mov				eax, startMessage
			call			print_string
		
			call			read_int						;user input

			mov				ebx, jumpTable
			dec     		eax								;Turns 1-4 to 0-3
			shl     		eax, 2							;Multiples by 4

			jmp				[ebx+eax]
			
item1:
			mov				eax, message1
			call			print_string
			jmp				endTable						;Break
item2:
			mov				eax, message2
			call			print_string	
			jmp				endTable						;Break
item3:
			mov				eax, message3
			call			print_string
			jmp				endTable						;Break
item4:
			mov				eax, message4
			call			print_string
			jmp				endTable						;Break
endTable:
			
			pop				ecx
			pop				ebx
     		pop 			eax								;Puts values back in registers
            ret