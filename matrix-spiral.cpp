#include <iostream>
using namespace std;

#define m 5
#define n 5

void printSpiralOrder(int mat[m][n])
{
    int row = m;
    int col = n;
    int right = 0, left = col - 2, up = row - 2, down = 0;
    while (1)
    {
        // right path
        if (right < col)
        {
            cout << mat[down][right] << " -> ";
            right++;
            continue;
        }
        else if (down + 1 < row) // down path
        {
            cout << mat[down + 1][right - 1] << " -> ";
            down++;
            continue;
        }
        else if (left > n - col - 1) //left path
        {
            cout << mat[down][left] << " -> ";
            left--;
            continue;
        }
        else if (up > m - row) //up path
        {
            cout << mat[up][left + 1] << " -> ";
            up--;
            continue;
        }
        else
        {
            row--;
            col--;
            right = n - col;
            if (right >= col)
            {
                break;
            }
            left = col - 2;
            up = row - 2;
            down = m - row;
        }
    }
}

int main()
{
    //  input matrix
    cout << "Printing given matrix in spiral order..." << endl;
    int matrix[m][n] = {{1, 2, 3, 4, 5},
                        {16, 17, 18, 19, 6},
                        {15, 24, 25, 20, 7},
                        {14, 23, 22, 21, 8},
                        {13, 12, 11, 10, 9}};

    printSpiralOrder(matrix);
    cout << "\n\n";
    return 0;
}
