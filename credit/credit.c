#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user number
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);
//assigning each digit in card number
    int d1;
    int d2;
    int d3;
    int d4;
    int d5;
    int d6;
    int d7;
    int d8;
    int d9;
    int d10;
    int d11;
    int d12;
    int d13;
    int d14;
    int d15;
    int d16;
// calculating each digit value
    d1 = number % 10;
    d2 = (number / 10) % 10;
    d3 = (number % 1000) / 100;
    d4 = (number % 10000) / 1000;
    d5 = (number % 100000) / 10000;
    d6 = (number % 1000000) / 100000;
    d7 = (number % 10000000) / 1000000;
    d8 = (number % 100000000) / 10000000;
    d9 = (number % 1000000000) / 100000000;
    d10 = (number % 10000000000) / 1000000000;
    d11 = (number % 100000000000) / 10000000000;
    d12 = (number % 1000000000000) / 100000000000;
    d13 = (number % 10000000000000) / 1000000000000;
    d14 = (number % 100000000000000) / 10000000000000;
    d15 = (number % 1000000000000000) / 100000000000000;
    d16 = (number % 10000000000000000) / 1000000000000000;

// solving with Luhn's algorithm
    int m2 = d2 * 2;
    int s2 = ((m2 / 10) % 10) + (m2 % 10);
    int m4 = d4 * 2;
    int s4 = ((m4 / 10) % 10) + (m4 % 10);
    int m6 = d6 * 2;
    int s6 = ((m6 / 10) % 10) + (m6 % 10);
    int m8 = d8 * 2;
    int s8 = ((m8 / 10) % 10) + (m8 % 10);
    int m10 = d10 * 2;
    int s10 = ((m10 / 10) % 10) + (m10 % 10);
    int m12 = d12 * 2;
    int s12 = ((m12 / 10) % 10) + (m12 % 10);
    int m14 = d14 * 2;
    int s14 = ((m14 / 10) % 10) + (m14 % 10);
    int m16 = d16 * 2;
    int s16 = ((m16 / 10) % 10) + (m16 % 10);
//making checksum
    int sum1 = s2 + s4 + s6 + s8 + s10 + s12 + s14 + s16;
    int chksum =  sum1 + d1 + d3 + d5 + d7 + d9 + d11 + d13 + d15;
    printf("%i\n", chksum);
//declare card type if the card is valid
    //for visa type
    if (chksum % 10 <= 0)
    {
        if ((d13 == 4 || d14 == 4 || d15 == 4 || d16 == 4))
        {
            printf("VISA\n");
        }
        //for master card type
        else if ((d16 == 5 && d15 == 1) || (d16 == 5 && d15 == 2) || (d16 == 5 && d15 == 3) || (d16 == 5 && d15 == 4) || (d16 == 5
                 && d15 == 5))
        {
            printf("MASTERCARD\n");
        }
        //for American express card type
        else if ((d15 == 3 && d14 == 4) || (d15 == 3 && d14 == 7))
        {
            printf("AMEX\n");
        }
        //if valid cards don't match the situation reject
        else
        {
            printf("INVALID\n");
        }
    }
    //if chksum is not equal 0 than invalid
    else
    {
        printf("INVALID\n");
    }
}

