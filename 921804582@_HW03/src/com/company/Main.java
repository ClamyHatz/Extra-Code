package com.company;
/*
 Assignment #3
 921804582@_HW03
 Lily Keus
 */
public class Main {

    public static void main(String[] args) {

        Shape s1 = new Circle(5.5, "RED", false); // Upcast Circle to Shape
        System.out.println(s1); //This is being called from the Circle class
        System.out.println(s1.getArea()); // Circle class
        System.out.println(s1.getPerimeter()); // Circle class
        System.out.println(s1.getColor()); //Circle class
        System.out.println(s1.isFilled()); //Circle class
        System.out.println(s1.getRadius()); //Circle class //This doesn't work because Shape doesn't have a getRadius method.
        Circle c1 = (Circle)s1; // Downcast back to Circle
        System.out.println(c1); //Circle class
        System.out.println(c1.getArea()); //Circle class
        System.out.println(c1.getPerimeter()); //Circle class
        System.out.println(c1.getColor()); //Circle class
        System.out.println(c1.isFilled()); //Circle class
        System.out.println(c1.getRadius()); //Circle class
        Shape s2 = new Shape(); //This doesn't work because you cannot create an object based of an abstract class
        Shape s3 = new Rectangle(1.0, 2.0, "RED", false); // Upcast
        System.out.println(s3); //Rectangle class
        System.out.println(s3.getArea()); //Rectangle class
        System.out.println(s3.getPerimeter()); //Rectangle class
        System.out.println(s3.getColor()); //Rectangle class
        System.out.println(s3.getLength()); //Rectangle class //This doesn't work because Shape doesn't have a getLength method.
        Rectangle r1 = (Rectangle)s3; // downcast
        System.out.println(r1); //Rectangle class
        System.out.println(r1.getArea()); //Rectangle class
        System.out.println(r1.getColor()); //Rectangle class
        System.out.println(r1.getLength()); //Rectangle class
        Shape s4 = new Square(6.6); // Upcast
        System.out.println(s4); //Square class
        System.out.println(s4.getArea()); //Square class
        System.out.println(s4.getColor()); //Square class
        System.out.println(s4.getSide()); //Square class //This doesn't work because Shape doesn't have a getSide method.
// Take note that we downcast Shape s4 to Rectangle,

// which is a superclass of Square, instead of Square
        Rectangle r2 = (Rectangle)s4; //Downcast Shape s4 to Rectangle r2
        System.out.println(r2); //Square class
        System.out.println(r2.getArea()); //Square class
        System.out.println(r2.getColor()); //Square class
        System.out.println(r2.getSide()); //Square class //This doesn't work because Rectangle doesn't have a getSide method.
        System.out.println(r2.getLength()); //Square class
// Downcast Rectangle r2 to Square
        Square sq1 = (Square)r2; //Downcast Rectangle r2 to Square sq1
        System.out.println(sq1); //Square class
        System.out.println(sq1.getArea()); //Square class
        System.out.println(sq1.getColor()); //Square class
        System.out.println(sq1.getSide()); //Square class
        System.out.println(sq1.getLength()); //Square class
    }
}
/*
  Abstract methods cannot be used. Abstract classes cannot create an object. the main use for abstract methods is to have
  their kids use it in later methods, for the abstract methods can not be used themselves. Abstract Classes can not create
  an object, the abstract classes are used as a basis for future classes to inherit their variables and methods.
 */