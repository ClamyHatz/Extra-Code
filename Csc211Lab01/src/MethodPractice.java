/*
 * Lab 6
 * Description: Uses multiple methods to get a variety of results
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
public class MethodPractice {
    public static void main(String[] args) {
        System.out.println("Part 1: Bart Simpson Chalk");
        System.out.println();
        //creates a for loop that runs 23 times
        for (int i = 0; i < 23; i++){
            //calls the method bartSimpsonChalk
            bartSimpsonChalk();
        }
        System.out.println();
        System.out.println("Part 2: Multiply Doubles");
        System.out.println();
        //multiplies the two numbers within the parentheses by calling multiplyDoubles
        double a = multiplyDoubles(10.4, 20.0);
        //multiplies the two numbers within the parentheses by calling multiplyDoubles
        double b = multiplyDoubles(12.3, 5.34);
        //multiplies the two numbers within the parentheses by calling multiplyDoubles
        double c = multiplyDoubles(a, b);
        System.out.println("the value of c is: " + c);
        System.out.println();
        System.out.println("Part 2: Print Operations");
        System.out.println();
        //shows addition, subtraction, multiplication, and division from the two numbers in the parentheses
        printOperations(10, 20);
        System.out.println();
        //shows addition, subtraction, multiplication, and division from the two numbers in the parentheses
        printOperations(25, 4);
    }
    public static void bartSimpsonChalk(){
        System.out.println("I will not bury the new kid");
    }
    static double multiplyDoubles(double x, double y){
        //returns x times y
        return x * y;
    }
    static void printOperations(int x, int y){
        //new variable adds x and y
        int add = x+y;
        //new variable subtracts x and y
        int minus = x-y;
        //new variable multiplies x and y
        int multi = x*y;
        //new variable divides x and y
        int divide = x/y;
        System.out.println("For the numbers "+x+" and "+y+":");
        System.out.println("Addition is: " + add);
        System.out.println("Subtraction is: " + minus);
        System.out.println("Multiplication is: " + multi);
        System.out.println("Quotient is: " + divide);
    }
}
