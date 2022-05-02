package edu.sfsu;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static void printStack(ArrayStack s) {
        ArrayStack<Integer> backup = new ArrayStack<>();
        System.out.println("Stack contents:");
        while (!s.isEmpty()) {
            int t = (Integer)s.pop();
            backup.push(t);
            System.out.print(t + " ");
        }
        System.out.println();

        while(!backup.isEmpty())
            s.push(backup.pop());
    }
    public static void main(String[] args) {
        ArrayStack<Integer> stk = new ArrayStack<>();

        int choice = -1;

        do {
            System.out.println("[1] To push an item into the stack");
            System.out.println("[2] To pop an item from the stack");
            System.out.println("[3] To print the top of stack");
            System.out.println("[4] To check of stack is empty");
            System.out.println("[5] To print stack contents");
            System.out.println("[6] To sort stack");
            System.out.println("[7] To Exit");
            System.out.println("Enter your choice:");
            Scanner in = new Scanner(System.in);
            choice = in.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter an item");
                    int num = in.nextInt();
                    stk.push(num);
                    break;
                case 2:
                    if (!stk.isEmpty()) {
                        stk.pop();
                    }
                    break;
                case 3:
                    if (!stk.isEmpty())
                        System.out.println("Top of the stack is " + stk.peek());
                    else
                        System.out.println("Stack is empy ");
                    break;
                case 4:
                    if (stk.isEmpty()) {
                        System.out.println("Stack is empty");
                    } else {
                        System.out.println("Stack is not empty");
                    }
                    break;
                case 5:
                    printStack(stk);
                    break;
                case 6:
                    int counter =0;
                    ArrayStack<Integer> temp = new ArrayStack<>();
                    while(!stk.isEmpty()){
                        temp.push(stk.pop());
                        counter++;
                    }
                    int[] arr = new int[counter];
                    for(int i = 0; i < counter; i++){
                        stk.push(temp.peek());
                        arr[0] = temp.pop();
                    }
                    Arrays.sort(arr);
                    System.out.println(Arrays.toString(arr));
                case 7:
                    System.out.println("GoodBye!");
                    break;
                default:
                    System.out.println("Invalid choice! Enter a number in the range [1-7]");
                    break;
            }
        } while (choice != 7);
    }
}
