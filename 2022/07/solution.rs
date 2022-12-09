
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, BufRead, Result};

fn main() -> Result<()> {
    let fd = File::open("input.txt")?;
    let mut cwd: Vec<String> = Vec::new();

    let mut sizes: HashMap<Vec<String>, i64> = HashMap::new();
    sizes.insert(vec![], 0);

    let br = BufReader::new(fd);
    for l in br.lines() {
        let s = l.unwrap();
        let mut tokens = s.split(' ');
        match tokens.next() {
            Some("$") => {
                tokens.next();
                let directory = tokens.next();
                match directory {
                    Some("/")  => { cwd.clear(); },
                    Some("..") => { cwd.pop(); },
                    Some(d)    => { cwd.push(d.to_string()); },
                    None       => {}, // Not a "cd" command, ignore
                }
            },
            Some(entry) => {
                if entry.chars().nth(0).unwrap() == 'd' {
                    // New directory found! Add it to our sizes map
                    let name = tokens.next().unwrap();
                    let mut key = cwd.clone();
                    key.push(name.to_string());
                    sizes.insert(key, 0);
                } else {
                    // New file found! Add its size to cwd and all parent directories
                    let size = entry.parse::<i64>().unwrap();
                    let mut key = cwd.clone();
                    loop {
                        *sizes.get_mut(&key).unwrap() += size;
                        if key.len() == 0 {
                            break;
                        }
                        key.pop();
                    }
                }
            },
            None => {},
        }
    }

    let excess = sizes[&vec![]] - (70000000 - 30000000);

    println!("{}", sizes.values().filter(|&x| *x <= 100000).sum::<i64>());
    println!("{}", sizes.values().filter(|&x| *x >= excess).min().unwrap());

    Ok(())
}
