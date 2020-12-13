#include <stdio.h>

void swap (int *x, int *y) 
{
    int t = *x;
    *x = *y;
    *y = t;
}

int partition (int arr[], int begin, int end)
{
    // pivot标杆位置，counter：小于pivot的元素个数
    int pivot = end, counter = begin;
    for (int i = begin; i < end; i++)
    {
        if (arr[i] < arr[pivot])
        {
            swap(&arr[i], &arr[counter]);
            counter++;
        }
    }
    swap(&arr[counter], &arr[pivot]);
    return counter;
}

void quick_sort (int arr[], int begin, int end)
{ 
    if (end <= begin) return;
    int pivot = partition(arr, begin, end);
    quick_sort(arr, begin, pivot - 1);
    quick_sort(arr, pivot + 1, end);
}

int main() {
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int len = (int) sizeof(arr) / sizeof(*arr);
    quick_sort(arr, 0, len - 1);
    int i;
    for (i = 0; i < len; i++)
        printf("%d ", arr[i]);
    return 0;
}
