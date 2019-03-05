package main

import "fmt"

var limit = 100006

func primes_counts() []int {
	limit = limit + 1
	primes := make([]bool, limit)
	// implies up to the sqrt of limit
	for k := 2; k*k <= limit; k++ {
		if primes[k] != true {
			for ix := k * k; ix < limit; ix += k {
				primes[ix] = true
			}
		}
	}

	count := 0
	counts := make([]int, limit)
	for ix := 2; ix < limit-6; ix++ {
		if primes[ix] != true && primes[ix+6] != true {
			count = count + 1
		}
		counts[ix] = count

	}
	return counts
}
func main() {
	var nbTest, current int
	counts := primes_counts()
	fmt.Scan(&nbTest)
	for nbTest > 0 {
		fmt.Scan(&current)
		fmt.Println(counts[current])
		nbTest--
	}

}
