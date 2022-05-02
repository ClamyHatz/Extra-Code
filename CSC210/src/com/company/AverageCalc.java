/*
 * Assignment 1
 * Description: Calculates user BMI based on user input.
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
//Imports the scanner utility
import java.util.Scanner;

public class AverageCalc {
    public static void main(String[] args) {
        // Creates scanner input capabilities
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter 3 whole numbers: ");
        //Takes first integer from user
        int theNumberF = input.nextInt();
        //Takes second integer from user
        int theNumberS = input.nextInt();
        //Takes third integer from user
        int theNumberT = input.nextInt();
        //gets the average of the three variables saves it as a float
        float sol = (((float)theNumberF + (float)theNumberS + (float)theNumberT) / 3);
        System.out.print("You entered " + theNumberF +" "+ theNumberS +" "+ theNumberT +" "+ "and the average of them is " + sol);
    }
}