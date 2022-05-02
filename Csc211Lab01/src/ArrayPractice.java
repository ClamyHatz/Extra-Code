public class ArrayPractice {
    public static void main(String[] args) {
        int[] scores = new int[100]; // creates an array that has 100 slots

        for (int i = 0; i < 100; i++){ //cycles 100 times
            int val = (int)(Math.random() * 100); // creates a random number between 0 and 100
            scores[i] = val; //adds the random number to the next spot in the array
        }

        int index = 1;

        scores[index] = 50; // sets the second position in the array to 50

        System.out.println("Employee " + index + " has a score of " + scores[index]);
        System.out.println(scores.length); // prints out length of list

        //Part 2:

        int sum = 0;

        for (int i = 0; i < 100; i++){ // cycles 100 times
            sum = sum + scores[i]; //takes sum and adds it to the selected score in scores
        }
        double average = sum / (scores.length); //gets teh average of sum

        System.out.println("Average Score: " + average);
    }
}

