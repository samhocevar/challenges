#include <cstdio>
#include <cstdint>
#include <fstream>
#include <map>
#include <string>
#include <vector>

// There are 8 room cells and 7 hallway cells:
//
// ·············
// ·65 4 3 2 10·  hall
// ···7·6·5·4···  room
//   ·3·2·1·0·    room
//   ·········

// Distances from room to hall
static uint8_t const distances[8][7] =
{
    {  4,  3,  3,  5,  7,  9, 10 },
    {  6,  5,  3,  3,  5,  7,  8 },
    {  8,  7,  5,  3,  3,  5,  6 },
    { 10,  9,  7,  5,  3,  3,  4 },

    {  3,  2,  2,  4,  6,  8,  9 },
    {  5,  4,  2,  2,  4,  6,  7 },
    {  7,  6,  4,  2,  2,  4,  5 },
    {  9,  8,  6,  4,  2,  2,  3 },
};

// Blockers from room to hall
static uint64_t blockers[8][7];

static inline uint64_t room_pos(int n) { return (uint64_t)0x1 << (4 * n); }
static inline uint64_t hall_pos(int n) { return (uint64_t)0x1 << (4 * (n + 8)); }

static uint8_t const A = 1;
static uint8_t const B = 2;
static uint8_t const C = 3;
static uint8_t const D = 4;

static inline uint8_t final_room(uint8_t val) { return 4 - val; }
static inline uint8_t peek_room(uint64_t state, int n) { return (state >> (4 * n)) & 0xf; }
static inline uint8_t peek_hall(uint64_t state, int n) { return (state >> (4 * (n + 8))) & 0xf; }

#if 0
static void print_state(uint64_t state)
{
    printf("#############\n#");
    for (int i = 7; i--;)
        printf(i <= 1 || i == 6 ? "%c" : "%c ", " ABCD"[peek_hall(state, i)]);
    printf("#\n###");
    for (int i = 8; i-- > 4;)
        printf("%c#", " ABCD"[peek_room(state, i)]);
    printf("##\n  #");
    for (int i = 4; i--;)
        printf("%c#", " ABCD"[peek_room(state, i)]);
    printf("\n  #########\n");
}
#endif

static uint64_t parse_state(std::string const &s)
{
    uint64_t ret = 0;
    for (auto c : s)
        if (c >= 'A' && c <= 'D')
             ret = (ret << 4) | (c - 'A' + 1);
    return ret;
}

struct move
{
    int src, dst;
};

static std::vector<move> get_moves(uint64_t state)
{
    std::vector<move> ret;
    // All exit moves
    for (int room = 0; room < 8; ++room)
    {
        auto n = peek_room(state, room);
        if (n == 0)
            continue; // Empty room
        if (room < 4 && room == final_room(n))
            continue; // Already in place in bottom row
        if (room >= 4 && room - 4 == final_room(n) && n == peek_room(state, room - 4))
            continue; // Already in place in top row
        for (int hall = 0; hall < 7; ++hall)
        {
            if (peek_hall(state, hall))
                continue; // Destination is occupied
            if (state & blockers[room][hall])
                continue; // Someone’s in the way
            ret.push_back(move{ room, 8 + hall });
        }
    }
    // All reentry moves
    for (int hall = 0; hall < 7; ++hall)
    {
        auto n = peek_hall(state, hall);
        if (n == 0)
            continue; // Empty hallway
        auto room = final_room(n);
        if (peek_room(state, 4 + room) == 0)
        {
            auto m = peek_room(state, room);
            if (m == 0 && !(state & blockers[room][hall]))
                ret.push_back(move{ 8 + hall, room });
            else if (m == n && !(state & blockers[room + 4][hall]))
                ret.push_back(move{ 8 + hall, 4 + room });
        }
    }
    return ret;
}

static uint64_t end_state = parse_state("ABCDABCD");

static std::map<uint64_t, int32_t> costs;

static int32_t get_cost(uint64_t state)
{
    if (state == end_state)
        return 0;
    auto cached = costs.find(state);
    if (cached != costs.end())
        return std::get<1>(*cached);
    int32_t best_cost = 100000;
    for (auto &move : get_moves(state))
    {
        static int32_t const mul[4] = { 1, 10, 100, 1000 };
        auto n = (state >> (4 * move.src)) & 0xf;
        auto d = move.src > move.dst ? distances[move.dst][move.src - 8]
                                     : distances[move.src][move.dst - 8];
        auto s = state - (n << (4 * move.src)) + (n << (4 * move.dst));
        int32_t move_cost = d * mul[n - 1];
        best_cost = std::min(best_cost, move_cost + get_cost(s));
    }
    costs[state] = best_cost;
    return best_cost;
}

int main(void)
{
    // Rooms 4, 5, 6, 7 block rooms 0, 1, 2, 3
    for (int room = 0; room < 4; ++room)
        for (int hall = 0; hall < 7; ++hall)
            blockers[room][hall] |= 0xf * room_pos(room + 4);
    // Hallways block other hallways
    for (int room = 0; room < 4; ++room)
    {
        for (int hall = 0; hall < 7; ++hall)
        {
            for (int n = hall + 1; n < room + 2; ++n)
            {
                blockers[room][hall] |= 0xf * hall_pos(n);
                blockers[room + 4][hall] |= 0xf * hall_pos(n);
            }
 
            for (int n = room + 2; n < hall; ++n)
            {
                blockers[room][hall] |= 0xf * hall_pos(n);
                blockers[room + 4][hall] |= 0xf * hall_pos(n);
            }
        }
    }

    std::ifstream t("input.txt");
    std::string input((std::istreambuf_iterator<char>(t)), std::istreambuf_iterator<char>());
    uint64_t state = parse_state(input);

    printf("%d\n", get_cost(state));
}

