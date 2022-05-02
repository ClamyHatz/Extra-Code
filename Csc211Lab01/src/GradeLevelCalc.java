/*
 * Lab 2
 * Description: Calculates users graded based on their inputed age
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */

import java.util.Scanner; //Imports the scanner utility

public class GradeLevelCalc {

    public static void main(String[] args) { // Main loop begins
        Scanner input = new Scanner(System.in); // Creates scanner input capabilities
        System.out.println("I will guess your grade based on your age");
        System.out.println("Please enter name: ");
        String name = input.nextLine(); // Next line will read and save users name as a string
        System.out.println("Thanks " + name + "! Now enter you age: ");
        int age = input.nextInt(); // Next line will save users age as an integer

        switch(age) { // Starts switch based on users age
            case 3:
                System.out.println(name + ", you are in Preschool");
                break;
            case 4:
                System.out.println(name + ", you are in Junior Kindergarten");
                break;
            case 5:
                System.out.println(name + ", you are in Kindergarten");
                break;
            case 6:
                System.out.println(name + ", you are in Grade 1");
                break;
            case 7:
                System.out.println(name + ", you are in Grade 2");
                break;
            case 8:
                System.out.println(name + ", you are in Grade 3");
                break;
            case 9:
                System.out.println(name + ", you are in Grade 4");
                break;
            case 10:
                System.out.println(name + ", you are in Grade 5");
                break;
            case 11:
                System.out.println(name + ", you are in Grade 6");
                break;
            case 12:
                System.out.println(name + ", you are in Grade 7");
                break;
            case 13:
                System.out.println(name + ", you are in Grade 8");
                break;
            case 14:
                System.out.println(name + ", you are in Grade 9");
                break;
            case 15:
                System.out.println(name + ", you are in Grade 10");
                break;
            case 16:
                System.out.println(name + ", you are in Grade 11");
                break;
            case 17:
                System.out.println(name + ", you are in Grade 12");
                break;
            default:
                System.out.println("you have entered an unacceptable age");
        }
    }
}
