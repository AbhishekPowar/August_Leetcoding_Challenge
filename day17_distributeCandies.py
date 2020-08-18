class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # renaming for easier access
        N = candies
        p = num_people

        # last number that is valid
        n = int(-0.5 + (0.25+(2*N))**0.5)
        # Number of valid rows
        rows = n//p

        # sum till valid row
        intersum = int(p*((rows*(rows-1))//2))
        # arr init
        arr = [(i*rows) + intersum for i in range(1, p+1)]

        # last valid number
        last = n - n % p

        # sum till last valid number
        cursum = ((last+1)*last)//2
        # calculating remaining
        rem = N-cursum

        # Normal logic
        for idx in range(0, p):
            last += 1
            if last <= rem:
                arr[idx] += last
                rem -= last
            else:
                arr[idx] += rem
                break
        return arr
