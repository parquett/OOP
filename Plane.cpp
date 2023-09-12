#include <iostream>
#include <string>
using namespace std;

class Plane {
public:
    // Constructor 
    Plane(bool isFlying, double speed, string color)
        : isFlying_(isFlying), speed_(speed), color_(color) {}

    void printState() const {
        cout << "Plane State: " << (isFlying_ ? "Flying" : "Standing") << endl;
        cout << "Speed: " << speed_ << " units per second" << endl;
        cout << "Color: " << color_ << endl;
    }

private:
    bool isFlying_;
    double speed_;
    string color_;
};

