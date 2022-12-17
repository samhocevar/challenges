#include <string>
#include <fstream>
#include <cstdio>
#include <map>
#include <vector>

int const search1 = 2022
int const search2 = 1000000000000

static const uint32_t shapes[] =
{
    0x0000000f, 0x00020702, 0x00040407, 0x01010101, 0x00000303
};

int main()
{
    std::ifstream t("input.txt");
    std::string input((std::istreambuf_iterator<char>(t)),
                       std::istreambuf_iterator<char>());
    while (input.back() == '\n' || input.back() == '\r')
        input.pop_back();

    size_t str_off = 0;
    size_t top = 0;
    size_t modulus = 5 * input.size();
    size_t delta_n = 0, delta_top = 0, confirmations = 0;

    std::map<uint64_t, std::tuple<size_t, size_t>> history;
    std::vector<uint8_t> grid;

    for (size_t n = 1; ; ++n)
    {
        while (grid.size() < top + 7)
            grid.push_back(0);

        uint32_t s = shapes[(n - 1) % 5] << 2;
        size_t y = top + 3;

        // Drop shape according to rules, update top accordingly
        for (;;)
        {
            uint32_t mask = grid[y] | (grid[y + 1] << 8) | (grid[y + 2] << 16) | (grid[y + 3] << 24);
            if (input[str_off++ % input.size()] == '>')
            {
                if (!(s & 0x40404040) && !((s << 1) & mask))
                    s <<= 1;
            }
            else
            {
                if (!(s & 0x01010101) && !((s >> 1) & mask))
                    s >>= 1;
            }

            if (y == 0 || s & (((mask & 0x00ffffff) << 8) | grid[y - 1]))
            {
                for (int i = 0; i < 4; ++i)
                    grid[y + i] |= (s >> i * 8) & 0xff;
                while (grid[top])
                    ++top;
                break;
            }
            --y;
        }

        // Each time the input and the shapes do a full cycle, check in our history whether
        // the same top 8 lines were found. Repeat the test 100 times to make sure we are
        // really caught in a loop.
        if (n % modulus == 0)
        {
            uint64_t state = 0;
            for (int i = 0; i < 8; ++i)
                state = (state << 8) | grid[top - i];

            auto prev = history.find(state);
            if (prev != history.end())
            {
                auto old_n = std::get<0>(prev->second);
                auto old_top = std::get<1>(prev->second);
                if (n - old_n > delta_n)
                {
                    delta_n = n - old_n;
                    delta_top = top - old_top;
                    confirmations = 1;
                }
                else if (n - old_n == delta_n)
                    ++confirmations;
            }
            else
                confirmations = 0;

            history[state] = std::tuple(n, top);
        }

        if (n == search1)
            printf("%lld\n", top);

        if (confirmations > 100 && (n % delta_n == search2 % delta_n))
        {
            auto k = (search2 - n) / delta_n;
            printf("%lld\n", top + k * delta_top);
            break;
        }
    }
}
