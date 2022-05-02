/*
 * Assignment 3
 * Description: picks a random number between 1 - 6 then says what it is plus is it is even or odd and if it's divisible by three
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.lang.Math;
public class DiceRolling {
    public static void main(String[] args) {
        // define the range
        int max = 6;
        int min = 1;
        int range = max - min + 1;

        // generate random numbers within 1 to 10
        int rand = (int)(Math.random() * range) + min;

        System.out.println("I got " + rand);

        // starts switch from random number
        switch(rand){
            case 6:
                System.out.println("This is an even number");
                break;
            case 5:
                System.out.println("This is an odd number");
                break;
            case 4:
                System.out.println("This is an even number");
                break;
            case 3:
                System.out.println("This is an odd number");
                break;
            case 2:
                System.out.println("This is an even number");
                break;
            case 1:
                System.out.println("This is an odd number");
                break;
        }
        // starts switch from random number
        switch(rand) {
            case 6:
                System.out.println("This number is divisible by 3");
                break;
            case 5:
                System.out.println("This number is not divisible by 3");
                break;
            case 4:
                System.out.println("This number is not divisible by 3");
                break;
            case 3:
                System.out.println("This number is divisible by 3");
                break;
            case 2:
                System.out.println("This number is not divisible by 3");
                break;
            case 1:
                System.out.println("This number is not divisible by 3");
                break;
        }
    }
}
