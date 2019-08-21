package main

import (
	"fmt"
)

func main() {
	var (
		given  int
		left   int
		rite   int
		maxs   int
		mins   int
		powers uint
	)
	fmt.Scanf("%d %d %d", &given, &left, &rite)

	powers = 0
	for i := 0; i < left; i++ {
		mins += 1 << powers
		powers++
	}
	mins += given - left

	powers = 0
	for i := 0; i < rite; i++ {
		maxs += 1 << powers
		powers++
	}
	maxs += (given - rite) * (1 << (powers - 1))
	fmt.Printf("%d %d", mins, maxs)

}
