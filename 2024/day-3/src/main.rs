use regex::Regex;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part-1 Answer: {}", part_1());
    println!("Part-2 Answer: {}", part_2());
}

fn part_1() -> i32 {
    let file: File = File::open("input.txt").expect("Failed to open file");
    let reader: BufReader<File> = BufReader::new(file);
    let mut input: String = String::new();

    for line in reader.lines() {
        input.push_str(&line.unwrap());
    }

    // regex for pattern: mul (1-3 digit number, 1-3 digit number) with named groups
    let re = Regex::new(r"mul\((?<num1>\b\d{1,3}\b),(?<num2>\b\d{1,3}\b)\)").unwrap();
    let mut result: i32 = 0;
    for mt in re.captures_iter(&input) {
        result += &mt["num1"].parse::<i32>().expect("Failed to parse number")
            * &mt["num2"].parse::<i32>().expect("Failed to parse number");
    }
    return result;
}

fn part_2() -> i32 {
    let file: File = File::open("input.txt").expect("Failed to open file");
    let reader: BufReader<File> = BufReader::new(file);
    let mut input: String = String::new();

    // multi line concat
    for line in reader.lines() {
        input.push_str(&line.unwrap());
    }

    let mut should_perform: bool = true;
    let re = Regex::new(
        r"mul\((?<num1>\b\d{1,3}\b),(?<num2>\b\d{1,3}\b)\)|(((?<yes>do\(\))|(?<no>don't\(\))))",
    )
    .unwrap();

    let mut result: i32 = 0;
    for mt in re.captures_iter(&input) {
        if mt.name("yes").is_some() {
            should_perform = true;
            continue;
        }
        if mt.name("no").is_some() {
            should_perform = false;
            continue;
        }
        if should_perform {
            result += &mt["num1"].parse::<i32>().expect("Failed to parse number")
                * &mt["num2"].parse::<i32>().expect("Failed to parse number");
        }
    }
    return result;
}
