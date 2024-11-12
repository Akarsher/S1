#include <stdio.h>

void insertSpecific(int a[], int *n, int pos, int value);
void deleteSpecific(int a[], int *n, int pos);
void traverse(int a[], int n);

void main() {
    int a[20];
    int i, n, ch;

    printf("Enter the size of the array (max 20): ");
    scanf("%d", &n);

    if (n > 20) {
        printf("Array size can't exceed 20!\n");
        return;
    }

    printf("Enter the array elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // Continuous while loop
    while (1) {
        printf("\nSelect an option:\n");
        printf("1. Insert an element at a particular position\n");
        printf("2. Delete an element at a particular position\n");
        printf("3. Traverse the array\n");
        printf("4. Exit\n");
        printf("Enter the action to perform: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1: {
                int pos, value;
                printf("Enter the position (0 to %d): ", n);
                scanf("%d", &pos);
                if (pos < 0 || pos > n) {
                    printf("Invalid position!\n");
                } else {
                    printf("Enter the value to insert: ");
                    scanf("%d", &value);
                    insertSpecific(a, &n, pos, value);
                }
                break;
            }
            case 2: {
                int pos;
                printf("Enter the position to delete (0 to %d): ", n - 1);
                scanf("%d", &pos);
                if (pos < 0 || pos >= n) {
                    printf("Invalid position!\n");
                } else {
                    deleteSpecific(a, &n, pos);
                }
                break;
            }
            case 3:
                traverse(a, n);
                break;
            case 4:
                printf("Exiting the program.\n");
                return;  // Exit the program
            default:
                printf("Invalid option! Please try again.\n");
        }
    }
}

void traverse(int a[], int n) {
    printf("Array elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void insertSpecific(int a[], int *n, int pos, int value) {
    if (*n >= 20) {
        printf("Array overflow! Cannot insert more elements.\n");
        return;
    }

    for (int i = *n; i > pos; i--) {
        a[i] = a[i - 1];
    }

    a[pos] = value;
    (*n)++;
    printf("\nArray after insertion:\n");
    traverse(a, *n);
}

void deleteSpecific(int a[], int *n, int pos) {
    for (int i = pos; i < *n - 1; i++) {
        a[i] = a[i + 1];
    }
    (*n)--;

    printf("\nArray after deletion:\n");
    traverse(a, *n);
}
