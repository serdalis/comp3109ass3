#include <stdio.h>
#include <stdlib.h> 
#include <math.h>
#include <time.h>

/* alignment macro: aligns a memory block a to multiplies of a */ 
#define align(s,a) (((size_t)(s) + ((a) - 1)) & ~((size_t) (a) - 1))
/* Alignment for SSE unit */ 
#define SSE_ALIGN (16)
/* Number of elements */ 
#define NUM (12)

extern void foo(int, float *, float *);
int main(void) 
{ 	
	int i;
	float *a = malloc(sizeof(float)*NUM + SSE_ALIGN),
		  *b = malloc(sizeof(float)*NUM + SSE_ALIGN),  
		  *c = malloc(sizeof(float)*NUM + SSE_ALIGN); 	
	/* make sure that pointers are aligned to multiplies of 16 bytes */
	a= 	(float *) align(a, SSE_ALIGN);
	b= 	(float *) align(b, SSE_ALIGN);
	c= 	(float *) align(c, SSE_ALIGN);
	
	foo(NUM, a, b);

	for (i = 0; i < NUM; i++)
		printf("Vector: a[%d] -> %f\n", i, a[i]);
	printf("\n");

	for (i = 0; i < NUM; i++)
		printf("Vector: b[%d] -> %f\n", i, b[i]);
	printf("\n", b[i]);

	for (i = 0; i < NUM; i++)
		printf("Vector: c[%d] -> %f\n", i, c[i]);


	return 0; 
}
