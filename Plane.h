#ifndef PLANE_H
#define PLANE_H

#include <string>
using namespace std;

class Plane {
public:
    Plane(bool isMoving, double speed, string color);

    void printState() const;

private:
    bool isMoving_;
    double speed_;
    string color_;
};

#endif
