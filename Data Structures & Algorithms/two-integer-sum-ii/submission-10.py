class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        size = len(numbers) - 1
        last_i = len(numbers) - 2
        stride = (len(numbers) - 1) // 2
        while(i <= last_i):
            # print(i, j, stride)
            # print(j)
            numi = numbers[i]
            numj = numbers[j]
            sums = numi + numj
            # print(sums, "=", numi, "+", numj)
            if (sums == target):
                return [i + 1, j + 1]
            elif(sums <= target):
                if stride == 0:
                    i, j = (i + 1), (i + 2)
                    stride = (size - j) // 2
                else:
                    j = j + stride
            elif(sums >= target):
                if stride == 0:
                    i, j = (i + 1), (i + 2)
                    stride = (size - j) // 2
                else:
                    size = j 
                    j = j - stride
            stride = (size - (j - 1)) // 2
            # print(numbers[j])
        return []
            
            
            

                

        