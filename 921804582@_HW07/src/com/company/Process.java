package com.company;

public class Process implements Comparable{
    protected int ID;
    protected int priority;

    public Process(int ID, int priority) {
        this.ID = ID;
        this.priority = priority;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    @Override
    public String toString() {
        return "ID:" + ID + " with priority " + priority;
    }

    @Override
    public int compareTo(Object o) {
        return (this.getPriority() < ((Process) o).getPriority() ? 1 : (this.getPriority() == ((Process) o).getPriority() ? 0 : -1));
    }
}
