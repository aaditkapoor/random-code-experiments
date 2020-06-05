from typing import List

def selfDividingNumbers(left: int, right: int) -> List[int]:
        numbers = []


        def isSelf(n):
            for i in str(n):
                if i == "0" or n % int(i) > 0:
                    return False
            return True

        for i in range(left, right+1):
            if isSelf(i):
                numbers.append(i)
        return numbers
