use std::collections::BinaryHeap;
use std::fs::File;
use std::io::{prelude::*, BufReader, Result};

fn main() -> Result<()> {
    let fd = File::open("input.txt")?;

    let mut heap = BinaryHeap::new();
    let mut sum = 0;

    // Parse file and feed the heap with partial sums
    let br = BufReader::new(fd);
    for l in br.lines() {
        match l?.parse::<i32>() {
            Ok(n) => sum += n,
            Err(_) => { heap.push(sum); sum = 0; },
        }
    }
    heap.push(sum);

    // Print largest value
    let mut best = 0;
    match heap.peek() { None => {}, Some(n) => best = *n }
    println!("{}", best);

    // Print sum of three largest values
    let mut best3 = 0;
    for _ in 0..3 {
        match heap.pop() { None => {}, Some(n) => best3 += n }
    }
    println!("{}", best3);

    Ok(())
}
