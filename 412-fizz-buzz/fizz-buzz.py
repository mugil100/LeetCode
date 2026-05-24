class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        op_arr = [0]*n
        for i in range(n):
            if (i+1) %3 ==0 and (i+1) %5 ==0:
                op_arr[i] = "FizzBuzz"
            elif (i+1) %3 ==0:
                op_arr[i] = "Fizz"
            elif (i+1) %5 ==0:
                op_arr[i] = "Buzz"
            else:
                op_arr[i]= str(i+1)
        return op_arr

        