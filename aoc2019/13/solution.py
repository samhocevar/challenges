#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(int, next(f).split(',')))

class cpu():
    def __init__(self, data):
        self.pc = 0
        self.rb = 0
        self.ram = data.copy()
        self.coro = self.run()
        self.out = []

    def send(self, n): self.coro.send(n)

    def get(self):
        n, self.out = self.out[0], self.out[1:]
        return n

    def run(self):
        while True:
            op = self.ram[self.pc]
            match op % 100:
                case 1: self.write(op, 3, self.read(op, 1) + self.read(op, 2)); self.pc += 4
                case 2: self.write(op, 3, self.read(op, 1) * self.read(op, 2)); self.pc += 4
                case 3: a = yield; self.write(op, 1, a); self.pc += 2
                case 4: self.out.append(self.read(op, 1)); self.pc += 2
                case 5:
                    if self.read(op, 1): self.pc = self.read(op, 2)
                    else: self.pc += 3
                case 6:
                    if not self.read(op, 1): self.pc = self.read(op, 2)
                    else: self.pc += 3
                case 7: self.write(op, 3, int(self.read(op, 1) < self.read(op, 2))); self.pc += 4
                case 8: self.write(op, 3, int(self.read(op, 1) == self.read(op, 2))); self.pc += 4
                case 9: self.rb += self.read(op, 1); self.pc += 2
                case 99: return

    def validate(self, loc):
        if loc is not None and len(self.ram) <= loc:
            self.ram.extend([0] * (loc + 1 - len(self.ram)))

    def address(self, op, n):
        param = self.ram[self.pc + n]
        match op // 10 ** (n + 1) % 10:
            case 0: return param, None
            case 1: return None, param
            case 2: return self.rb + param, None

    def read(self, op, n):
        loc, val = self.address(op, n)
        self.validate(loc)
        return val if loc is None else self.ram[loc]

    def write(self, op, n, val):
        loc, _ = self.address(op, n)
        self.validate(loc)
        self.ram[loc] = val

cabinet = cpu(data)
try:
    next(cabinet.coro)
except Exception as e:
    pass

screen = {}
while True:
    try:
        x, y, t = cabinet.get(), cabinet.get(), cabinet.get()
        screen[(x, y)] = t
    except StopIteration:
        pass
    except:
        print(sum(1 for t in screen.values() if t == 2))
        break
