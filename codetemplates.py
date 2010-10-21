func_template = '''
	.text
	.align 4, 0x90

	.global %(name)s
	%(name)s:
		pushl	%%ebp
		movl	%%esp, ebp
		pushl	%%ebx

%(body)s
	
	movl	-4(%%ebp), %%ebx
	leave
	ret
'''
