use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    part_1();

    part_2();
}

fn part_1() {
    let file: File = File::open("input.txt").expect("Failed to open file");
    let reader: BufReader<File> = BufReader::new(file);
    let mut result: i32 = 0;

    // reading a file line by line with 2 numbers in each line
    for line in reader.lines() {
        let line = line.unwrap();
        let vec: Vec<i32> = line
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Failed to parse number"))
            .collect();

        result += if is_safe(&vec) { 1 } else { 0 };
    }

    println!("Part-1 Result : {result}");
}

fn part_2() {
    let file: File = File::open("input.txt").expect("Failed to open file");
    let reader: BufReader<File> = BufReader::new(file);
    let mut result: i32 = 0;

    for line in reader.lines() {
        let line: String = line.unwrap();
        let vec: Vec<i32> = line
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Failed to parse number"))
            .collect();

        let safe: bool = is_safe(&vec);
        if !safe {
            for i in 0..vec.len() {
                let mut new_vec: Vec<i32> = vec.clone();
                new_vec.remove(i);

                if is_safe(&new_vec) {
                    result += 1;
                    break;
                }
            }
        } else {
            result += 1;
        }
    }

    println!("Part-2 Result : {result}");
}

fn is_safe(vec: &Vec<i32>) -> bool {
    let mut safe: bool = true;
    safe &= vec
        .windows(2)
        .all(|w| (w[0] - w[1]).abs() > 0 && (w[0] - w[1]).abs() < 4);

    safe &= is_sorted_ascending(&vec) || is_sorted_descending(&vec);

    return safe;
}

fn is_sorted_ascending<T: Ord>(list: &[T]) -> bool {
    return list.windows(2).all(|w| w[0] <= w[1]);
}

fn is_sorted_descending<T: Ord>(list: &[T]) -> bool {
    return list.windows(2).all(|w| w[0] >= w[1]);
}
