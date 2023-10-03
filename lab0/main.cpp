#include <iostream>
#include "Plane.h"
using namespace std;

int main() {
    Plane myPlane(true, 500.0, "White");

    myPlane.printState();

    return 0;
}
