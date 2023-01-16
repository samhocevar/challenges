package main

import (
    "bufio"
    "os"
    "sort"
    "strconv"
)

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
    }
    list = append(list, sum)

    sort.Ints(list)
    list = list[len(list)-3:]

    println(list[2])
    println(list[0] + list[1] + list[2])
}
