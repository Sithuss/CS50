#include <cs50.h>
#include <stdio.h>

int main(void)
{
// prompt user input
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1  || n > 8);

//making height of the pyramid
    for (int i = 0; i < n; i++)
    {
        //making spaces for left side
        for (int r = 0; r < n - i - 1; r++)
        {
            printf(" ");
        }
        //making left side
        for (int m = 0; m <= i ; m++)
        {
            printf("#");
        }
        //make 2 spaces
        printf("  ");
        //makeing right side
        for (int v = 0; v <= i ; v++)
        {
            printf("#");
        }
        printf("\n");
    }
}