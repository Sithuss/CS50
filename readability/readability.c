#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//declare blah blah blah..
int letters(string s);
int words(string s);
int sentences(string s);

int main(void)
{
    //user prompt text
    string t =  get_string("Text:");
    int letter =  letters(t);
    int word = words(t);
    int sentence = sentences(t);

//calculating Coleman-Liau index
    float index = (0.0588 * letter / word * 100) - (0.296 * sentence / word * 100) - 15.8;
    int inde = round(index);

// declaring the result
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
// declaring grade between 1 and 16
    {
        printf("Grade %i\n", index);
    }
}

//counting the letters
int letters(string s)
{
    int u = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
        if (isalpha(s[i]))
        {
            u++;
        }
    //return value letter count
    return u;
}

//counting the words
int words(string s)
{
    int l = 0;
    int word1 = 1;
    while (s[l] != '\0')
    {
        if (s[l] == 32 || s[l] == '\n')
        {
            word1++;
        }
        l++;
    }
    //return value word count
    return word1;
}

//couting the sentences
int sentences(string s)
{
    int v = 0;
    int sent = 0;
    while (s[v] != '\0')
    {
        if (s[v] == '!' || s[v] == '.' || s[v] == '?')
        {
            sent++;
        }
        v++;
    }
    //return value count sentence
    return sent;
}









