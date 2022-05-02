/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.sfsu;

import java.util.Arrays;

/**
 *
 * @author abeer
 */
public class ArrayStack<T> implements StackInterface<T> {

    private T[] stack; // array of stack entries
    private int topIndex1; // index of top entry
    private int topIndex2;
    private static final int DEFAULT_INITIAL_CAPACITY = 50;

    public ArrayStack() {
        this(DEFAULT_INITIAL_CAPACITY);
    }

    public ArrayStack(int initialCapacity) {
        // the cast is safe because the new array contains null entries
        @SuppressWarnings("unchecked")
        T[] tempStack = (T[]) new Object[initialCapacity];
        stack = tempStack;
        topIndex1 = -1;
        topIndex2 = initialCapacity;
    }

    private void ensureCapacity() {
        if (topIndex1 >= topIndex2 - 1) // if array is full,
        // double size of array
        {
            @SuppressWarnings("unchecked")
            T[] temp = (T[]) new Object[stack.length - topIndex2];
            for(int i = 0; i < temp.length; i++){
                temp[i] = pop2();
            }
            stack = Arrays.copyOf(stack, 2 * stack.length);
            topIndex2 = stack.length;
            for(int i = temp.length; i > 0; i--){
                push2(temp[i - 1]);
            }
        }
    } // end ensureCapacity

    @Override
    public void push1(T entry) {
        ensureCapacity();
        topIndex1++;
        stack[topIndex1] = entry;
    }

    @Override
    public T pop1() {
        T top = null;
        if (!isEmpty1()) {
            top = stack[topIndex1];
            stack[topIndex1] = null;
            topIndex1--;
        } // end if
        return top;
    }

    @Override
    public T peek1() {
        T top = null;
        if (!isEmpty1()) {
            top = stack[topIndex1];
        }
        return top;
    }

    @Override
    public boolean isEmpty1() {
        return topIndex1 < 0;
    }

    @Override
    public void push2(T entry) {
        ensureCapacity();
        topIndex2--;
        stack[topIndex2] = entry;
    }

    @Override
    public T pop2() {
        T top = null;
        if (!isEmpty2()) {
            top = stack[topIndex2];
            stack[topIndex2] = null;
            topIndex2++;
        } // end if
        return top;
    }

    @Override
    public T peek2() {
        T top = null;
        if (!isEmpty2()) {
            top = stack[topIndex2];
        }
        return top;
    }

    @Override
    public boolean isEmpty2() {
        return topIndex2 > stack.length - 1;
    }
}
