#include <vector>
#include <cstdio>

using namespace std;

int main() {
    int H, W, X, Y;
    scanf("%d %d %d %d", &H, &W, &X, &Y);

    vector<vector<int>> B(H + X, vector<int>(W + Y));
    for (int i = 0; i < H + X; ++i) {
        for (int j = 0; j < W + Y; ++j) {
            scanf("%d", &B[i][j]);
        }
    }
    vector<vector<int>> A(H, vector<int>(W));
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (i >= X && j >= Y) {
                A[i][j] = B[i][j] - A[i-X][j-Y];
            }
            else {
                A[i][j] = B[i][j];
            }
        }
    }
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            printf("%d", A[i][j]);
            if (j != W - 1) printf(" ");
        }
        printf("\n");
    }
    return 0;
}