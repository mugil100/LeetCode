class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        op_arr = []
        for i in range(n):
            if (i+1) %3 ==0 and (i+1) %5 ==0:
                op_arr.append("FizzBuzz")
            elif (i+1) %3 ==0:
                op_arr.append("Fizz") 
            elif (i+1) %5 ==0:
                op_arr.append("Buzz")
            else:
                op_arr.append(str(i+1))
        return op_arr

        