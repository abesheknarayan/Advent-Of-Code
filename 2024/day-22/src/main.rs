use std::cmp;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Answers: {:?}", solve());
}

fn solve() -> (i64, i32) {
    let reader = file_reader("input.txt");

    let mut count: Vec<HashMap<(i32, i32, i32, i32), i32>> = Vec::new();

    let mut part_1_result: i64 = 0;
    let mut part_2_result: i32 = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let mut num: i64 = line.parse().expect("Failed to parse line");
        let mut diff: Vec<i32> = Vec::new();
        let mut temp_count: HashMap<(i32, i32, i32, i32), i32> = HashMap::new();
        for j in 0..2000 {
            let temp: i64 = do_op(num);
            if j > 0 {
                diff.push((temp as i32 % 10) - (num as i32 % 10));
            }
            if j >= 4 {
                let diff_tuple: (i32, i32, i32, i32) =
                    (diff[j - 4], diff[j - 3], diff[j - 2], diff[j - 1]);
                if temp_count.get(&diff_tuple).is_none() {
                    temp_count.insert(diff_tuple, temp as i32 % 10);
                }
            }
            num = temp;
        }
        count.push(temp_count);
        part_1_result += num;
    }

    let mut distinct_tuples: HashSet<(i32, i32, i32, i32)> = HashSet::new();

    for cmap in count.iter() {
        for k in cmap.keys() {
            distinct_tuples.insert(*k);
        }
    }

    for tuple in distinct_tuples.iter() {
        let mut temp_result: i32 = 0;
        for cmap in count.iter() {
            if cmap.get(tuple).is_none() {
                continue;
            }
            temp_result += *cmap.get(tuple).expect("expected value for key");
        }
        part_2_result = cmp::max(part_2_result, temp_result);
    }

    return (part_1_result, part_2_result);
}

fn do_op(num: i64) -> i64 {
    let modulo: i64 = 16777216;

    let mut temp: i64 = num * 64;
    temp = temp ^ num;
    temp %= modulo;

    let temp2: f64 = temp as f64 / 32 as f64;
    let mut temp3: i64 = temp2.floor() as i64;
    temp = temp ^ temp3;
    temp %= modulo;

    temp3 = temp * 2048;
    temp = temp ^ temp3;
    temp %= modulo;

    return temp;
}

fn file_reader(file: &str) -> BufReader<File> {
    let file: File = File::open(file).expect("Failed to open file");
    return BufReader::new(file);
}
