int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    if (numsSize <= 0) return 0;
    for (int j = 0; j < numsSize; j++){
        if (nums[j] != nums[i]){
            i++;
            nums[i] = nums[j];
            }
        }   
return (i+1);
}
