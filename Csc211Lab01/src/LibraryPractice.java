/*
 * Lab 4
 * Description: Print out things using char and String methods
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
public class LibraryPractice {
    public static void main(String[] args) {

        String first = "\"Boba Guys is pretty good!\" - William Lew"; //new string named first
        System.out.println(first);
        System.out.println(first.length()); //tells us how long string first is

        String second = "\"Quickly is garbage!\" - Everyone with Taste Buds"; //new string named second
        System.out.println(first + second);
        System.out.println(first.compareTo(second)); //compares string first and second

        second = "\"Boba Guys is pretty good!\" - William Lew"; //changes what string second equals
        System.out.println(first.compareTo(second)); //compares string first and second

        first = "Hello World!"; //changes what string first equals
        System.out.println(first.compareTo(second)); //compares string first and second

        String third = "A1B2C3D4"; //new string named third
        char[] thirdArray = third.toCharArray(); //turns string third into an array of char type
        for(int i = 0; i < third.length(); i++){ //for loop runs for the length of string third
            if(Character.isDigit(thirdArray[i])){ //checks if the char type is a digit
                System.out.println(thirdArray[i]); //if it is print it
            }
        }
        int fourth = Character.getNumericValue(thirdArray[3]); //new int fourth sets it equal to the numeric value of the fourth char type in String third
        System.out.println(fourth);
    }
}
