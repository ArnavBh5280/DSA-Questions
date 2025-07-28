#include <string>

class Solution {
public:
    int findNthDigit(int n) {
        long long digitLength = 1;
        long long count = 9;
        long long start = 1;

        while (n > digitLength * count) {
            n -= digitLength * count;
            digitLength++;
            count *= 10;
            start *= 10;
        }

        start += (n - 1) / digitLength;
        std::string number = std::to_string(start);
        return number[(n - 1) % digitLength] - '0';
    }
};
