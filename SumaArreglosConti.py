from typing import List
 
def checkSubarraySum( nums: List[int], k: int) -> bool: 
    resultado =[] 
    mensaje = False 
    for j in range(1,100): 
        for i in range (0,len(nums)-1): 
            if(sum(nums) == j*k): 
                mensaje = True
            if(nums[i] + nums[i+1] == j*k ): 
                resultado.append(nums[i])
                resultado.append(nums[i+1])  
                mensaje= True     
    return mensaje 
if __name__ == "__main__":
    mi_lista = [23,50,50]
    print(checkSubarraySum(mi_lista,100))     