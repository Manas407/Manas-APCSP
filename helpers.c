#include "helpers.h"
#include <stdio.h>
void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing

    for (int w = 0; w < width; w++)
    {
        for (int h = 0; h < height; h++)
        {
            if (image[h][w].rgbtBlue == 0 && image[h][w].rgbtRed == 0 && image[h][w].rgbtGreen == 0)
            {
                image[h][w].rgbtRed = 253;
                image[h][w].rgbtGreen = 48;
                image[h][w].rgbtBlue = 146;
            }
            // if i want random colors excluding white and black then i use a random number generation function and set parameters
            // for it to generate any number which isn't correlating to a black or white rgb value
        }
    }
}
