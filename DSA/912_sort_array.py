def sortArray(nums:list[int])-> list[int]:
    
    # merge sort

    def merge(arr1,arr2):
        n = len(arr1)
        m = len(arr2)
        result = []

        l, r = 0,0

        while l<n and r<m:
            if arr1[l]<=arr2[r]:
                result.append(arr1[l])
                l+=1
            else:
                result.append(arr2[r])
                r+=1
        if l==n:
            result.extend(arr2[r:])
        if r==m:
            result.extend(arr1[l:])
        return result
    
    def mergesort(nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = mergesort(nums[:mid])
        right = mergesort(nums[mid:])

        return merge(left,right)
    
    return mergesort(nums)

def sortArray2(nums:list[int])-> list[int]:
    
    # quick sort
    
    def partition(nums, start=0, end = None):
        if end is None:
            end = len(nums)-1
        l, r = start, end-1     # end-1 because our pivot point is last element of the nums

        while l<=r:
            if nums[l]<= nums[end]:
                l+=1
            elif nums[r]>nums[end]:
                r -= 1
            if l<r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[l], nums[end] = nums[end], nums[l]

        return l
    
    def quicksort(nums, start=0, end=None):
        if end is None:
            nums = list(nums)
            end = len(nums)-1
        if start<end:
            pivot = partition(nums,start,end)
            quicksort(nums,start,pivot-1)
            quicksort(nums,pivot+1,end)
        return nums
    
    return quicksort(nums)




if __name__ == '__main__':
    nums = [2,3,42,1,435,23,452]
    print(sortArray(nums))
    print(sortArray2(nums))
