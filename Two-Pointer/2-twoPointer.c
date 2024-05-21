#include <stdio.h>
#include <stdlib.h>

/**
 * twoPointer - Solves the two-pointer algorithm problem
 * @lst: Sorted array of integers
 * @target: Target sum
 * @numSize: size of the array
 * @returnSize: size of the return array
 *
 * Return: The pair of numbers adding up to the target sum
 */

int *twoPointer(int lst[], int target, int numSize, int *returnSize)
{
	int start = 0;
	int end = numSize - 1;

	while (start < end)
	{
		int sum = lst[start] + lst[end];

		if (sum == target)
		{
			int *result = malloc(2 * sizeof(int));

			result[0] = start;
			result[1] = end;
			*returnSize = 2;

			return (result);
		} else if (sum < target)
		{
			start++;
		} else
		{
			end--;
		}
	}

	*returnSize = 0;
	return (NULL);
}


/**
 * main - Entry point of the program
 *
 * Return: 0 on success, -1 on failure
 */
int main(void)
{
	int nums[] = {1, 3, 4, 5, 6, 8, 9, 12};
	int numSize = sizeof(nums) / sizeof(nums[0]);
	int target = 11;

	int returnSize;
	int *result = twoPointer(nums, target, numSize, &returnSize);

	if (returnSize != 2)
		printf("No pair found\n");
	printf("Pair found: %d, %d\n", nums[result[0]], nums[result[1]]);

	free(result);
	return (0);
}
