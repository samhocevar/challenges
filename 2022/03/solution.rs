use itertools::Itertools;
use std::collections::HashSet;
use std::fs::File;
use std::io::{prelude::*, BufReader, Result};

// Compute score for all chars in a collection (in our case there will only be one value)
fn score<T>(coll: T) -> i32
    where T: IntoIterator<Item = char> {
    coll.into_iter()
        .map(|c| (c as i32 - 38) % 58) // -38 = 27-'A'   58 = 'a'-'A'+26
        .sum()
}

// Return chars that appear in every string of collection
fn common_chars<T>(coll: T) -> HashSet<char>
    where T: IntoIterator<Item = String> {
    coll.into_iter()
        .map(|s| -> HashSet<char> { HashSet::from_iter(s.chars()) })
        .reduce(|a, b| &a & &b)
        .unwrap()
}

fn main() -> Result<()> {
    let fd = File::open("input.txt")?;
    let br = BufReader::new(fd);

    let (mut s1, mut s2) = (0, 0);

    for tu in &br.lines().chunks(3) {
        // Trim lines and put them in a vector
        let v: Vec<String> = tu.into_iter()
                               .map(Result::unwrap)
                               .map(|s| str::trim_end(&s).to_owned())
                               .collect();

        // Score for problem 1
        for s in &v {
            let (a, b) = s.split_at(s.len() / 2);
            s1 += score(common_chars(vec![a.to_owned(), b.to_owned()]));
        }

        // Score for problem 2
        s2 += score(common_chars(v));
    }

    print!("{}\n{}\n", s1, s2);

    Ok(())
}
