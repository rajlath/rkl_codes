package main

import "fmt"

func intMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n int
	fmt.Scan(&n)

	for c := 0; c < n; c++ {
		var m int
		fmt.Scan(&m)
		points := make([]int, m)
		best_here := 0
		best_alls := 0
		for i := 0; i < m; i++ {
			fmt.Scan(&points[i])
			best_here += points[i]
			if best_here < 0 {
				best_here = 0
			}
			best_alls = intMax(best_alls, best_here)
		}
		fmt.Println(best_alls)
	}

}
