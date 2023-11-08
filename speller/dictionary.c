// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 29; // Using prime number instead of alphabet.

// Declaring variables.
unsigned int key;
unsigned int words;

// Hash table (array of pointers).
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    key = hash(word);
    node *ptr = table[key];

    // Now ptr is pointing to the first node of the hash table category (where the word looked at should be).

    while (ptr != 0)
    {
        if (strcasecmp(word, ptr -> word) == 0)
        {
            return true;
        }

        ptr = ptr -> next; // To iterate to next linked node if there's a linked list in that hash.
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long djb2 = 5381;
    int c;

    while ((c = tolower(*word++))) // Iterating characters.
    {

        djb2 = ((djb2 << 5) + djb2) + c; // Shifting 5 bits to the left multiplies faster by 32.
    }

    return djb2 % N;

    // Now the hash function doesn't arbitrarily favor any hash value (which would do if using only first letter to compute).
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        printf("Couldn't open %s\n", dictionary);
        return false;
    }

    char word[LENGTH + 1];

    // Keep scanning words until end of file (fscan returns EOF).
    while (fscanf(file, "%s", word) != EOF)
    {
        // Allocating memory for node.
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return false;
        }

        // Copying strings into the node.
        strcpy(n -> word, word);
        key = hash(word);
        n -> next = table[key]; // Pointing the node to the previous node (or hash if it's the first node).
        table[key] = n; // Pointing the hash to the last node added.

        words++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (words > 0)
    {
        return words;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr)
        {
            node *tmp = ptr; // Temp storage.
            ptr = ptr -> next; // Point next node.
            free(tmp);
        }
    }
    return true;
}
