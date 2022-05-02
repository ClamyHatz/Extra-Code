package com.company;

public class Exam2 {
    /*********************************************************************************************/

    public static void main(String[]args){

        String input = "a3b3e3";

        System.out.println(writeString(input));

    }

    public static String writeString(String input){
        int length = 0;
        for(int i = 0; i < input.length(); i++) {
            char tempC = input.charAt(i);
            if (Character.isDigit(tempC)) {
                length = length + Character.getNumericValue(tempC);
            }
        }

        String output = "";
        char[] charList = new char[length];
        int placement = 0;

        for(int i = 0; i < input.length(); i++) {
            char tempC = input.charAt(i);
            if (Character.isDigit(tempC)) {
                int tempDig = tempC;
                int letterPart = i - 1;
                for (int u = Character.getNumericValue(tempDig); u > 0; u--) {
                    char tempCs = input.charAt(letterPart);
                    charList[placement] = tempCs;
                    placement++;
                }
            }
        }
        output = new String(charList);
        return output;
    }
}
