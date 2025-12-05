int searchInsert(int* nums, int numsSize, int target) {
    int i = 0;

    for (i = 0; i < numsSize; i++)
    {
        // check if any numbers are equal to the target
        if (nums[i] == target)
        {
            return i;
        }

        // if not, check where the target would be inserted by checking i and i+1
        if (i + 1 < numsSize && target > nums[i] && target < nums[i+1])
        {
            return i+1;
        }

        // special case: if the target should be inserted at the end of the array, i.e., it is the largest number
        if (i == numsSize - 1 && target > nums[i])
        {
            return i+1;
        }
    }

    return 0;
}
