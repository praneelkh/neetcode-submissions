class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L_ptr = 0
        R_ptr = len(numbers) - 1

        while numbers[L_ptr] + numbers[R_ptr] != target:
            if (numbers[L_ptr] + numbers[R_ptr]) < target:
                L_ptr += 1
            elif (numbers[L_ptr] + numbers[R_ptr]) > target:
                R_ptr -= 1
        
        return [L_ptr + 1, R_ptr + 1]
        
        