from typing import List
def removeDuplicates( nums: List[int]) -> int: 
        lista_nueva = [] 
        lista_nueva.append(nums[0])
        for i in range(1,len(nums)): 
            if(nums[i]!= nums[i-1]):
                lista_nueva.append(nums[i])  
                print(lista_nueva)
        k = len(lista_nueva) 
        return k

if __name__ == "__main__":
    mi_lista = [1,1,2]
    print("Lista original:", mi_lista)
    print("Lista sin duplicados:", removeDuplicates(mi_lista))