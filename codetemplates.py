from string import Template

# assign function

func_template = Template('''
.text
.align 4, 0x90

.global $name
	$name:
		pushl	%%ebp
		movl	%%esp, %%ebp
		pushl	%%eax
		
$body

	pop %%eax
	leave
	ret
''')

#allocate local variables has to be generated first in functions
setdefine_template = Template('''
	movl 8(%%ebp), %%eax
	imull $$4, %%eax, %%eax
	addl $$16, %%eax
	imull $$$var_num, %%eax, %%eax
	subl %%eax, %%esp
	andl $$-16, %%esp

	$body
	
	movl %%ebp, %%eax
	subl $$4, %%eax
	movl %%eax, %%esp
	
''')
# place parameter var_num into destreg
par_template = Template('''
	movl 8+4*$var_num (%%ebp), %destreg
''')

# place local var_num into destreg
getdefine_template = Template('''
	movl 8(%%ebp), %destreg
	imull $$4, %destreg, %destreg
	addl $$16, %destreg
	imull $$$var_num, %destreg, %destreg
	subl %%ebp, %destreg
	negl %destreg
	andl $$-16, %destreg
''')

# place constant val into destreg
constaddr_template = Template('''
	movl $$.const$val, %destreg
''')

consttable_template = Template('''
.data
.align 16
.const$val:
	.float $val
	.float $val
	.float $val
	.float $val
''')

# ident = factor
equ_template = Template('''
	movl $sourceaddr, %%ebx
	movl $destaddr, %%eax
	

	movl 8(%%ebp), %%ecx
	shrl $$2, %%ecx
	jz .loop_end<X>

.loop_begin<X>:
	movaps (%%ebx), %%xmm0
	movaps %%xmm0, (%%eax)

	addl $$16, %%eax #add this line if %%eax is not pointing to a constant
	addl $$16, %%ebx
	loopl .loop_begin<X>
.loop_end<X>:
''')

# ident = factor OP factor
equWithOp_template = '''
	movl $sourceaddr1, %%ebx
	movl $sourceaddr2, %%edx
	movl $destaddr, %%eax

	movl 8(%%ebp), %%ecx
	shrl $$2, %%ecx
	jz .loop_end<X>

.loop_begin<X>:
	movaps (%%eax), %%xmm0
	movaps (%%ebx), %%xmm1
	$operation %%xmm0, %%xmm1
	movaps %%xmm1, (%%edx)

	addl $$16, %%eax #add this line if %%eax is not pointing to a constant
	addl $$16, %%ebx #add this line if %%ebx is not pointing to a constant
	addl $$16, %%edx
	loopl .loop_begin<X>
.loop_end<X>:
'''
#invoke a function
invoke_template = '''
	# invoke function <name>
	subl $$4*<N+1>, %%esp # grow the stack
	movl <argN>, %%eax # setup argN
	movl %%eax, <4*N>(%%esp)
	movl <arg1>, %%eax # setup arg1
	movl %%eax, 4(%%esp)
	movl 8(%%ebp), %%eax # setup implicit vector length
	movl %%eax, 0(%%esp)
	call <name> # invoke the function
	addl $$4*<N+1>, %%esp # restore the stack
'''
