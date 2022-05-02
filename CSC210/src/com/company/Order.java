/*
 * Assignment 4
 * Description: makes a menu and adds money from the user
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.util.Scanner; //imports scanner tool
public class Order {
    public static void main(String[] args) { //main loop begins
        System.out.println("Welcome to lily's restaurant");
        String[] menu = {"Bulgogi", "Kalbi", "Kimchi Fried Rice"};
        System.out.println();
        int totalComb = 0, total = 0;
        double totalTax = 0;
        while (true) { //starts an infinite while loop
            int item = menu_received(); //sets item equal to the return value of menu_received
            if (item == 0){ //checks if item is 0
                totalTax = (totalComb * 1.085); //takes total and adds tax
                System.out.println("Your total after tax is " + totalTax);
                break; //ends infinite while loop
            }
            if (item == 1) { //checks if item is one
                total = 15;
            } else if (item == 2) { //checks if item is two
                total = 18;
            } else if (item == 3) { //checks if item is three
                total = 16;
            }
            totalComb = totalComb + total; //adds total to total combo
            System.out.println("Your total is " + totalComb);
            System.out.println("Thank you for ordering " + menu[item - 1]);
        }
        double tip = tip_calculator(totalComb);
        System.out.println("Your total after tax and tip is "+ tip);
        System.out.println("Thank you and enjoy the food and come again!");
    }
    public static double tip_calculator(int total){
        Scanner input = new Scanner(System.in); //sets up scanner tool

        double ten = total * .10; //calculates tax
        double fifteen = total * .15; //calculates tax
        double twenty = total * .20; //calculates tax
        System.out.println("1. tip 10%: "+ten);
        System.out.println("2. tip 15%: "+fifteen);
        System.out.println("3. tip 20%: "+twenty);
        System.out.println("Please choose one option: (0 for no tip):");
        int item = input.nextInt(); //takes user input
        double totalTax = total * 1.085;
        double tip = totalTax;

        if (item == 1) {
            tip = totalTax + total * .10; //adds tax if item is one
        } else if (item == 2) {
            tip = totalTax + total * .15; //adds tax if item is two
        } else if (item == 3) {
            tip = totalTax + total * .20; //adds tax if item is three
        }

        return tip; //returns user input
    }
    public static int menu_received() {
        Scanner input = new Scanner(System.in); //sets up scanner tool


        System.out.println("Here is our menu!");
        System.out.println("1. Bulgogi -- $15.00");
        System.out.println("2. Kalbi -- $18.00");
        System.out.println("3. Kimchi Fried Rice -- $16.00");
        System.out.println("Please choose one option at one time using the number (0 for the end of order):");
        int item = input.nextInt(); //takes user input

        return item; //returns user input
    }
}
