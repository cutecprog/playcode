%include "/tools/lib/asm_io.inc"

segment         .data
	
segment         .text

				global          factorial
				
;------------------------------------------------------
;Author: 		Professor Black
;Procedure:		factorial
;Parameters:	eax
;Returns:		eax
;Description:	Computes the factorial of the parameter 
;				in eax, and returns the value in eax.
;------------------------------------------------------	

factorial:
    push ebx            ; save caller's registers
    push edx
    cmp eax, 0
    jnz non_base
base_case:
    mov eax, 1          ; return the base value
    pop edx             ; restore the caller's registers
    pop ebx
    ret
non_base:
    push eax            ; save the input number for a moment
    sub eax, 1          ; subtract one for the recursive call
    call    factorial   ; recursive call, result is in eax on return
    pop ebx             ; recover the input number into ebx
    mul ebx             ; form this result in eax using mul
    pop edx             ; restore caller's registers
    pop ebx
    ret