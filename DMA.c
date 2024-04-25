#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr1, *arr2, *arr3;
    int n;

    // Allocate memory for arr1 using malloc
    printf("Enter the number of elements for arr1: ");
    scanf("%d", &n);
    arr1 = (int *)malloc(n * sizeof(int));

    if (arr1 == NULL) {
        printf("Memory allocation for arr1 failed.\n");
        return 1;
    }

    // Initialize arr1 elements
    for (int i = 0; i < n; i++) {
        arr1[i] = i + 1;
    }

    // Allocate memory for arr2 using calloc
    printf("Enter the number of elements for arr2: ");
    scanf("%d", &n);
    arr2 = (int *)calloc(n, sizeof(int));

    if (arr2 == NULL) {
        printf("Memory allocation for arr2 failed.\n");
        return 1;
    }

    // Allocate memory for arr3 using realloc
    printf("Enter the new size for arr3: ");
    scanf("%d", &n);
    arr3 = (int *)realloc(arr2, n * sizeof(int));

    if (arr3 == NULL) {
        printf("Memory reallocation for arr3 failed.\n");
        free(arr2); // Free the memory allocated for arr2
        return 1;
    }

    // Display arr1
    printf("arr1 elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    // Display arr3
    printf("arr3 elements (after reallocation): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr3[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(arr1);
    free(arr3);

    return 0;
}
