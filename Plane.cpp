#include "Plane.h"
#include <iostream>
using namespace std;

Plane::Plane(bool isMoving, double speed, string color)
    : isMoving_(isMoving), speed_(speed), color_(color) {}

void Plane::printState() const {
    cout << "Plane State: " << (isMoving_ ? "Moving" : "Standing") << endl;
    cout << "Speed: " << speed_ << " units per second" << endl;
    cout << "Color: " << color_ << endl;
}
