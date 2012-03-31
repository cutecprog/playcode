;--------------------------------------------------------------------
; File:     predureArgues.asm
; Author:   (Andrew) Scott Grooms
; Date:     Feb 21, 2010
; Class:    COSC2425
;
;--------------------------------------------------------------------
%include "/tools/lib/asm_io.inc"

segment         .data

segment         .text

                global           _asm_main
				
_asm_main:
            enter           0, 0				
			push 			eax
			push 			ebx
			
			mov				ebx, 7				;Moves 7 into ebx
			push			ebx					;Pushes ebx onto stack (enters parameter)
			call 			procedure			
			
			
			pop 			ebx
     		pop 			eax
            leave
            ret

procedure:
			push			ebp					;Pushes basic pointer onto the stack (saves)
			mov				ebp, esp 			;Moves the address of stack pointer in basic pointer
			mov 			eax,[ebp+8]			;Moves the value of the address of stack plus 8 bytes (gets parameter)
			call			print_int
			call			print_nl
			pop				ebp					;Pops ebp of stack (restores)
			ret				4					;Pops parameters off stack (deletes) and returns