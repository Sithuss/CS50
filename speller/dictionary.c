// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"
#include <stdio.h>
#include <cs50.h>
#include <strings.h>
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

unsigned int word_count = 0;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int cursor = hash(word);
    node *chker = table[cursor];
    while (chker != NULL)
    {
        if (strcasecmp(chker->word, word) == 0)
        {
            return true;
        }
        chker = chker->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int length = strlen(word);
    unsigned int index = 0;
    for (int i = 0; i < length; i++)
    {
        index += tolower(word[i]);
        index = index % N;
    }
    return index;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Unable to open dictionary\n");
        return false;
    }
    char word[LENGTH + 1];
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    while (fscanf(input, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        n->next = NULL;
        int index = hash(word);
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }
        word_count++;
    }
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (word_count > 0)
        return word_count;
    else
        return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N ; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
