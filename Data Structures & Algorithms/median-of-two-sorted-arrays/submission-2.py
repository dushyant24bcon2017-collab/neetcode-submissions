class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #in this soln what we are doing is we are creating two portions 
        #a left one and a right one , with this we can find the middle elem
        #if the the toal of len is even then then the avg of the two middle 
        #eelms , and of odd then our middle eelm , 
        # how we are going to find out our left and right partition is by 
        #binary search cause that would be the best possible way we have already 
        #done it in the lenier time and for o(logn) we would run binary search 
        #on one array[small one ] after that we would have 4 values Aleft Aright 
        #Bleft Bright and what we need is that aleft<=bright and bleft <Aright
        #we are doing this cris cross because the elems in the same array would 
        #always be sorted and aleft < = aright and so and so  if these conds 
        #not satisfied we eithe do l=i+1 when aright <bleft  
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1