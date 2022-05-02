/*
 * Assignment 4
 * Description: picks a random number between 0 and 51 then says what it is plus which card it would be in an unopened deck
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 210-04
 * Semester: 2021 - 2
 */
package com.company;
import java.lang.Math;
public class CardPick {
    public static void main(String[] args) {
        // define the range
        int max = 0;
        int min = 51;
        int range = max - min + 1;

        // generate random numbers within 1 to 10
        int rand = (int)(Math.random() * range) + min;

        // for clover cards adds 1 to the random number so counting up starts at 2
        int clo = rand+1;
        // for spades cards subtracts 12 to the random number so counting up starts at 2
        int spa = rand-12;
        // for diamond cards subtracts 25 to the random number so counting up starts at 2
        int dia = rand-25;
        // for heart cards subtracts 38 to the random number so counting up starts at 2
        int hea = rand-38;

        // strats a switch based on the random number
        switch (rand){
            case 0:
                System.out.println("I got " + rand + ", which is Clover Ace");
                break;
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
                System.out.println("I got " + rand + ", which is Clover " + clo);
                break;
            case 10:
                System.out.println("I got " + rand + ", which is Clover Jack");
                break;
            case 11:
                System.out.println("I got " + rand + ", which is Clover Queen");
                break;
            case 12:
                System.out.println("I got " + rand + ", which is Clover King");
                break;
            case 13:
                System.out.println("I got " + rand + ", which is Spades Ace");
                break;
            case 14:
            case 15:
            case 16:
            case 17:
            case 18:
            case 19:
            case 20:
            case 21:
            case 22:
                System.out.println("I got " + rand + ", which is Spades " + spa);
                break;
            case 23:
                System.out.println("I got " + rand + ", which is Spades Jack");
                break;
            case 24:
                System.out.println("I got " + rand + ", which is Spades Queen");
                break;
            case 25:
                System.out.println("I got " + rand + ", which is Spades King");
                break;
            case 26:
                System.out.println("I got " + rand + ", which is Diamond Ace");
                break;
            case 27:
            case 28:
            case 29:
            case 30:
            case 31:
            case 32:
            case 33:
            case 34:
            case 35:
                System.out.println("I got " + rand + ", which is Diamond " + dia);
                break;
            case 36:
                System.out.println("I got " + rand + ", which is Diamond Jack");
                break;
            case 37:
                System.out.println("I got " + rand + ", which is Diamond Queen");
                break;
            case 38:
                System.out.println("I got " + rand + ", which is Diamond King");
                break;
            case 39:
                System.out.println("I got " + rand + ", which is Heart Ace");
                break;
            case 40:
            case 41:
            case 42:
            case 43:
            case 44:
            case 45:
            case 46:
            case 47:
            case 48:
                System.out.println("I got " + rand + ", which is Heart " + hea);
                break;
            case 49:
                System.out.println("I got " + rand + ", which is Heart Jack");
                break;
            case 50:
                System.out.println("I got " + rand + ", which is Heart Queen");
                break;
            case 51:
                System.out.println("I got " + rand + ", which is Heart King");
        }
    }
}
