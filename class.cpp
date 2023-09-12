#include <iostream>
#include <string>
using namespace std;
class Object {
public:
    Object(bool isMoving, double speed, string color)
        : isMoving_(isMoving), speed_(speed), color_(color) {}

    void printState() const {
        cout << "Object State: " << (isMoving_ ? "Moving" : "Standing") << endl;
        cout << "Speed: " << speed_ << " units per second" << endl;
        cout << "Color: " << color_ << endl;
    }

private:
    bool isMoving_;
    double speed_;
    string color_;
};
