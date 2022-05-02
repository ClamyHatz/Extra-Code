package com.company;

public class Square extends Rectangle{

    private double side;

    public Square(double side) {
        this.side = side;
    }

    public Square(double side, String color, boolean filled) {
        super(side, side, color, filled);
    }

    public Square() {

    }

    public double getSide() {
        return side;
    }

    public void setSide(double side) {
        super.length = side;
        super.width = side;
    }

    public void setLength(double side){
        super.length = side;
    }

    public void setWidth(double side){
        super.width = side;
    }



    @Override
    public String toString() {
        return "Square{" +
                "side=" + side +
                '}';
    }
}
