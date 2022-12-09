const std = @import("std");

const vec2 = @Vector(2, i32);

pub fn main() !void {
    var rope = std.mem.zeroes([10]vec2);
    var visited1 = std.AutoHashMap(vec2, void).init(std.heap.page_allocator);
    var visited2 = std.AutoHashMap(vec2, void).init(std.heap.page_allocator);

    var f = try std.fs.cwd().openFile("input.txt", .{});
    defer f.close();
    var s = std.io.bufferedReader(f.reader()).reader();
    var buf: [128]u8 = undefined;

    while (try s.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        const dir = switch (line[0]) {
            'U' => @Vector(2, i32){ 0, 1 },
            'D' => @Vector(2, i32){ 0, -1 },
            'L' => @Vector(2, i32){ -1, 0 },
            else => @Vector(2, i32){ 1, 0 },
        };

        var step = try std.fmt.parseInt(usize, line[2..], 10);
        while (step > 0) : (step -= 1) {
            rope[0] += dir;
            for (rope[0..rope.len-1]) |v, i| {
                var delta = rope[i + 1] - v;
                if ((2 == try std.math.absInt(delta[0])) or (2 == try std.math.absInt(delta[1]))) {
                    rope[i + 1] -= delta - @divTrunc(delta, vec2{2, 2});
                }
            }

            try visited1.put(rope[1], {});
            try visited2.put(rope[9], {});
        }
    }

    std.debug.print("{d}\n{d}\n", .{visited1.count(), visited2.count()});
}
