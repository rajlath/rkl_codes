package main

import "fmt"

func main() {
	var n int
	cannot := "cannot distribute"
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		A, B := 0, 0
		fmt.Scan(&A)
		fmt.Scan(&B)
		if B == 0 {
			fmt.Println(cannot)
		} else {
			ans := A / B
			if ans > 0 {
				fmt.Println(ans)
			} else {
				fmt.Println(cannot)
			}
		}
	}
}
