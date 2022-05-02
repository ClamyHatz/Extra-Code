/*
 * Lab 12
 * Description: uses try-catch statements to catch errors if they show up (they always do)
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
public class ExceptionsTest {
    public static void main(String[] args) {
        int[] array = {1, 2, 3}; // creates a new array
        int x = 0; // creates an int x
        try {
            array[4] = x; // makes array position 4 equal to x
        } catch (Exception e) { //if there is an error do this
            x = -1; // set x equal to -1
        } finally {
            System.out.println(x); // prints the value fo x
        }
        try{
            x = 5; // sets x equal to five
            methodWithException(array); // calls method
            x = 6; //sets x equal to 6
        } catch (Exception e){ // if there is an error do this
            System.out.println(x); // prints value of x
        }
    }
    static void methodWithException(int[] array) throws IndexOutOfBoundsException{ //creates a method with a throw statement to see if the index goes out of bounds
        int y = array[50]; // sets y to the position of 50 in array array
    }
}
