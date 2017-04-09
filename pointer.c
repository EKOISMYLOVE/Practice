#include <stdio.h>
int main()
{
    int test=1;
    int *point= NULL;

    //You can use int *point = %test;

    point=&test;

    printf("%p point value=test address. \n" , point);
    printf("%X test value. \n" , *point);
    printf("%p point address. \n" , &point);

    int **point2 = NULL;
    point2 = &point;

    printf("%p point2 value=point address. \n" , point2);
    printf("%p point2 address. \n" , &point2);
    
    return 0;
}
