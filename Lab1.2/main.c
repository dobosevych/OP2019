#include <stdio.h>
#include <string.h>

int main() {
    char digits[100];
    int m, n;
    int counter = 0;
    scanf("%d", &m);
    scanf("%d", &n);
    int num = 1;
    while (counter < m * n) {
        char str[20];
        sprintf(str, "%d", num);
        for (int i = 0; i < strlen(str); i++) {
            digits[counter] = str[i];
            counter++;
        }
        num += 1;
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%c", digits[n * i + j]);
        }
        printf("\n");
    }
    return 0;
}