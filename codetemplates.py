# assign function
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
#allocate local variables has to be generated first in functions
alloclocal_template = '''
	movl 8(%%ebp), %%eax
	imull $4, %%eax, %%eax
	addl $16, %%eax
	imull $<%(var_num)s>, %%eax, %%eax
	subl %%eax, %%esp
	andl $-16, %%esp
'''
# place parameter var_num into destreg
par_template = '''
	movl 8+4*%(var_num)s (%%ebp), %%eax

'''
# place local var_num into destreg
localaddr_template = '''
	movl 8(%%ebp), %%eax
	imull $4s, %%eax, %%eax
	addl $16, %%eax
	imull $<%(var_num)s>, %%eax, %%eax
	subl %ebp, %(destreg)s
	negl %(destreg)s
	sub $15, %(destreg)s
	andl $-16, %(destreg)s
'''
# place constant val into destreg
const_template = '''
	movl $.const%(val)s, %(destreg)s

	.data
	.align 16
	.const%(val)s:
		.float %(val)s
		.float %(val)s
		.float %(val)s
		.float %(val)s
'''
# ident = factor
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
# ident = factor OP factor
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
#invoke a function
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
