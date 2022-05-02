/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.sfsu;

/**
 *
 * @author abeer
 */
public interface StackInterface<T> {
    public void push1(T entry);
    public T pop1();
    public T peek1();
    public boolean isEmpty1();

    public void push2(T entry);
    public T pop2();
    public T peek2();
    public boolean isEmpty2();
}
