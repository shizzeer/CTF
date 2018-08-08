section .text
global _start

_start:
	mov eax, 0x8048540    ; store the address of win function in the eax
	call eax              ; jump to this address and call this function
