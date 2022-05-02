package com.company;

import java.util.Arrays;

public class bla {

        public static void main(String[]args){

            int [][] matrix = { {1, 1, 1, 2, 2}, {3, 3, 4, 4, 5}, {6, 6, 7, 7, 8}, {8, 9, 9, 10, 10}, {10, 11, 11, 12, 12} };

            System.out.println(Arrays.toString(uniqueValue(matrix)));

        }
        public static int[] uniqueValue(int [][] matrix){
            int output = 0;
            int out[] = new int[2];
            int [] numb = new int[12];
            for (int x = 0; x <= 4; x++) {
                for (int y = 0; y <= 4; y++){
                    int var = matrix[x][y];
                    switch (var){
                        case 1:
                            numb[0] = numb[0] + 1;
                            break;
                        case 2:
                            numb[1] = numb[1] + 1;
                            break;
                        case 3:
                            numb[2] = numb[2] + 1;
                            break;
                        case 4:
                            numb[3] = numb[3] + 1;
                            break;
                        case 5:
                            numb[4] = numb[4] + 1;
                            break;
                        case 6:
                            numb[5] = numb[5] + 1;
                            break;
                        case 7:
                            numb[6] = numb[6] + 1;
                            break;
                        case 8:
                            numb[7] = numb[7] + 1;
                            break;
                        case 9:
                            numb[8] = numb[8] + 1;
                            break;
                        case 10:
                            numb[9] = numb[9] + 1;
                            break;
                        case 11:
                            numb[10] = numb[10] + 1;
                            break;
                        case 12:
                            numb[11] = numb[11] + 1;
                            break;
                    }
                }
            }
            for (int i = 0; i <= 11; i++){
                int temp = numb[i];
                if (temp == 1){
                    output = i + 1;
                }
            }
            for (int x = 0; x <= 4; x++) {
                for (int y = 0; y <= 4; y++) {
                    int var = matrix[x][y];
                    if (var == output){
                        out[0] = x;
                        out[1] = y;
                        return out;
                    }
                }
            }
            return out;
    }
}
