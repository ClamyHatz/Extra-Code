/*
 * Assignment 4
 * Description: acts as a banking system for the user
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.util.Scanner; //imports scanner tool
public class BankAccount {
    public static void main(String[] args) { // main loop begins
        Scanner input = new Scanner(System.in); //sets up scanner tool
        double balance = 0;
        String answer = "SF";
        int accountNo = 1234567890;

        while (true) { //infinite while loop begins
            System.out.println("Operations");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Change Answer of Security Question");
            System.out.println("5. Exit");
            System.out.println();
            System.out.print("Enter your choice: ");
            int item = input.nextInt(); //takes user input
            switch (item){ //begins switch
                case 1:
                    checkBalance(balance, answer, accountNo);
                    break;
                case 2:
                    balance = depositMoney(balance); //changes balanced based on depositMoney's return
                    break;
                case 3:
                    balance = withdrawMoney(balance); //changes balanced based on withdrawMoney's return
                    break;
                case 4:
                    answer = changeAnsSecurityQuestion(); //changes answer based on changeAnsSecurityQuestion's return
                    break;
                case 5:
                    System.out.println("Thank you for visiting us!");
                    System.exit(0); //kills the program
                    break;
            }
        }
    }
    public static void checkBalance(double balance, String answer, int accountNo){
        Scanner input = new Scanner(System.in); //sets up scanner tool
        System.out.println("In which city was your first job? ");
        String city = input.nextLine(); //takes user input
        if (city.equals(answer)){ //checks if input and answer are the same
            System.out.println("Account Number: ");
            int response = input.nextInt(); //takes user input
            if (response == accountNo){ //checks if input and account Number are the same
                System.out.println("Balance: " + balance);
            }
            else{
                System.out.println("Incorrect Answer");
            }
        }
        else{
            System.out.println("Incorrect Answer");
            System.out.println();
        }
    }
    public static double depositMoney(double balance){
        Scanner input = new Scanner(System.in); //sets up scanner tool
        System.out.print("Enter the amount to deposit: ");
        double amount = input.nextDouble(); //takes user input
        return balance + amount;
    }
    public static double withdrawMoney(double balance){
        Scanner input = new Scanner(System.in); //sets up scanner tool
        System.out.print("Enter the amount to withdraw: ");
        double with = input.nextDouble();
        if (with <= balance){ //checks if user input is less than balance
            balance = balance - with; //takes user input out of balance
        }
        else {
            System.out.println("Transaction Failed. Not enough balance");
        }
        return balance;
    }
    public static String changeAnsSecurityQuestion(){
        Scanner input = new Scanner(System.in); //sets up scanner tool
        System.out.print("In which city was your first job? ");
        return input.nextLine();
    }
}
