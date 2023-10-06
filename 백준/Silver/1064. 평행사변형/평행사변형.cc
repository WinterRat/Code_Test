#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

double distance(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main() {
    double x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    double cross_Product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
    if (cross_Product == 0) {
        cout << -1 << endl;
        return 0;
    }

    double dist1 = distance(x1, y1, x2, y2);
    double dist2 = distance(x1, y1, x3, y3);
    double dist3 = distance(x2, y2, x3, y3);

    double maxDist = max({dist1, dist2, dist3});
    double minDist = min({dist1, dist2, dist3});

    printf("%.10f\n", 2 * (maxDist - minDist));

    return 0;
}