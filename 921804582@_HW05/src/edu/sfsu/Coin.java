package edu.sfsu;

import java.util.Objects;

public class Coin implements Comparable{

    public int coinValue;

    public Coin(int coinValue) {
        this.coinValue = coinValue;
    }

    public int getCoinValue() {
        return coinValue;
    }

    public void setCoinValue(int coinValue) {
        this.coinValue = coinValue;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coin coin = (Coin) o;
        return coinValue == coin.coinValue;
    }

    @Override
    public int hashCode() {
        return Objects.hash(coinValue);
    }

    @Override
    public String toString() {
        return ""+coinValue;
    }



    @Override
    public int compareTo(Object o) {
        return  (this.getCoinValue() < ((Coin) o).getCoinValue() ? -1 : (this.getCoinValue() == ((Coin) o).getCoinValue() ? 0 : 1));
    }

}
