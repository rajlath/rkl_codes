package main

import "fmt"

func main() {
	var n, m, p, a1, a2, b1,b2 int
	fmt.Scan(&n)
	a := [n][n]int{}
	fmt.Scan(&m)
	for i := 0; i < n; i++ {
		fmt.Scan(&p)
		fmt.Scan(&a1)
		fmt.Scan(&a2)
		fmt.Scan(&b1)
		fmt.Scan(&b2)
		for x:=a1; x<b1; x+=1{
			for y:=a2; y<b2; y+=1{
				a[x][y] ^= p
			}
		}
	}

	for i := range a {
        fmt.Printf("%v\n", i)

    }
}