#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //testing argc
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //testing argv[1] contains other chars rather than digit
    for (int i = 0, n = strlen(argv[1]); i < n ; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int num = atoi(argv[1]);
//user prompt plain text
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");
    //output cipher test
    for (int l = 0, m = strlen(plain); l < m; l++)
    {
        //for upper character
        if (isupper(plain[l]))
        {
            char cipher = (((plain[l] + num) - 'A') % 26) + 'A';
            printf("%c", cipher);
        }
        //for lower cipher characters
        else if (islower(plain[l]))
        {
            char cipher = (((plain[l] + num) - 'a') % 26) + 'a';
            printf("%c", cipher);
        }
        else
            //for other characters
        {
            printf("%c", plain[l]);
        }
    }
    printf("\n");
}