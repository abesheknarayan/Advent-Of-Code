use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file: File = File::open("input2.txt").expect("Failed to open file");
    let reader: BufReader<File> = BufReader::new(file);

    let mut first_list: Vec<i32> = Vec::new();
    let mut second_list: Vec<i32> = Vec::new();
    
    // reading a file line by line with 2 numbers in each line
    for line in reader.lines() {
        let line = line.unwrap();
        let words: Vec<&str> = line.trim().split_whitespace().collect();
        let num1: i32 = words[0].parse().expect("Failed to read first number");
        let num2: i32 = words[1].parse().expect("Failed to read second number");
        first_list.push(num1);
        second_list.push(num2);
    }

    // part_1(&mut first_list, &mut second_list);

    part_2(&mut first_list, &mut second_list);

}

fn part_1(first_list: &mut Vec<i32>, second_list: &mut Vec<i32>) {
        // sort both list
        first_list.sort();
        second_list.sort();
    
        let mut result: i32 = 0;
    
        for (x,y) in first_list.iter().zip(second_list.iter()) {
            result += (x-y).abs();
        }
    
        println!("Result: {result}");   
}

fn part_2(first_list: &mut Vec<i32>, second_list: &mut Vec<i32>) {
    // Hashmap to keep the count from second_list
    let mut counts: HashMap<i32,i32> = HashMap::new();
    for x in second_list {
        *counts.entry(*x).or_insert(0) += 1;
    }

    let mut result: i64 = 0;

    for x in first_list {
        let num: i32 = *x;
        let count: i32 = *counts.entry(num).or_default();
        result += (num as i64 * count as i64);
    }

    println!("Result: {result}");
}