package com.company;
/*
Assignment #07
921804582@_HW07
Lily Keus
 */
import java.util.*;

public class Main {
    public static void GenerateProcesses(Queue IPQ){
        for(int i = 0; i < 10; i++){
            Process p = new Process(i + 1, (int)Math.floor(Math.random()*(100-1+1)+1));
            IPQ.add(p);
            System.out.println("Currently adding process: "+p);
        }
    }
    public static void ServerProcesses(Queue IPQ){
        int s = IPQ.size();
        for(int i=0;i < s;i++){
            Object p = IPQ.remove();
            System.out.println("Currently processing process: "+p);
        }
    }

    public static void main(String[] args) {
        Queue<Process> IPQ = new PriorityQueue<>(10);
        GenerateProcesses(IPQ);
        ServerProcesses(IPQ);
    }
}
