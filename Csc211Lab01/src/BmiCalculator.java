/*
 * Lab 1
 * Description: Calculates user BMI based on user input.
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */

import java.util.Scanner; //Imports the scanner utility

public class BmiCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Creates scanner input capabilities

        System.out.println("Input weight and height");
        int weight = input.nextInt(); // Takes user input weight as an integer
        double height = input.nextDouble(); // Takes user input height as a double

        double BMI = weight / (height * height); //Calculates BMI using previous variables

        int bmiCast = (int)BMI; //casts BMI into an integer

        System.out.println("Weight: " + weight);
        System.out.println("Height: " + height);
        System.out.println("Your BMI is: " + BMI);
        System.out.println("Your casted BMI is: " + bmiCast);
    }
}
