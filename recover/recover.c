#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

// Define block size.
#define BLOCK_SIZE 512

// Define new type to store data.
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Making sure of image name usage in the CLI.
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Opening the file in read mode and keeping track of location.
    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }

    // Declaring needed variables.
    int jpg_n = 0; // Counter.
    uint8_t buffer[BLOCK_SIZE]; // Buffer array to store data in upper typedef.
    char jpg_nm[8];
    FILE *out = NULL;
    bool jpg = false;

    // Reading image in blocks.
    while (fread(buffer, BLOCK_SIZE, 1, file) == 1)
    {
        // Check block start to find the start of new JPG.
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        // (buffer[3] & 0xf0) == 0xe0) means that the condition is matched if buffer[3] is anything between 0xe0 and 0xf0.
        {
            // Close previous file if open.
            if (jpg)
            {
                fclose(out);
            }
            //
            else
            {
                jpg = true;
            }

            // Open new file named with 3 integers ending in the counter of previously opened JPGs.
            sprintf(jpg_nm, "%03d.jpg", jpg_n); // %3d gives three decimals at jpg_nm before jpg_n.
            out = fopen(jpg_nm, "w"); // W to write.

            // If file cannot be opened, return 2.
            if (out == NULL)
            {
                fclose(file);
                printf("Could not create file\n");
                return 2;
            }

            jpg_n++;
        }

        // Write block to JPG.
        if (jpg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, out);
        }
    }

    // Close image file and last JPG.
    fclose(file);
    if (jpg)
    {
        fclose(out);
    }

    return 0;

}