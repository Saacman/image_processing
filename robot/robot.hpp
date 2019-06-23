#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#define PI 3.14159265
using namespace std;

struct point {
  float x;
  float y;
};


class Robot {
public:
  Robot();

  Robot(float w, float h, float x0, float y0, float x1, float y1, float r = 3.0, int n = 10)

  float distance(point& other) {
    return sqrt(pow((p_one.x - p_two.x),2) + pow((p_one.y - p_two.y), 2));
  }


private:
  point goal;
  point past_pos;
  point actual_pos;
  int steps;
  int n;
  float radius;

}

#endif
