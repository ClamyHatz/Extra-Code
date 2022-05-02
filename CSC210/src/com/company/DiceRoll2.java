/*
 * Assignment 6
 * Description: Rolls a die then tells the user the probabily of each face *
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.util.Scanner; //imports scanner
public class DiceRoll2 {
    public static void main(String[] args) { //main loop begins
        Scanner input = new Scanner(System.in); //starts scanner
        System.out.print("How many times should the dice roll?: ");
        float diceRoll = input.nextInt(); //takes user input on how many times the dice should roll
        float face1 = 0;
        float face2 = 0;
        float face3 = 0;
        float face4 = 0;
        float face5 = 0;
        float face6 = 0;
        for (int i = 0; i <=diceRoll; i++){ //starts a for loop that runs as many times as the user has chosen
            int rand = (int)(Math.random() * 6) + 1; // gets a random number between 1 and 6
            switch (rand){ // switch begins
                case 1:
                    face1++;
                    break;
                case 2:
                    face2++;
                    break;
                case 3:
                    face3++;
                    break;
                case 4:
                    face4++;
                    break;
                case 5:
                    face5++;
                    break;
                case 6:
                    face6++;
                    break;
            }
        }
        float prob1 = (face1 / diceRoll);//calculates probability for face
        float prob2 = (face2 / diceRoll);//calculates probability for face
        float prob3 = (face3 / diceRoll);//calculates probability for face
        float prob4 = (face4 / diceRoll);//calculates probability for face
        float prob5 = (face5 / diceRoll);//calculates probability for face
        float prob6 = (face6 / diceRoll);//calculates probability for face
        int cast1 = (int)face1;//casts face
        int cast2 = (int)face2;//casts face
        int cast3 = (int)face3;//casts face
        int cast4 = (int)face4;//casts face
        int cast5 = (int)face5;//casts face
        int cast6 = (int)face6;//casts face
        System.out.println("[When the dice rolls " + diceRoll +" times]");
        System.out.println("Occurrence of each face is");
        System.out.println(cast1+ ", "+cast2+ ", "+cast3+ ", "+cast4+ ", "+cast5+ ", "+cast6+ ": "+ diceRoll);
        System.out.println("Therefore the probability of each face is ");
        System.out.println(prob1+ ", "+prob2+ ", "+prob3+ ", "+prob4+ ", "+prob5+ ", "+prob6);
    }
}
