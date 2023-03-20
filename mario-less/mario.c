#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        //prompt user
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    //looping
    for (int i = 0; i < h; i++)
    {   //adding spaces
        for (int l = 0; l < h - i - 1; l ++)
        {
            printf(" ");
        }
        //making hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        //next line
        printf("\n");
    }
}

