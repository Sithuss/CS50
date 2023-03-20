#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //testing argc
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
//testing keylength
    int n = strlen(argv[1]);
    if (n != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    //testing alphabet and repeated characters
    for (int i = 0; i < n; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        for (int j = i + 1; j < n; j++)
        {
            if (argv[1][j] == argv[1][i])
            {
                printf("Key must not contain repeated characters\n");
                return 1;
            }
        }
    }

    string key = argv[1];
    //prompt user plain text
    string plain = get_string("plane text: ");

    printf("ciphertext: ");
//loading cipher test
    for (int l = 0, m = strlen(plain); l < m; l++)
    {
        //for upper csae character
        if (isupper(plain[l]))
        {
            int en = plain[l] - 65;
            printf("%c", toupper(key[en]));
        }
        //for lowercase character
        else if (islower(plain[l]))
        {
            int en = plain[l] - 97;
            printf("%c", tolower(key[en]));
        }
        else if (!isalpha(plain[l]))
        {
            printf("%c", plain[l]);
        }
    }
    //move cursor to next line
    printf("\n");
}

