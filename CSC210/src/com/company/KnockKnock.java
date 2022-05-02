/*
 * Assignment 2
 * Description: Calculates user BMI based on user input.
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
//Imports the scanner utility
import java.util.Scanner;

public class KnockKnock {
    public static void main(String[] args) {
        // Creates scanner object
        Scanner input = new Scanner(System.in);
        System.out.println("Knock, knock");
        //saves user response as a string
        String Response1 = input.nextLine();
        //checks if user answered properly
        if (Response1.equals("Who's there?")) {
            System.out.println("Annie");
            //saves user response as a string
            String Response2 = input.nextLine();
            //checks if user answered properly
            if (Response2.equals("Annie who?")) {
                System.out.println("Annie thing you can do I can do better");
            }
        }
    }
}
