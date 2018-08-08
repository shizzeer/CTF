section .text
global _start

_start:
	xor eax, eax        
	push eax            ; Push NULL bytes on the stack
	push 0x68732f2f     ; Push 'hs//' on the stack because of little endian
	push 0x6e69622f     ; Push 'nib/' on the stack because of little endian	
	mov ebx, esp        ; Move address of the '/bin//sh' to the ebx register
	push eax            ; Push NULL bytes on the stack again
	mov edx, esp        ; Move address of NULL bytes to the edx register
	push ebx            ; Push address of the string '/bin//sh' on the stack again
	mov ecx, esp        ; Move address of address of the string to ecx
	xor eax, eax
	mov al, 11          ; execve syscall
	int 0x80            ; call kernel

