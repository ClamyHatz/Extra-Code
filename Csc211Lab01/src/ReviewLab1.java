/*
 * Lab Review 1
 * Description: calls a method and prints a pyramid to size a user chooses
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
import java.util.Scanner; //Imports the scanner utility
public class ReviewLab1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Creates scanner input capabilities
        System.out.print("Enter desired height of pyramid: ");
        int size = input.nextInt(); //takes next input to be the size / height of the pyramid
        printPyramid(size); //calls methode printPyramid with size equaling x
    }
    public static void printPyramid(int x){
        for (int i = x; i >=0; i--){ //repeats x number of times
            for(int o = i - 1; o >= 0; o--){ //repeats i - 1 times
                System.out.print(" ");
            }
            for(int u = x; u >= i; u--){ //repeats the difference of x to i number of times
                System.out.print("* ");
                if(u == i){ // once u = i start a new line
                    System.out.println();
                    break;
                }
            }
        }
    }
}
