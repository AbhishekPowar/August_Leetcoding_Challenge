# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         return ['FizzBuzz' if i%3==0 and i%5==0 else 'Buzz' if i%5 ==0 else 'Fizz' if i%3==0 else str(i) for i in range(1,n+1)]

# Explanation:
# Shorthand not readable but possible

if __name__ == "__main__":
    n = 15
    # arr = [str(i) for i in range(1, n+1)]
    # for idx in range(n):
    #     val = idx+1
    #     if val % 3 == 0 and val % 5 == 0:
    #         arr[idx] = 'FizzBuzz'
    #     elif val % 3 == 0:
    #         arr[idx] = 'Fizz'
    #     elif val % 5 == 0:
    #         arr[idx] = 'Buzz'

    arr = [(i % 3 == 0)*'Fizz' + (i % 5 == 0)*'Buzz' or str(i)
           for i in range(1, n+1)]
