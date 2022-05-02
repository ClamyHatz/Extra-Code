package edu.sfsu;

import java.util.Arrays;
import java.util.Scanner;
/*
    Assignment #5
    921804582@_HW05
    Lily Keus
 */
public class Main {

    public static void main(String[] args) {
        NodeBasedBag<Coin> bag = new NodeBasedBag<>();
        int choice = -1;

        do {
            System.out.println("[1] Adding a coin");
            System.out.println("[2] Removing a coin");
            System.out.println("[3] Removing a specific coin");
            System.out.println("[4] Clear the bag");
            System.out.println("[5] Get the frequency of a given coin");
            System.out.println("[6] Check if specific coin exists in the bag");
            System.out.println("[7] Get minimum coin value");
            System.out.println("[8] Get maximum");
            System.out.println("[9] Print bag contents");
            System.out.println("[10] Print bag contents ordered");
            System.out.println("[11] Exit");
            System.out.println("Enter your choice:");
            Scanner in = new Scanner(System.in);
            choice = in.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter the coins value:");
                    int x = in.nextInt();
                    Coin item = new Coin(x);
                    if (x == 10 || x == 25 || x == 75 || x == 100) {
                        if (bag.add(item)) {
                            System.out.println("Item " + item + " is added successfully to the bag");
                        }
                    }
                    else {
                        System.out.println("Item " + x + " was not added to the bag");
                        System.out.println("Try adding 10, 25, 75, or 100");
                    }
                    break;
                case 2:
                    if (bag.isEmpty()) {
                        System.out.println("Bag is empty!");
                    } else {
                        System.out.println("Item " + bag.remove() + " is removed successfully");
                    }
                    break;
                case 3:
                    System.out.println("Enter the item you want to remove from the bag:");
                    x = in.nextInt();
                    item = new Coin(x);
                    if (bag.contains(item)) {
                        bag.remove(item);
                        System.out.println("Item " + item + " is removed from the bag");
                    } else {
                        System.out.println("The item " + item + " doesnt exist in the bag");
                    }
                    break;
                case 4:
                    bag.clear();
                    System.out.println("Bag is empty now!");
                    break;
                case 5:
                    System.out.println("Enter the item you are looking for:");
                    x = in.nextInt();
                    item = new Coin(x);
                    System.out.println("The item " + item + " is found " + bag.getFrequencyOf(item) + " times");
                    break;
                case 6:
                    System.out.println("Enter the item you are looking for:");
                    x = in.nextInt();
                    item = new Coin(x);
                    if (bag.contains(item)) {
                        System.out.println("The item " + item + " is in the bag");
                    } else {
                        System.out.println("The item " + item + " is NOT in the bag");
                    }
                    break;
                case 7:
                    if(bag.isEmpty()){
                        System.out.println("Bag is empty!");
                    } else{
                        System.out.println("The minimum value in the bag is: " + bag.minVal());
                    }
                    break;
                case 8:
                    if(bag.isEmpty()){
                        System.out.println("Bag is empty!");
                    } else{
                        System.out.println("The maximum value in the bag is: " + bag.maxVal());
                    }
                    break;
                case 9:
                    if (bag.isEmpty()) {
                        System.out.println("Bag is empty!");
                    } else {
                        System.out.println("Bag content:");
                        System.out.println(Arrays.toString(bag.toArray()));
                    }
                    break;
                case 10:
                    if(bag.isEmpty()){
                        System.out.println("Bag is empty!");
                    } else{
                        System.out.println("Sorted bag content:");
                        System.out.println(Arrays.toString(bag.sortArray()));
                    }
                    break;
                case 11:
                    System.out.println("GoodBye!");
                    break;
                default:
                    System.out.println("Invalid choice! Enter a number in the range [1-9]");
                    break;
            }
        } while (choice != 11);
    }
}
