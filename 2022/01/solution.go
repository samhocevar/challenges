package main

import (
    "bufio"
    "os"
    "sort"
    "strconv"
)

func keep(list []int, n int) []int {
    sort.Ints(list)
    return list[len(list)-n:]
}

func main() {
    fd, _ := os.Open("input.txt")
    defer fd.Close()

    scanner := bufio.NewScanner(fd);
    list := []int{}
    sum := 0

    for scanner.Scan() {
        if line := scanner.Text(); line == "" {
            list = append(list, sum)
            sum = 0
        } else if n, err := strconv.Atoi(line); err == nil {
            sum += n
        }

        // Optional memory optimisation: whenever we have more than 100 elements, only keep the best 3
        if len(list) > 100 {
            list = keep(list, 3)
        }
    }
    list = append(list, sum)

    list = keep(list, 3)
    println(list[2])
    println(list[0] + list[1] + list[2])
}
