from typing import List 
def twoSum( nums: List[int],target:int) -> List[int]: 
    lista_nueva = [] 
    for i in range(1,len(nums)): 
        if(nums[i]+ nums[i-1] == target): 
            lista_nueva.append(i-1)
            lista_nueva.append(i)  
    return lista_nueva
         
if __name__ == "__main__":
    mi_lista = [3,3] 
    target = 6
    print("Lista con indices:", twoSum(mi_lista,target))             
             