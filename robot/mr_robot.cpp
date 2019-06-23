#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <opencv2/opencv.hpp>

#define PI 3.14159265
using namespace std;
using namespace cv;

// Prototipos
float random_angle();
float distance(Point2f, Point2f);
bool update(Point2f&, int, Point2f&, float, Point2f&, int, int);
void drawCircle(Point2f , Mat&);

int main() {
  srand((int)time(0));

  int steps = 1000;
  int n = 10;
  float radius = 100;
  Point2f past, goal, actual;
  int width, height;

  // Entrada del usuario
  cout << "Enter the map dimensions" << endl;
  cin >> width; cin >> height;
  cout << "Enter the initial position" << endl;
  cin >> actual.x; cin >> actual.y;
  cout << "Enter the Goal Position" << endl;
  cin >> goal.x; cin >> goal.y;

  Mat image = Mat::zeros( width, height, CV_8UC3 );

  drawCircle(actual, image);
  drawCircle(goal, image);
  
  while((distance(actual, goal) > radius/2) && (steps > 0)) {
    cout << "La posición actual es: (" << actual.x << ", " << actual.y << ")" << endl;
    steps--;
    update(actual, n, goal, radius, past, width, height);
    line(image, past, actual, Scalar(255, 127, 0), 3, CV_AA);
  }
  cout << "La posición final es: (" << actual.x << ", " << actual.y << ")" << endl;
  imshow("Ruta", image);
  waitKey();
  destroyAllWindows();
  return 0;
}

// Funciones usadas
float random_angle() {
  return rand() % 360 ;
}

float distance(Point2f p_one, Point2f p_two) {
  return sqrt(pow((p_one.x - p_two.x),2) + pow((p_one.y - p_two.y), 2));
}

bool update(Point2f& actual, int n, Point2f& goal, float radius, Point2f& past, int width, int height) {
  for(int i = 0; i < n; i++) {
    float alpha = (random_angle() * PI) / 180 ;
    Point2f posible;
    posible.x = actual.x + radius * cos(alpha);
    posible.y = actual.y + radius * sin(alpha);
    if(distance(posible, goal) < distance(actual, goal)) {
      //if((posible.x > 0.0 && posible <= width) && (posible.y > 0.0 && posible <= height))
      past = actual;
      actual = posible;
      return true;
    }
  }
  return false;
}

void drawCircle(Point2f point, Mat& image) {
  circle(image, point, 15, (0, 10, 255), -1);
}
