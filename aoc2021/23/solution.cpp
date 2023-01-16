#include <cstdio>
#include <cstdint>
#include <fstream>
#include <map>
#include <string>
#include <vector>

// There are 4 lines of rooms, 16 room cells, and 7 hallway cells:
//
// ·············
// ·65 4 3 2 10·  hall
// ···f·e·d·c···  room
//   ·b·a·9·8·    room
//   ·7·6·5·4·    room
//   ·3·2·1·0·    room
//   ·········

// Distances from room lines to hallway
static uint8_t const distances[4][7] =
{
    {  3,  2,  2,  4,  6,  8,  9 },
    {  5,  4,  2,  2,  4,  6,  7 },
    {  7,  6,  4,  2,  2,  4,  5 },
    {  9,  8,  6,  4,  2,  2,  3 },
};

struct move
{
    int src, dst;
};

struct state
{
    uint64_t m_rooms;
    uint32_t m_hallway;

    // Parse a string, either for part 1 or part 2. Only the ABCD characters are meaningful.
    void init(std::string const &s, int part)
    {
        m_hallway = 0; m_rooms = 0;
        for (auto c : s)
        {
            if (c >= 'A' && c <= 'D')
                m_rooms = (m_rooms << 4) | (c - 'A' + 1);
            if (part == 2 && (m_rooms & 0xf000) && !(m_rooms & 0xf0000))
                m_rooms = (m_rooms << 32) | 0x43214213;
        }
        if (part == 1)
            m_rooms = (m_rooms << 32) | 0x12341234;
    }

    int32_t solve() const
    {
        std::map<state, int32_t> costs;
        return get_cost(costs);
    }

private:
    void print() const
    {
        printf("#############\n#");
        for (int i = 7; i--;)
            printf(i <= 1 || i == 6 ? "%c" : "%c ", " ABCD"[peek_hall(i)]);
        printf("#\n###");
        for (int l = 4; l--;)
        {
            for (int i = 4; i--;)
                printf("%c#", " ABCD"[peek_room(l * 4 + i)]);
            printf(l == 3 ? "##\n  #" : l ? "\n  #" : "\n  #########\n");
        }
    }

    inline uint8_t peek_hall(int n) const { return (m_hallway >> (4 * n)) & 0xf; }
    inline uint8_t peek_room(int n) const { return (m_rooms >> (4 * n)) & 0xf; }

    // Return if the path is free between a room line and a hallway position
    inline bool is_path_free(int line, int hall) const
    {
        for (int n = hall + 1; n < line + 2; ++n)
            if (peek_hall(n))
                return false;
        for (int n = line + 2; n < hall; ++n)
            if (peek_hall(n))
                return false;
        return true;
    }

    // List possible moves for a given position
    std::vector<move> list_moves() const
    {
        std::vector<move> ret;

        // Count how many items are already arranged in the room lines
        uint8_t arranged[4] { 0 };
        for (int line = 0; line < 4; ++line)
            while (arranged[line] < 4 && 4 - peek_room(line + arranged[line] * 4) == line)
                ++arranged[line];

        // All exit moves
        for (int line = 0; line < 4; ++line)
        {
            if (arranged[line] == 4 || !peek_room(line + arranged[line] * 4))
                continue; // Everything is neatly arranged
            for (int room = line + 12; room >= 0; room -= 4)
            {
                if (!peek_room(room))
                    continue; // Skip to first non-empty room
                for (int hall = 0; hall < 7; ++hall)
                    if (!peek_hall(hall) && is_path_free(line, hall))
                        ret.push_back(move { room, hall + 16 });
                break;
            }
        }

        // All reentry moves
        for (int hall = 0; hall < 7; ++hall)
        {
            auto n = peek_hall(hall);
            if (n == 0)
                continue; // Empty hallway
            auto line = 4 - n;
            auto room = line + arranged[line] * 4;
            if (!peek_room(room) && is_path_free(line, hall))
                ret.push_back(move{ 16 + hall, room });
        }

        return ret;
    }

    // Get the cost of solving a given position. Cache history in a map for performance.
    int32_t get_cost(std::map<state, int32_t> &costs) const
    {
        if (m_rooms == state::end)
            return 0;

        auto cached = costs.find(*this);
        if (cached != costs.end())
            return std::get<1>(*cached);

        int32_t best_cost = 1000000;
        for (auto &move : list_moves())
        {
            auto s2 = *this;
            int32_t move_cost = s2.apply_move(move);
            best_cost = std::min(best_cost, move_cost + s2.get_cost(costs));
        }
        costs[*this] = best_cost;
        return best_cost;
    }

    // Apply a move in-place and return how much it cost
    int32_t apply_move(move m)
    {
        static int32_t const mul[4] = { 1, 10, 100, 1000 };
        int hallway = m.src >= 16 ? m.src - 16 : m.dst - 16;
        int room = m.src >= 16 ? m.dst : m.src;

        auto n = m.src >= 16 ? (m_hallway >> (4 * hallway)) & 0xf : (m_rooms >> (4 * room)) & 0xf;
        auto d = distances[room & 3][hallway] + (3 - room / 4);

        m_hallway ^= n << (4 * hallway);
        m_rooms ^= n << (4 * room);
        return d * mul[n - 1];
    }

    static uint64_t const end = 0x1234123412341234;
};

static bool operator <(state const &a, state const &b)
{
    return a.m_rooms == b.m_rooms ? a.m_hallway < b.m_hallway : a.m_rooms < b.m_rooms;
}

int main(void)
{
    std::ifstream t("input.txt");
    std::string input((std::istreambuf_iterator<char>(t)), std::istreambuf_iterator<char>());

    state s;
    s.init(input, 1);
    printf("%d\n", s.solve());

    s.init(input, 2);
    printf("%d\n", s.solve());
}
