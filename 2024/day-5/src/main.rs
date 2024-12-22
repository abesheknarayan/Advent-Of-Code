use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::vec;

fn main() {
    println!("Part-1: {}", part_1());
}

fn part_1() -> i32 {
    let reader = file_reader("input.txt");

    let mut res: i32 = 0;

    let mut is_graph_over: bool = false;

    let mut adjaceny_graph: HashMap<i32, Vec<i32>> = HashMap::new();
    let mut indegree: HashMap<i32, i32> = HashMap::new();
    let mut nodes: HashSet<i32> = HashSet::new();
    let mut page_ordering: Vec<Vec<i32>> = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap();
        if line.is_empty() {
            is_graph_over = true;
            continue;
        }
        if !is_graph_over {
            let inp: Vec<&str> = line.split("|").collect();
            let x: i32 = inp[0].parse().expect("error in parsing");
            let y: i32 = inp[1].parse().expect("error in parsing");
            // println!("{} before {}", x, y);
            adjaceny_graph.entry(x).or_insert(vec![]).push(y);
            nodes.insert(x);
            nodes.insert(y);
            let indegree_for_y = indegree.entry(y).or_insert(0);
            *indegree_for_y += 1;
        } else {
            let inp: Vec<i32> = line
                .split(",")
                .map(|c| c.parse().expect("error in parsing"))
                .collect();
            page_ordering.push(inp);
        }
    }

    let mut queue: VecDeque<i32> = VecDeque::new();
    for node in nodes.iter(){ 
        // basically indegree is zero. Should be added to the queue.
        if indegree.get(&node).is_none() {
            indegree.insert(*node, 0);
            queue.push_back(*node);
        }
    }

    let mut order: Vec<i32> = Vec::new();

    while !queue.is_empty() {
        let mut node: i32 = queue.pop_front().expect("Queue is empty");
        order.push(node);
        for neighbour in adjaceny_graph.entry(node).or_default() {
            let indegree_for_node = indegree.entry(*neighbour).or_default();
            *indegree_for_node -=1;
            if *indegree_for_node == 0 {
                queue.push_back(*neighbour);
            }
        }
    }

    println!("Nodes: {:?}", nodes);
    println!("Nodes: {}", nodes.len());
    println!("Order: {:?}", order);
    println!("Queue: {:?}", queue);
    println!("Indegree: {:?}", indegree);


    let mut indexing: HashMap<i32, i32> = HashMap::new();

    for (i, v) in order.iter().enumerate() {
        indexing.insert(*v, i as i32);
    }

    for page in page_ordering.iter() {
        let mut new_index: Vec<i32> = Vec::new();
        let mut is_valid: bool = true;
        for x in page.iter() {
            if indexing.get(x).is_none() {
                println!("Cannot find element: {}", x);
                is_valid = false;
                break;
            }
            new_index.push(*indexing.get(x).expect("Error in getting index"));
        }

        if is_valid && is_sorted_ascending(&new_index) {
            let middle_index: i32  = (page.len() as i32  - 1 )/2;
            res += page[middle_index as usize];
        }
    }

    return res;
}

fn part_2() -> i32 {
    let mut res: i32 = 0;

    return res;
}

fn is_sorted_ascending<T: Ord>(list: &[T]) -> bool {
    return list.windows(2).all(|w| w[0] <= w[1]);
}

fn file_reader(file: &str) -> BufReader<File> {
    let file: File = File::open(file).expect("Failed to open file");
    return BufReader::new(file);
}

