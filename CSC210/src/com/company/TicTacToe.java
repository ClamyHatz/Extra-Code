//TicTacToe game implemented with 2d arrays
package com.company;

import java.util.Scanner;

public class TicTacToe{
      //global declared
      static char [][] cell = new char[3][3];
      static int count = 0;

  public static void main(String[]args){
      //fill all the space with the space separator
      for(int i=0; i<cell.length; i++){
        for(int j=0; j<cell[i].length; j++){
          cell[i][j] = '\u00A0';
        }
      }
      while(count < 9){

          showCell();
          checkGame();
          player_x();
          showCell();
          checkGame();
          if(count == 9){
            System.out.println("\nNobody Wins!\n");
            break;
          }
          player_o();

      }

  }

  public static void player_x(){

      //create scanner object
      Scanner input = new Scanner(System.in);
      //prompt the user to enter row 0,1, or 2 for player X
      System.out.print("Enter row 0,1, or 2 for player X: ");
      //assign the user input integer to row variable
      int row = input.nextInt();
      //prompt the user to enter column 0,1, or 2 for player X
      System.out.print("Enter col 0,1, or 2 for player X: ");
      //assign the user input integer to col variable
      int col = input.nextInt();
      //while loop to check cell[row][col] != '\u00A0'
      if (cell[row][col] != '\u00A0') {
          System.out.println("No");
          if (cell[row][col] == 'x'){
              cell[row][col] = 'x';
          }
          if (cell[row][col] == 'o'){
              cell[row][col] = 'o';
          }
          player_x();
      }
      else{
          cell[row][col] = 'x';
          //incrment the count variable
          count++;
      }


  }//player_x method

  public static void player_o(){

      //create the scanner object
      Scanner input = new Scanner(System.in);
      //prompt the user to enter row 0,1, or 2 for player O
      System.out.print("Enter row 0,1, or 2 for player O: ");
      //assign the user input integer to row variable
      int row = input.nextInt();
      //prompt the user to enter column 0,1, or 2 for player O
      System.out.print("Enter col 0,1, or 2 for player O: ");
      //assign the user input integer to col variable
      int col = input.nextInt();
      //while loop to check cell[row][col] != '\u00A0'
      if (cell[row][col] != '\u00A0') {
          System.out.println("No");
          if (cell[row][col] == 'x'){
              cell[row][col] = 'x';
          }
          if (cell[row][col] == 'o'){
              cell[row][col] = 'o';
          }
          player_o();
      }
      else{
          cell[row][col] = 'o';
          //incrment the count variable
          count++;
      }



  }//player_o method

  public static void showCell(){
      System.out.println("---------------");
      System.out.printf(" | %c | %c | %c | \n", cell[0][0], cell[0][1], cell[0][2]);
      System.out.println("---------------");
      System.out.printf(" | %c | %c | %c | \n", cell[1][0], cell[1][1], cell[1][2]);
      System.out.println("---------------");
      System.out.printf(" | %c | %c | %c | \n", cell[2][0], cell[2][1], cell[2][2]);
      System.out.println("---------------");

  }//showCell method

  public static void checkGame(){
      for(int i  = 0; i < 3; i++){
          if (cell[i][0] == 'o' && cell[i][1] == 'o' && cell[i][2] == 'o'){
              System.out.println("Player o Wins!");
              System.exit(0);
          }
          else if(cell[0][i] == 'o' && cell[1][i] == 'o' && cell[2][i] == 'o'){
              System.out.println("Player o Wins!");
              System.exit(0);
          }
      }
      if (cell[0][0] == 'o' && cell[1][1] == 'o' && cell[2][2] == 'o'){
          System.out.println("Player o Wins!");
          System.exit(0);
      }
      if (cell[0][2] == 'o' && cell[1][1] == 'o' && cell[2][0] == 'o'){
          System.out.println("Player o Wins!");
          System.exit(0);
      }
      for(int i  = 0; i < 3; i++){
          if (cell[i][0] == 'x' && cell[i][1] == 'x' && cell[i][2] == 'x'){
              System.out.println("Player x Wins!");
              System.exit(0);
          }
          else if(cell[0][i] == 'x' && cell[1][i] == 'x' && cell[2][i] == 'x'){
              System.out.println("Player x Wins!");
              System.exit(0);
          }
      }
      if (cell[0][0] == 'x' && cell[1][1] == 'x' && cell[2][2] == 'x'){
          System.out.println("Player x Wins!");
          System.exit(0);
      }
      if (cell[0][2] == 'x' && cell[1][1] == 'x' && cell[2][0] == 'x'){
          System.out.println("Player x Wins!");
          System.exit(0);
      }

  }//checkGame method

}
