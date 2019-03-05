use std::io;

fn get_line() -> String {
    let mut res = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut res);
    res
}

fn get_int() -> i32 {
    get_line().trim().parse().unwrap()
}

fn main(){
    let nb_test = get_int();
    for i in  0..nb_test{
        let mut current = get_int();
        current %= 6;
        if (current == 0) || (current == 1){
            println!("B")
        }else{
            println!("A")
        }
    }

}