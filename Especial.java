public class Especial {
    public static void main(String[] args) {
        int [] nums = {2,7,1,19,18,3}; 
        int suma = sumOfSquares(nums); 
        System.out.println(suma);

    } 
    public static int sumOfSquares(int[] nums){  
        int contador = 0; 
        int longitud = nums.length; 
        for (int i = 1; i<=nums.length-1;i++){ 
            if(longitud % i == 0){ 
                int nuevoNum = 0;
                nuevoNum = nums[i]*nums[i]; 
                contador += nuevoNum; 
            } 
        }
        return contador; 
    }
}//PREGUNTAR MAS ADELANTE
