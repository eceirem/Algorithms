#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> list1(n + 1, 0);

    int counter = 1;
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; j += counter) {
            if (list1[j] == 1) {
                list1[j] = 0;
            } else {
                list1[j] = 1;
            }
        }
        counter++;
    }

    for (int i = 1; i <= n; ++i) {
        if (list1[i] == 1) {
            std::cout << i << std::endl;
        }
    }

    return 0;
}
