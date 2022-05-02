package edu.sfsu;
/*
    Assignment #6
    921804582@_HW06
    Lily Keus
 */
import java.util.Scanner;

public class Main {
    static void printStack1(ArrayStack s) {
        ArrayStack<Integer> backup = new ArrayStack<>();
        System.out.println("Stack contents:");
        while (!s.isEmpty1()) {
            int t = (Integer)s.pop1();
            backup.push1(t);
            System.out.print(t + " ");
        }
        System.out.println();

        while(!backup.isEmpty1())
            s.push1(backup.pop1());
    }
    static void printStack2(ArrayStack s) {
        ArrayStack<Integer> backup = new ArrayStack<>();
        System.out.println("Stack contents:");
        while (!s.isEmpty2()) {
            int t = (Integer)s.pop2();
            backup.push2(t);
            System.out.print(t + " ");
        }
        System.out.println();

        while(!backup.isEmpty2())
            s.push2(backup.pop2());
    }
    public static void main(String[] args) {
        ArrayStack<Integer> stk = new ArrayStack<>();

        int choice = -1;

        do {
            System.out.println("[1] Push into first stack");
            System.out.println("[2] Push into second stack");
            System.out.println("[3] Pop from first stack");
            System.out.println("[4] Pop from second stack");
            System.out.println("[5] Print top of first stack");
            System.out.println("[6] Print top of second stack");
            System.out.println("[7] Print contents of first stack");
            System.out.println("[8] Print contents of second stack");
            System.out.println("[9] Exit");
            System.out.println("Enter your choice:");
            Scanner in = new Scanner(System.in);
            choice = in.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter an item");
                    int num = in.nextInt();
                    stk.push1(num);
                    break;
                case 2:
                    System.out.println("Enter an item");
                    num = in.nextInt();
                    stk.push2(num);
                    break;
                case 3:
                    if (!stk.isEmpty1()) {
                        stk.pop1();
                    }
                    break;
                case 4:
                    if (!stk.isEmpty2()) {
                        stk.pop2();
                    }
                    break;
                case 5:
                    if (!stk.isEmpty1())
                        System.out.println("Top of the stack is " + stk.peek1());
                    else
                        System.out.println("Stack is empty");
                    break;
                case 6:
                    if (!stk.isEmpty2())
                        System.out.println("Top of the stack is " + stk.peek2());
                    else
                        System.out.println("Stack is empty");
                    break;
                case 7:
                    printStack1(stk);
                    break;
                case 8:
                    printStack2(stk);
                    break;
                case 9:
                    System.out.println("GoodBye!");
                    break;
                default:
                    System.out.println("Invalid choice! Enter a number in the range [1-9]");
                    break;
            }
        } while (choice != 9);
    }
}
