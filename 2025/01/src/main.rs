use std::io::{self, BufRead, BufReader};
use std::fs::File;

fn read_lines(path: &str) -> io::Result<Vec<String>> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);

    reader.lines().collect()
}

fn wrap_0_99(value: i32) -> i32 {
    ((value % 100) + 100) % 100
}


fn main() -> io::Result<()> {
    // read input file by args
    let contents = read_lines("input.txt")?;

    let mut dail_state = 50;

    // Each time we hit zero, we increase this variable.
    let mut rule_counter = 0;

    for element in contents {

        println!("Next combination is: {}", element);

        let direction = element.chars().nth(0);
        
        let mut value: i32 = element[1..].parse().expect("invalid number");

        println!("Looping: {}", value);
        while value >= 0 {
            if direction == Some('L') {
                dail_state -= 1;
                dail_state = wrap_0_99(dail_state);
            } else {
                dail_state += 1;
                dail_state = wrap_0_99(dail_state);
            }

            if dail_state == 0 {
                rule_counter += 1;
            }

            value -= 1;
        }
    }

    println!("Rule Counter ended at {}", rule_counter);
    
    Ok(())
} 