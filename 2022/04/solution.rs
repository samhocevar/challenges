use std::fs::File;
use std::io::{prelude::*, BufReader, Result};

fn main() -> Result<()> {
    let fd = File::open("input.txt")?;
    let br = BufReader::new(fd);

    let (mut o1, mut o2) = (0, 0);

    for l in br.lines() {
        let v: Vec<i64> = l.unwrap()
                           .trim()
                           .split(&['-', ','][..])
                           .map(|s| s.parse().unwrap())
                           .collect();
        o1 += ((v[0]-v[2]) * (v[1]-v[3]) <= 0) as i64;
        o2 += (v[1] >= v[2] && v[3] >= v[0]) as i64;
    }

    print!("{}\n{}\n", o1, o2);

    Ok(())
}
