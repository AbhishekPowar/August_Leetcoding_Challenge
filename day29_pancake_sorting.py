class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def reverse(A,n):
            A[:n+1] = A[:n+1][::-1]


        def findMax(A,n):
            maxx = 0
            issorted=True
            for i in range(n+1):
                if A[i]>A[maxx]:
                    maxx=i
                #Check if already sorted
                if i!=0 and issorted:
                    issorted = A[i]>=A[i-1]
            return maxx if issorted==False else -1


        N= len(A)
        steps = []
        for n in range(N-1,-1,-1):
            idx= findMax(A,n)
            # Break if sorted
            if idx==-1: 
                break
            #Dont flip if in right place
            if idx != n:
                # No need to bring to idx 0
                if idx !=0:
                    reverse(A,idx)
                    steps.append(idx)
                reverse(A,n)
                steps.append(n)
        
        # Convesting into 1 based indexing
        return [i+1 for i in steps]

# Logic

# Find maximum numbers index 
# Move it to idx 0
# Move it to Nth position
# arr = [3, 2, 4, 1]

# Max at idx 2
# Flip from idx 2             
# [4, 2, 3, 1]
# Flip from idx 3
# [1, 3, 2, 4]

# Max at idx 1
# Flip at idx 1
# [3, 1, 2, 4]
# flip at idx 2
# [2, 1, 3, 4]

# Max at idx 0
# Flip at idx 0
# [1, 2, 3, 4]