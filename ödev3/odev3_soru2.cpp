#include <iostream>
#include <cmath> //pow

int lg(int n) {
    int m = 0;
    while (pow(2, m) < n) {
        m++;
    }
    return m;
}

int main() {
    int num;
    std::cin >> num;
    std::cout << lg(num);
    return 0;
}
