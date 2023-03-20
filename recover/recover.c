#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    //check more than two arguments
    if (argc != 2)
    {
        printf("Usage ./recover file\n");
        return 1;
    }
    FILE *infile = fopen(argv[1], "r");
    //if blank file, exists
    if (infile == NULL)
    {
        printf("Could not open \n");
        return 1;
    }
    //settig up values
    BYTE bytes[512];
    int counter = 0;
    char filename[8];
    FILE *img = NULL;
    //read the files
    while (fread(bytes, sizeof(BYTE), 512, infile) == 512)
    {
        //check jpeg or not
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            //count jpeg files
            if (counter == 0)
            {
                //create new file for jpeg
                sprintf(filename, "%03i.jpg", counter);
                //open new file
                img = fopen(filename, "w");
                //write on new file
                fwrite(bytes, sizeof(BYTE), 512, img);

                counter++;
            }
            else if (counter > 0)
            {
                //repeat steps for the next jpeg
                fclose(img);

                sprintf(filename, "%03i.jpg", counter);

                img = fopen(filename, "w");

                fwrite(bytes, sizeof(BYTE), 512, img);

                counter++;
            }
        }
        //continue writing until new jpeg found
        else if (counter > 0)
        {
            fwrite(bytes, sizeof(BYTE), 512, img);
        }
    }
    //close all files
    fclose(img);
    fclose(infile);
}