#include <stdlib.h> 

/* alignment macro: aligns a memory block a to multiplies of a */ 
#define align(s,a) ((size_t)((s) + ((a) - 1)) & ~((size_t) (a) - 1)) 
/* Alignment for SSE unit */ 
#define SSE_ALIGN (16)
/* Number of elements */ 
#define NUM (100) 

int main(void) 
{ 	
	float *a = malloc(sizeof(float)*NUM + SSE_ALIGN),
		  *b = malloc(sizeof(float)*NUM + SSE_ALIGN), 
		  *c = malloc(sizeof(float)*NUM + SSE_ALIGN); 	
	/* make sure that pointers are aligned to multiplies of 16 bytes */
	a= 	(float *) align(a, SSE_ALIGN);
	b= 	(float *) align(b, SSE_ALIGN);
	c= 	(float *) align(c, SSE_ALIGN);
	
	foo(NUM,a);
	return 0; 
}

