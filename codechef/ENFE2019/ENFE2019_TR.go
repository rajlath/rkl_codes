fn main() {
	let mut input = format!("");
	std::io::stdin().read_line(&mut input).ok();
	let v: Vec<i16> = input
		.trim()
		.split_whitespace()
		.map(|x| x.parse().expect(""))
		.collect();
	if v[0] - 1 <= v[1] {
		println!("{}", v[0] - 1);
		std::process::exit(0);
	}
	let mut money_to_spent = v[1];
	let mut fuel = v[1];
	for i in 1..v[0] {
		if i != 1 {
			fuel = fuel - 1;
		}
		//println!("CITY: {} F: {} SISA: {}", i, fuel, v[0] - i);
		// 1 2 3 4 5 6 7 8 9
		//   2
		if v[0] - i <= fuel {
			break;
		}
		if i != 1 {
			money_to_spent = money_to_spent + i;
			fuel = fuel + 1;
		}
	}
	println!("{}", money_to_spent);
}
