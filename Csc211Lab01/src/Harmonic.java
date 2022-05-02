/*
 * Lab 5
 * Description: Create a harmonic series based on n
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
public class Harmonic {
    public static void main(String[] args) {
        //creates float variable for sum
        double sum = 1;
        //creates and stores the sum for the for loop
        double forSum = 0;
        //creates and stores the sum for the while loop
        double whileSum = 0;
        //creates and stores the value of w
        int w = 1;
        //creates and stores teh value of n
        int n = 50;

        //for loop starts with i being 1 then repeats until it is equal or less than n
        for ( int i = 1; n >= i; i++ ){
            //adds 1 over the value of i to the total sum
            forSum = forSum + (sum/i);
        }
        //for loop starts with w being 1 then repeats until it is equal or less than n
        while (w <= n){
            //adds 1 over the value of w to the total sum
            whileSum = whileSum + (sum/w);
            //adds 1 to the value of w
            w++;
        }

        System.out.println("For loop harmonic series to "+ n + ": " + forSum);
        System.out.println("While loop harmonic series to "+ n + ": " + whileSum);
    }
}
