use std::fs;
use multiset::HashMultiSet;

fn parse(s: &String, n: usize) -> usize {
    let mut stats: HashMultiSet<char> = HashMultiSet::new();
    let chars: Vec<char> = s.chars().collect();

    for i in 0..chars.len() {
        stats.insert(chars[i]);
        if i >= n { stats.remove(&chars[i - n]); }
        if stats.distinct_elements().count() == n { return i + 1; }
    }
    0
}

fn main() {
    let s: String = fs::read_to_string("input.txt").unwrap();

    println!("{}", parse(&s, 4));
    println!("{}", parse(&s, 14));
}
