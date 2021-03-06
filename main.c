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

extern void foo(int, float *, float *, float *);
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
	
	foo(NUM, a, b, c);

	printf("Vector a\n");
	for (i = 0; i < NUM; i++)
		printf("%f\n",a[i]);
	printf("\n");

	printf("Vector b\n");
	for (i = 0; i < NUM; i++)
		printf("%f\n",b[i]);
	printf("\n");
	
	printf("Vector c\n");
	for (i = 0; i < NUM; i++)
		printf("%f\n",c[i]);


	return 0; 
}
