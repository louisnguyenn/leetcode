/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0, j = 1;
    int *arr = NULL;

    // declare return size (two sum always returns 2 integers)
    *returnSize = 2;

    // allocate memory of the array for two integers
    arr = malloc(sizeof(int)*2);

    // outer for loop iterates to next number if every number after that index does not add up to the target
    for (i = 0; i < numsSize; i++)
    {
        // inner for loop will add numbers to i that are i+1 indices away
        for (j = i+1; j < numsSize; j++)
        {
            // if statement checks if the two indices add up to target AND the indices are different
            if (nums[i] + nums[j] == target && i != j)
            {
                arr[0] = i;
                arr[1] = j;
            }
        }
    }

    return arr; // return array with indices
}
