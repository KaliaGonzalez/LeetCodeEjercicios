from typing import List

def sortColors(nums: List[int]) -> None: 
     n = len(nums) 
     for i in range(0,n-1): 
         #accedemos al elemento siguiente
         for j in range (0, n-1-i): 
             if(nums[j]> nums[j+1]): 
                 mayor = nums[j] 
                 nums[j] = nums[j+1] 
                 nums[j+1] = mayor  
     print(nums)   
     
               
if __name__ == "__main__":
    mi_lista = [2,0,1]
    print(sortColors(mi_lista))     