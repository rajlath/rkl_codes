package main

import (
	"fmt"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	var caseno, students, updates, x, y, sums int
	fmt.Scan(&caseno)
	for i := 0; i < caseno; i++ {
		fmt.Printf("Case %d:", caseno)
		fmt.Println()
		fmt.Scan(&students)
		fmt.Scan(&updates)
		flag := 0
		scores := make([]int, students+1)
		fmt.Scan(&scores[0])
		for j := 1; j < students; j++ {
			fmt.Scan(&scores[j])
			if scores[j] != scores[j-1] {
				flag = 1
			}
		}
		for j := 0; j < updates; j++ {
			fmt.Scan(&x)
			fmt.Scan(&y)
			if flag == 0 {
				fmt.Println(0)
			}
			if scores[0] == x {
				scores[0] = y
			}
			sums = 0
			for a := 1; a < students; a++ {
				if scores[a] == x {
					scores[a] = y
				}
				sums += 2 * (abs(scores[a] - scores[a-1]))
			}
			fmt.Println(int(sums / 2))
		}

	}

}
