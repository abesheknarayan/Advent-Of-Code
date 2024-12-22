use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part-1 Answer: {}", part_1());
    println!("Part-2 Answer: {}", part_2());
}

fn part_1() -> i64 {
    let reader = file_reader("input.txt");

    let mut res: i64 = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let mut split: std::str::Split<'_, &str> = line.trim().split(":");
        let left_hand_side: i64 = split
            .next()
            .unwrap()
            .parse()
            .expect("Failed to read left hand side");
        let right_hand_side: Vec<i32> = split
            .next()
            .unwrap()
            .split_whitespace()
            .filter_map(|c| c.parse().ok())
            .collect();

        if perform_brute_force(left_hand_side, &right_hand_side) {
            res += left_hand_side;
        }
    }
    return res;
}

fn part_2() -> i64 {
    let reader = file_reader("input.txt");

    let mut res: i64 = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let mut split: std::str::Split<'_, &str> = line.trim().split(":");
        let left_hand_side: i64 = split
            .next()
            .unwrap()
            .parse()
            .expect("Failed to read left hand side");
        let right_hand_side: Vec<i32> = split
            .next()
            .unwrap()
            .split_whitespace()
            .filter_map(|c| c.parse().ok())
            .collect();

        if perform_brute_force_2(left_hand_side, &right_hand_side) {
            res += left_hand_side;
        }
    }

    return res;
}

fn perform_brute_force_2(left: i64, right: &Vec<i32>) -> bool {
    let exp: u32 = right.len() as u32;
    let base = 3 as i64;
    for i in 0..base.pow(exp - 1) {
        let base3: String = write_number_in_base3(i, (right.len() - 1) as usize);
        let mut temp_res: i64 = right[0] as i64;
        for j in 0..right.len() - 1 {
            let op = base3.chars().nth(j).expect("something wrong");
            if op == '0' {
                temp_res = temp_res + right[j + 1] as i64;
            } else if op == '1' {
                temp_res = temp_res * right[j + 1] as i64
            } else {
                temp_res = (temp_res.to_string() + &right[j + 1].to_string())
                    .parse()
                    .expect("something is wrong");
            }
        }

        if temp_res == left {
            return true;
        }
    }

    return false;
}

fn perform_brute_force(left: i64, right: &Vec<i32>) -> bool {
    let len = right.len();
    for i in 0..1 << (len - 1) {
        let mut temp_res: i64 = right[0] as i64;
        for j in 0..len - 1 {
            if i & (1 << j) != 0 {
                temp_res = temp_res + (right[j + 1] as i64);
            } else {
                temp_res = temp_res * (right[j + 1] as i64);
            }
        }

        if temp_res == left {
            return true;
        }
    }

    return false;
}

fn write_number_in_base3(mut num: i64, len: usize) -> String {
    let mut res: String = String::new();
    while num != 0 {
        let remainder = num % 3;
        res.push(char::from_digit(remainder as u32, 3).unwrap());
        num /= 3;
    }
    res = res.chars().rev().collect();
    // add padding for len digits
    return format!("{:0>width$}", res, width = len);
}

fn file_reader(file: &str) -> BufReader<File> {
    let file: File = File::open(file).expect("Failed to open file");
    return BufReader::new(file);
}
