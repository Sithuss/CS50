#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            int average = round((red + green + blue) / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;

        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            float counter = 0.00;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k < 0 || i + k > height - 1 || j + l < 0 || j + l > width - 1)
                    {
                        continue;
                    }
                    red += image[i + k][j + l].rgbtRed;
                    green += image[i + k][j + l].rgbtGreen;
                    blue += image[i + k][j + l].rgbtBlue;
                    counter++;
                }
            }
            tmp[i][j].rgbtRed = round(red / counter);
            tmp[i][j].rgbtGreen = round(green / counter);
            tmp[i][j].rgbtBlue = round(blue / counter);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmp[i][j].rgbtRed;
            image[i][j].rgbtGreen = tmp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = tmp[i][j].rgbtBlue;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redx = 0;
            int greenx = 0;
            int bluex = 0;
            int redy = 0;
            int greeny = 0;
            int bluey = 0;
            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    //skip invalid pixels
                    if (i + k - 1 < 0 || i + k - 1 > height - 1 || j + l - 1 < 0 || j + l - 1 > width - 1)
                    {
                        continue;
                    }
                    redx += (image[i + k - 1][j + l - 1].rgbtRed * gx[k][l]);
                    greenx += (image[i + k - 1][j + l - 1].rgbtGreen * gx[k][l]);
                    bluex += (image[i - 1 + k][j - 1 + l].rgbtBlue * gx[k][l]);

                    redy += (image[i + k - 1][j + l - 1].rgbtRed * gy[k][l]);
                    greeny += (image[i + k - 1][j + l - 1].rgbtGreen * gy[k][l]);
                    bluey += (image[i + k - 1][j + l - 1].rgbtBlue * gy[k][l]);
                }
            }
            int red = round(sqrt((redx * redx) + (redy * redy)));
            int green = round(sqrt((greenx * greenx) + (greeny * greeny)));
            int blue = round(sqrt((bluex * bluex) + (bluey * bluey)));
            //check exceeded value
            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            tmp[i][j].rgbtRed = red;
            tmp[i][j].rgbtGreen = green;
            tmp[i][j].rgbtBlue = blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmp[i][j].rgbtRed;
            image[i][j].rgbtGreen = tmp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = tmp[i][j].rgbtBlue;
        }
    }
}
