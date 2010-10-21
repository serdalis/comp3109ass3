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

var_template = '''
	movl 8(%ebp), %eax # allocate local variables
	imull $4*<N>, %eax, %eax
	addl $15, %eax
	subl %eax, %esp

	movl 8+4*<N> (%ebp), <destreg>

	movl 8(%ebp), <destreg>
	imull $4*<N>, <destreg>, <destreg>
	addl $16, <destreg>
	subl %ebp, <destreg>
	negl <destreg>
	sub $15, <destreg>
	andl $-16, <destreg>

	movl $.const<X>, <destreg>

	.data
	.align 16
	.const<X>:
		.float <X>
		.float <X>
		.float <X>
		.float <X>
'''

equ_template = '''
	<load source address into %eax>
	<load destination address into %edx>

	movl 8(%ebp), %ecx
	shrl $2, %ecx
	jz .loop_end<X>

	.loop_begin<X>:
		movaps (%eax), %xmm0
		movaps %xmm0, (%edx)

		addl $16, %eax #add this line if %eax is not pointing to a constant
		addl $16, %edx
		loopl .loop_begin<X>
	.loop_end<X>:
'''
equWithOp_template = '''
	<load source1 address into %eax>
	<load source2 address into %ebx>
	<load destination address into %edx>

	movl 8(%ebp), %ecx
	shrl $2, %ecx
	jz .loop_end<X>

	.loop_begin<X>:
		movaps (%eax), %xmm0
		movaps (%ebx), %xmm1
		<operation> %xmm0, %xmm1
		movaps %xmm1, (%edx)

		addl $16, %eax #add this line if %eax is not pointing to a constant
		addl $16, %ebx #add this line if %ebx is not pointing to a constant
		addl $16, %edx
		loopl .loop_begin<X>
	.loop_end<X>:
'''
invoke_template = '''
	# invoke function <name>
	subl $4*<N+1>, %esp # grow the stack
	movl <argN>, %eax # setup argN
	movl %eax, <4*N>(%esp)
...
	movl <arg1>, %eax # setup arg1
	movl %eax, 4(%esp)
	movl 8(%ebp), %eax # setup implicit vector length
	movl %eax, 0(%esp)
	call <name> # invoke the function
	addl $4*<N+1>, %esp # restore the stack
'''
