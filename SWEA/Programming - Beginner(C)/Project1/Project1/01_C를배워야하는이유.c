#include <stdio.h>

int main(void) {
	int number;
	char letter;
	float realnumber;

	print("number? ");
	scanf("%d", &number);
	print("Realnumber? ");
	scanf("%f", &realnumber);
	print("%d, %f", number, realnumber);

	return 0;

}