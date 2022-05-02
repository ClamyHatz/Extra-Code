package edu.sfsu;
/*
 Assignment #4
 921804582@_HW04
 Lily Keus
 */
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        ArrayBag<String> bag = new ArrayBag<>();
        ArrayBag<String> bag2 = new ArrayBag<>();
        int choice = -1;

        do {
            System.out.println("[1] To add a new item to the bag");
            System.out.println("[2] To remove an item from the bag");
            System.out.println("[3] To remove a specific item from the bag");
            System.out.println("[4] To clear the bag");
            System.out.println("[5] To get a frequency of a given item in the bag");
            System.out.println("[6] To check if an item exist in the bag");
            System.out.println("[7] To print bag content");
            System.out.println("[8] To replace and item with another");
            System.out.println("[9] To combine two arrays");
            System.out.println("[10] To Exit");
            System.out.println("Enter your choice:");
            Scanner in = new Scanner(System.in);
            choice = in.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter item:");
                    String item = in.next();
                    if (bag.add(item)) {
                        System.out.println("Item " + item + " is added successfully to the bag");
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
                    item = in.next();
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
                    item = in.next();
                    System.out.println("The item " + item + " is found " + bag.getFrequencyOf(item) + " times");
                    break;
                case 6:
                    System.out.println("Enter the item you are looking for:");
                    item = in.next();
                    if (bag.contains(item)) {
                        System.out.println("The item " + item + " is in the bag");
                    } else {
                        System.out.println("The item " + item + " is NOT in the bag");
                    }
                    break;
                case 7:
                    if (bag.isEmpty()) {
                        System.out.println("Bag is empty!");
                    } else {
                        System.out.println("Bag content:");
                        System.out.println(Arrays.toString(bag.toArray()));
                    }
                    break;
                case 8:
                    System.out.println("Enter the item you want to change:");
                    item = in.next();
                    System.out.println("Enter the item you want to replace with:");
                    String item2 = in.next();
                    if (bag.contains(item)){
                        bag.replaceAll(item, item2);
                        System.out.println("Item " + item + " is replaced with " + item2);
                    } else {
                        System.out.println("The item " + item + " doesnt exist in the bag");
                    }
                    break;
                case 9:
                    System.out.println("Enter the length of the list:");
                    int len = in.nextInt();
                    for(int i = 0; i < len; i++){
                        System.out.println("Enter what goes in the other bag");
                        bag2.add(in.next());
                    }
                    bag.union(bag2);
                    bag2.clear();
                    break;
                case 10:
                    System.out.println("GoodBye!");
                    break;
                default:
                    System.out.println("Invalid choice! Enter a number in the range [1-9]");
                    break;
            }
        } while (choice != 10);
    }
}
