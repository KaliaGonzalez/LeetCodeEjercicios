from typing import List
def countSmaller( nums: List[int]) -> List[int]: 
    if(len(nums) == 1): 
        return [0]
    rep = [] 
    for i in range(0,len(nums)):  
        contador = 0 
        elemtoComparar = nums[i] 
        print(elemtoComparar)
        sublista = nums[i+1: len(nums)]  
        print(sublista)
        for j in  range(0,len(sublista)): 
            if(sublista[j]< elemtoComparar): 
                contador+=1 
        rep.append(contador) 
    return rep 


if __name__ == "__main__":
    mi_lista = [-1]
    print(countSmaller(mi_lista))            