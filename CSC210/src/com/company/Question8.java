package com.company;
public class Question8 {

    public static void main(String [] args) {

        int i, sum = 0;

        for( i = 5; i > 3; i-- ) {

            sum = sum + i;

            while( sum < 12 ) {

                sum = sum * 2 - 3;

                System.out.println(sum);

            }

            System.out.println( i + " " + sum );

        }

    }

}
