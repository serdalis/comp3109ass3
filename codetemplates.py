from string import Template

# assign function

func_template = Template('''#FUNCTION $name
.text
.align 4, 0x90

.global $name
$name:
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%eax
	
$body

pop %eax
leave
ret
''')

#allocate local variables has to be generated first in functions
setdefine_template = Template('''
#setdefine for $var_num variables	
	movl 8(%ebp), %eax
	imull $$4, %eax, %eax
	addl $$16, %eax
	imull $$$var_num, %eax, %eax
	subl %eax, %esp
	andl $$-16, %esp
	$body	
#Shrink stack
	movl %ebp, %eax
	subl $$4, %eax
	movl %eax, %esp
	
''')
# place parameter var_num into destreg
par_template = Template('''
#placing address of $var_num into %(destreg)s
	movl 8+4*$var_num (%%ebp), %(destreg)s
''')

# place local var_num into destreg
getdefine_template = Template('''
#placing address of local variable $var_num into %(destreg)s
	movl 8(%%ebp), %(destreg)s
	imull $$4, %(destreg)s, %(destreg)s
	addl $$16, %(destreg)s
	imull $$$var_num, %(destreg)s, %(destreg)s
	subl %%ebp, %(destreg)s
	negl %(destreg)s
	andl $$-16, %(destreg)s
''')

# place constant val into destreg
constaddr_template = Template('''
#placing address of const $val into %(destreg)s
	movl $$.const$val, %(destreg)s
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
#ident = factor
	$sourceaddr
	$destaddr

	movl 8(%ebp), %ecx
	shrl $$2, %ecx
	jz .loop_end$loop_val

.loop_begin$loop_val:
	movaps (%ebx), %xmm0
	movaps %xmm0, (%eax)

	$ifnot_constant
	addl $$16, %eax
	loopl .loop_begin$loop_val
.loop_end$loop_val:
''')

# ident = factor OP factor
equWithOp_template = Template('''
#ident = factor OP factor
	$sourceaddr_1
	$sourceaddr_2
	$destaddr

	movl 8(%ebp), %ecx
	shrl $$2, %ecx
	jz .loop_end$loop_val

.loop_begin$loop_val:
	movaps (%ebx), %xmm0
	movaps (%edx), %xmm1
	$operation %xmm1, %xmm0
	movaps %xmm0, (%eax)

	$ifnot_constant_1
	$ifnot_constant_2
	addl $$16, %eax
	loopl .loop_begin$loop_val
.loop_end$loop_val:
''')

#invoke a function
invoke_template = Template('''
#invoke function $name
	subl $$4*$Nplus1, %esp # grow the stack
	$args
	movl 8(%ebp), %eax # setup implicit vector length
	movl %eax, 0(%esp)
	call $name
	addl $$4*$Nplus1, %esp # restore the stack
''')