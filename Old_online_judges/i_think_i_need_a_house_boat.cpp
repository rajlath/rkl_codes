#include <stdio.h> // Preprocessor Directive
#include <math.h>
#define M_PI 3.14159265
int num_props; // The number of test cases
float x, y; // X and Y Cartesian coordinates
int i;
double calc; // The area of the semicircle/50
int years; // The number of years
int main( )
{
    scanf("%d", &num_props);
    for (i = 1; i <= num_props; i++)
    {
        scanf("%f %f", &x, &y); // Input the i-th test case
        calc = (x*x + y*y)* M_PI / 2 / 50; // Calculate the area of the  emi-circle/50
        years = ceil(calc);
        printf("Property %d: This property will begin eroding in year %d.\n",i, years); //Output
    }
    printf("END OF OUTPUT.\n");
}