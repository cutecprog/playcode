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
			
			mov				ebx, 4				;num
			mov				ecx, 2				;power
			push			ebx					;enters parameter
			push			ecx
			call 			pow			
			
			call			print_int
			call			print_nl
			
			pop 			ebx
     		pop 			eax
            leave
            ret
			
;------------------------------------------------------
;Author: 		Scott Grooms
;Procedure:		pow*
;Parameters:	Two 32-bit values
;Returns:		Uses eax to return a value
;------------------------------------------------------
pow:
			push			ebp					;Pushes basic pointer onto the stack (saves)
			mov				ebp, esp 			;Moves the address of stack pointer in basic pointer
			;push			ebx
			;push			ecx
			;push			edx
			mov 			ebx,[ebp+12]		;gets parameter
			mov 			ecx,[ebp+8]
			mov				eax, 0
			mov				edx, ebx
powloop:
			add				edx, eax
			dec				ecx
			jz				powend
			
			push			edx
			push			ebx
			call 			multiply

			jmp				powloop
powend:
			mov				eax, edx
			;pop				edx
			;pop				ecx
			;pop				ebx
			pop				ebp					;Pops ebp of stack (restores)
			ret				8					;Pops parameters off stack (deletes) and returns
			
;------------------------------------------------------
;Author: 		Scott Grooms
;Procedure:		mulitiply
;Parameters:	Two 32-bit values
;Returns:		Uses eax to return a value
;------------------------------------------------------
multiply:
			push			ebp					;Pushes basic pointer onto the stack (saves)
			mov				ebp, esp 			;Moves the address of stack pointer in basic pointer
			push			ebx					;eax is not pushed b/c it will be used to return a value
			push			ecx
			mov 			eax,[ebp+12]		;gets parameter
			mov 			ebx,[ebp+8]
			mov				edx, eax
multloop:
			dec				ebx
			jz				multend
			add				eax, edx			
			jmp				multloop
multend:
			pop				ecx
			pop				ebx
			pop				ebp					;Pops ebp of stack (restores)
			ret				8					;Pops parameters off stack (deletes) and returns