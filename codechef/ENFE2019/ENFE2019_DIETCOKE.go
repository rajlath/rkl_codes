package main

import (
	"fmt"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var nbTest, a, b int
	fmt.Scan(&nbTest)
	for nbTest > 0 {
		fmt.Scan(&a, &b)
		fmt.Println(a + b - gcd(a, b))
		nbTest--
	}

}
