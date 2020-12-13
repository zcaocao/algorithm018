#include <stdio.h>

void shell_sort(int arr[], int len) 
{
    int gap, i, j;
    int temp;
    for (gap = len >> 1; gap > 0; gap >>= 1) 
    {   printf("gap=%d \n", gap);
        for (i = gap; i < len; i++) 
        {
            temp = arr[i];
            printf("i=%d, temp=%d \n", i, temp);
            for (j = i - gap; j >= 0 && arr[j] > temp; j -= gap)
            {
                printf("j=%d; i-gap=%d, j+gap=%d; arr[j+gap]=%d; arr[j]=%d \n", j, i-gap, j+gap, arr[j+gap], arr[j]);
                arr[j + gap] = arr[j]; // j+gap 既是i，发现i前面每间隔gap有大于arr[i]的元素，就交换，将前面大元素挪到后面       
            }
            arr[j + gap] = temp; // 将arr[i]放入合适的位置
            printf("j+gap==%d \n \n",(j+gap));
        }
    }
}

int main() 
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int len = (int) sizeof(arr) / sizeof(*arr);
    shell_sort(arr, len);
    int i;
    for (i = 0; i < len; i++)
        printf("%d ", arr[i]);
    return 0;
}

