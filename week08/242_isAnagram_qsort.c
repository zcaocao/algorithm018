#include <stdlib.h>
int cmp(const void * a, const void * b)
{
    return (*(char *)a - *(char *)b);
}

bool isAnagram(char * s, char * t)
{
    int len_s = strlen(s);
    int len_t = strlen(t);

    qsort(s, len_s, sizeof(char), cmp);
    qsort(t, len_t, sizeof(char), cmp);
    return strcmp(s, t) == 0;
}
