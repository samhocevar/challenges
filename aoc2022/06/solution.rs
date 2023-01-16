use std::fs;
use std::iter::zip;
use multiset::HashMultiSet;

fn parse(s: &String, n: usize) -> usize {
    let mut stats: HashMultiSet<char> = HashMultiSet::new();
    let mut front = s.chars().into_iter();
    let back = s.chars().into_iter();

    // Initialise multiset with n-1 elements
    (&mut front).take(n - 1).for_each(|ch| stats.insert(ch));

    // Slide our window of width n and stop when all elements are distinct
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
