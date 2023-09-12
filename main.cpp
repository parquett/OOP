#include <iostream>
#include <string>
#include "plane.cpp"
int main() {
    Plane myPlane(true, 500.0, "White");

    myPlane.printState();

    return 0;
}
