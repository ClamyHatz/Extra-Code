package com.company;

import java.util.Arrays;

public class TwoSum {
    public static void main(String[]args) {
        int[] numbs = {3,3};
        int target = 6;
        System.out.println("Input: numbs = " + Arrays.toString(numbs) + ", target = " + target);
        System.out.println("Output: " + Arrays.toString(twoSum(numbs, target)));
    }
    public static int[] twoSum(int[] numbs, int target){
        int[] out = new int[2];
        for (int i = 0; i < numbs.length; i++){
            for(int u = i + 1; u < numbs.length; u++){
                if (numbs[i] + numbs[u] == target){
                    out[0] = i;
                    out[1] = u;
                    return out;
                }
            }
        }
        return out;
    }

}
