section .text
global _start
  _start:
    xor  rdx, rdx       ; 3rd argument (stored in rdx)

    ;First argument
    push rdx
    mov rax, 'h*******'
    shl rax, 56
    shr rax, 56
    push rax
    mov rax,'/bin/bas'  
    push rax
    mov rdi, rsp        ; 1st argument (stored in rdi)

    ;Second argument
    push rdx
    mov rax, '-c******'
    shl rax, 48
    shr rax, 48
    push rax
    mov rbx, rsp

    ;Third argument
    push rdx
    mov rax, 'la;*****'
    shl rax, 40
    shr rax, 40
    push rax
    mov rax, 'lo; ls -'
    push rax
    mov rax, 'echo hel'
    push rax
    mov rcx, rsp

    ;argv array (make sure to put in the addresses and not the values)
    push rdx
    push rcx
    push rbx
    push rdi
    mov rsi, rsp        ; 2nd argument (stored in rsi)

    xor  rax, rax
    mov  al, 59        ; execve()
    syscall
