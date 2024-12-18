public class Main {
     public static void main(String[] args) {
        int [][] tablero = { 
            {5,4,5,7,6} , 
            {6,8,6,7,6}, 
            {7,9,8,6,5}, 
            {4,7,8,6,7},
            {6,5,6,7,8} 
        } ; 
        boolean respuesta = solucion(tablero);  
        if(respuesta == true){ 
            System.out.println("Existe un camino");
        } 
        else { 
            System.out.println("No existe camino ");
        }

    } 
    public static boolean solucion(int[][] tablero) {  
        boolean [][] m = new boolean[5][5]; 
        for(int i = 0 ; i< 5; i++){ 
            for(int j = 0 ; j< 5; j++){ 
                if(i == 0 && j == 0){ 
                    m[i][j] = true; 
                } 
                else if (i> 0 && j==0) { 
                    m[i][j] = m[i-1][j]&& (Math.abs(tablero[i][j] - tablero[i-1][j])<=1);   
                } 
                else if (i== 0 && j>0){ 
                    m[i][j] = m[i][j-1]&& (Math.abs(tablero[i][j] - tablero[i][j-1] )<= 1);
                }  
                else if ( i>0 && j>0){ 
                    m[i][j] = (m[i][j-1]&& (Math.abs(tablero[i][j] - tablero[i][j-1] )<= 1)) || (m[i-1][j]&& (Math.abs(tablero[i][j] - tablero[i-1][j] )<= 1));

                }

            }
        } 
        return m[5-1][5-1]; 

    }
}
