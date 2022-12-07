use std::fs;
use std::iter::zip;
use multiset::HashMultiSet;

fn parse(s: &String, n: usize) -> usize {
    let mut stats: HashMultiSet<char> = HashMultiSet::new();
    let mut front = s.chars().into_iter();
    let back = s.chars().into_iter();

    // Initialise multiset with n-1 elements
    for _ in 1..n {
        stats.insert(front.next().unwrap());
    }

    for (i, (f, b)) in zip(front, back).enumerate() {
        stats.insert(f);
        if stats.distinct_elements().count() == n { return i + n; }
        stats.remove(&b);
    }
    0
}

fn main() {
    let s: String = fs::read_to_string("input.txt").unwrap();

    println!("{}", parse(&s, 4));
    println!("{}", parse(&s, 14));
}
