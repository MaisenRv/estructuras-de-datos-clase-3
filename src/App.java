import java.util.Scanner;

public class App {
    
    
    
    public static void main(String[] args) throws Exception {
        String[][]  tabla1 = {
            {"urbano","Latitud","4.23","longitud","-71","10","20"},
            {"calles","Latitud","2.33","longitud","-74.5","1000"},
            {"lagos","Latitud","3.33","longitud","-72.3","200","400"},
            {"rios","Latitud","4.44","longitud","-71.5","200"},
        };

        String[] cabezeras = {"lugar","coordenadas","perimetro/area"};
    

        Scanner cs = new Scanner(System.in);
        try {
            System.out.println("Escriba la longitud: ");
            Float longitud = cs.nextFloat();    
            System.out.println("Escriba la latitud: ");
            Float latitud = cs.nextFloat();
            
            int i=0;
            do{
                
                if(Float.parseFloat(tabla1[i][2])  == longitud && Float.parseFloat(tabla1[i][4]) == latitud ){
                    System.out.println(cabezeras[0] + " : " + tabla1[i][0]);
                    System.out.println(cabezeras[1] + " : " + tabla1[i][1] + ": " +  tabla1[i][2] + ": " + tabla1[i][3] + ": " + tabla1[i][4]);
                    try {
                        
                        System.out.println(cabezeras[2] + " : " + tabla1[i][5] + " " + tabla1[i][6]);
                    } catch (Exception e) {
                        System.out.println(cabezeras[2] + " : " + tabla1[i][5]);
                    }
                    
                }
                i++;
            }while (i < tabla1.length);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        

    }
}
