package edu.sfsu;

import java.util.Arrays;

public class ArrayBag<T> implements BagInterface<T> {
    private T[] bag;
    private static final int DEFAULT_CAPACITY = 25;
    private int numberOfEntries;

    /**
     * Creates an empty bag whose initial capacity is 25.
     */
    public ArrayBag() {
        this(DEFAULT_CAPACITY);
    }

    /**
     * Creates an empty bag having a given initial capacity.
     *
     * @param capacity the integer capacity desired
     */
    public ArrayBag(int capacity) {
        numberOfEntries = 0;
        bag = (T[]) new Object[capacity];
    }

    @Override
    public int getCurrentSize() {
        return numberOfEntries;
    }

    /**
     * Sees whether this bag is full.
     *
     * @return true if the bag is full, or false if not
     */
    @Override
    public boolean isFull() {
        return numberOfEntries == bag.length;
    }

    @Override
    public boolean isEmpty() {
        return numberOfEntries == 0;
    }

    /**
     * Adds a new entry to this bag.
     *
     * @param newEntry the object to be added as a new entry
     * @return true if the addition is successful, or false if not
     */
    @Override
    public boolean add(T newEntry) {
        ensureCapacity();
        bag[numberOfEntries] = newEntry;
        numberOfEntries++;
        return true;
    }

    private void ensureCapacity() {
        if (numberOfEntries == bag.length) {
            bag = Arrays.copyOf(bag, 2 * bag.length);
        }
    }

    @Override
    public T remove() {
        T result = null;
        if (numberOfEntries > 0) {
            numberOfEntries--;
            result = bag[numberOfEntries];
            bag[numberOfEntries] = null;
        } // end if
        if (isTooBig()){
            reduceArray();
        }
        return result;
    }

    @Override
    public boolean remove(T anEntry) {
        int index = getIndexOf(anEntry);
        T result = removeEntry(index);
        if (isTooBig()){
            reduceArray();
        }
        return anEntry.equals(result);
    }

    @Override
    public void clear() {
        bag = (T[]) new Object[DEFAULT_CAPACITY];
    }

    /**
     * Counts the number of times a given entry appears in this bag.
     *
     * @param anEntry the entry to be counted
     * @return the number of times anEntry appears in the bag
     */
    @Override
    public int getFrequencyOf(T anEntry) {
        int counter = 0;
        for (int index = 0; index < numberOfEntries; index++) {
            if (anEntry.equals(bag[index])) {
                counter++;
            } // end if
        } // end for
        return counter;
    }

    /**
     * Tests whether this bag contains a given entry.
     *
     * @param anEntry the entry to locate\
     * @return true if the bag contains anEntry, or false otherwise
     */
    @Override
    public boolean contains(T anEntry) {
        boolean found = false;
        for (int index = 0; !found && (index < numberOfEntries); index++) {
            if (anEntry.equals(bag[index])) {
                found = true;
            } // end if
        } // end for
        return found;
    }

    /**
     * Retrieves all entries that are in this bag.
     *
     * @return a newly allocated array of all the entries in the bag
     */
    @Override
    public T[] toArray() {
        T[] result = (T[]) new Object[numberOfEntries]; // unchecked cast
        for (int index = 0; index < numberOfEntries; index++) {
            result[index] = bag[index];
        } // end for
        return result;
    }

    private int getIndexOf(T anEntry) {
        int where = -1;
        boolean found = false;
        for (int index = 0; !found && (index < numberOfEntries); index++) {
            if (anEntry.equals(bag[index])) {
                found = true;
                where = index;
            } // end if
        } // end for
// Assertion: If where > -1, anEntry is in the array bag, and it
// equals bag[where]; otherwise, anEntry is not in the array
        return where;
    }

    private T removeEntry(int givenIndex) {
        T result = null;
        if (!isEmpty() && (givenIndex >= 0)) {
            result = bag[givenIndex]; // entry to remove
            numberOfEntries--;
            bag[givenIndex] = bag[numberOfEntries]; // replace entry with last entry
            bag[numberOfEntries] = null; // remove last entry
        } // end if
        return result;
    }

    public void replaceAll(T oldItem, T newItem){
        int amount = getFrequencyOf(oldItem);
        for(int i = 0; i < amount; i++){
            int index = getIndexOf(oldItem);
            bag[index] = newItem;
        }
    }

    private boolean isTooBig(){
        return numberOfEntries < bag.length/2 && bag.length > 20;
    }
    private void reduceArray(){
        bag = Arrays.copyOf(bag, (3 * bag.length)/4);
    }

    public void union(ArrayBag<T> nextBag) {

        for (int i = 0; i < nextBag.numberOfEntries; i++) {
            if (!contains((T)nextBag.bag[i])) {
                add((T)nextBag.bag[i]);
            }
        }
    }
}
