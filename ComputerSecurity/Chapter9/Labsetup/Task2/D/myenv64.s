ARGV equ 49 ; The place where argv[0] starts
section .text
  global _start
    _start:
	    BITS 64
	    jmp short two
    one:
 	    pop rbx           

      xor al, al
      mov [rbx+12],  al
      mov [rbx+22],  al
      mov [rbx+32],  al
      mov [rbx+ARGV-1],  al

      xor rax, rax
 	    mov [rbx+ARGV],  rbx  ; store rbx to memory at address rbx + 8
 	    mov [rbx+ARGV+8], rax  ; store rax to memory at address rbx + 16
      lea rcx, [rbx+13]
      mov [rbx+ARGV+16], rcx
      lea rcx, [rbx+23]
      mov [rbx+ARGV+24], rcx
      lea rcx, [rbx+33]
      mov [rbx+ARGV+32], rcx
      mov [rbx+ARGV+40], rax

      mov rdi, rbx       ; rdi = rbx
 	    lea rsi, [rbx+ARGV]   ; rsi = rbx + 8    
      lea rdx, [rbx+ARGV+16]
 	    mov rax, 0xFFFFFFFFFFFFFF3B        ; rax = 59
      shl rax, 56
      shr rax, 56
 	    syscall
     two:
        call one                                                                   
        db '/usr/bin/env', 0xFF ; The command string (terminated by a zero)
        db 'aaa=hello*'
        db 'bbb=world*'
        db 'ccc=hello world*'
        db 'AAAAAAAA'      ; Place holder for argv[0] 
        db 'BBBBBBBB'      ; Place holder for argv[1]
        db 'CCCCCCCC'
        db 'DDDDDDDD'
        db 'EEEEEEEE'
        db 'FFFFFFFF'
