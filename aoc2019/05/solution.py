#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(int, next(f).split(',')))

def execute(data, inputs):
    outputs = []
    pc = 0
    def get(op, n):
        return data[pc + n] if op // pow(10, n + 1) % 10 else data[data[pc + n]]
    while True:
        op = data[pc]
        match op % 100:
            case 1: data[data[pc + 3]] = get(op, 1) + get(op, 2); pc += 4
            case 2: data[data[pc + 3]] = get(op, 1) * get(op, 2); pc += 4
            case 3: data[data[pc + 1]] = inputs[0]; inputs = inputs[1:]; pc += 2
            case 4: outputs.append(get(op, 1)); pc += 2
            case 5:
                if get(op, 1): pc = get(op, 2)
                else: pc += 3
            case 6:
                if not get(op, 1): pc = get(op, 2)
                else: pc += 3
            case 7: data[data[pc + 3]] = int(get(op, 1) < get(op, 2)); pc += 4
            case 8: data[data[pc + 3]] = int(get(op, 1) == get(op, 2)); pc += 4
            case 99: return outputs

print(execute(data.copy(), [1])[-1])
print(execute(data.copy(), [5])[0])
