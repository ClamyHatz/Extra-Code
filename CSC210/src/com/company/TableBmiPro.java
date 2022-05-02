/*
 * Assignment 5
 * Description: creates a table showing multiple BMI's based on user input
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.util.Scanner; //imports scanner
public class TableBmiPro {
    public static void main(String[] args) { //main loop begins
        Scanner input = new Scanner(System.in); //starts scanner

        System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
        System.out.println("^ Welcome to:");
        System.out.println("^    BODY MASS INDEX (BMI) Computation PRO");
        System.out.println("^               by SFSU");
        System.out.println("^");
        System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
        System.out.print("Enter height in feet and inches: ");
        int heightFt = input.nextInt(); //next input takes height in feet
        int heightIn = input.nextInt(); //next input takes height in inches

        System.out.print("Enter the low weight in pounds: ");
        int weightLow = input.nextInt(); // next input takes lowest weight

        System.out.print("Enter the high weight in pounds: ");
        int weightHigh = input.nextInt(); // next input takes highest weight

        double height = (((heightFt * 12) + heightIn) * 0.0254); // converts height from feet to inches to meters

        String [] condition_array = {"not overweight", "overweight"}; //new array of strings

        System.out.println();
        System.out.println("WEIGHT      BMI          CONDITION");

        for(int i = weightLow; i <= weightHigh; i += 5){ //new for loop adds 5 to starting value until value is greater then weightHigh

            double weight = (i / 2.20462); //changes current weight into kilograms
            double BMI = weight / Math.pow(height, 2); // creates BMI with weight and height
            int choose = 0; //new variable
            if (BMI > 25){ //checks if BMI is less than 25 if so changes choose to 1
                choose = 1;
            }
            String cond = condition_array[choose]; //depenging on choose takes a string from condition array
            float bmiCast = (float)BMI; //casts BMI into float

            System.out.printf("%-11s %-12.4f %-23s %n",i, bmiCast, cond); //using format prints out current weight BMI and if teh weight is over wheight or not
        }
        System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
        System.out.println("^      Thank you for using my program.");
        System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
    }
}
