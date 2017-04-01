.data
buf:
	.long 0x00c105ed
str1:
	.string "coolfood"
.global your_asm_fn
.text
your_asm_fn:

push	%ebp
mov	%esp,%ebp

lea   str1, %eax
push  %eax

lea   buf, %eax
push  %eax

push  $0xacce55ed
call practice


leave
ret

