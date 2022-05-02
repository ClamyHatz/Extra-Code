/*
 * Lab 8
 * Description: Prints and adds to a garden (which is a 2D array)
 * Name: Lily Keus
 * ID: 921804582
 * Class: CSC 211-02
 * Semester: 2021 - 2
 */
public class Garden {
    public static void main(String[] args) {
        int[][] garden = new int[4][3]; //create a new 2D array that is 4 by 3
        garden[3][0] = 1; // col 3 row 0 is set to 1
        garden[1][1] = 1; // col 1 row 1 is set to 1
        garden[3][2] = 1; // col 3 row 2 is set to 1
        System.out.println("First Garden:");
        printGarden(garden); //calls printGarden method
        System.out.println();
        System.out.println("Second Garden: ");
        addFlower(garden, 1, 0); //calls addFlower method
        printGarden(garden); //calls printGarden method
        System.out.println("Flowers in Col 1: " + countFlowersColumn(garden, 1)); //calls and prints countFlowersColumn method
        System.out.println("Flowers in Row 1: " + countFlowersRow(garden, 1)); //calls and prints countFlowersRow method
    }

    public static void printGarden(int[][]garden){
        for(int y = 0; y < 3; y++) { // loops 3 times
            for (int x = 0; x < 4; x++) { // loops 4 times
                System.out.print(garden[x][y] + " "); //prints value in position of x and y
            }
            System.out.println(); //makes new line
        }
    }
    public static void addFlower(int[][] garden, int column, int row){
        garden[column][row] = 1; // changes set position to 1
    }
    public static int countFlowersColumn(int[][] garden, int column){
        int flowerCount = 0; //new variable set to 0
        for(int i = 0; i < 3; i++){ // loops 3 times
            if(garden[column][i] == 1){ //checks if variable is 1
                flowerCount++; //adds 1 to flower count
            }
        }
        return flowerCount; // returns flower count
    }
    public static int countFlowersRow(int[][] garden, int row){
        int flowerCount = 0; //new variable set to 0
        for(int i = 0; i < 4; i++){  // loops 4 times
            if(garden[i][row] == 1){ //checks if variable is 1
                flowerCount++; //adds 1 to flower count
            }
        }
        return flowerCount; // returns flower count
    }
}
