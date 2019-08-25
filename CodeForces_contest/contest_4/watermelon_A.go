package main

import (
	"bufio"
	"fmt"
	"os"
)

//execution time 63 ms
/*
func main() {
	var n int
	fmt.Scan(&n)
	ans := "NO"
	if n > 2 && n%2 == 0 {
		ans = "YES"
	}
	fmt.Print(ans)
}
*/

// using bufio

func main() {
	var given int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d\n", &given)
	answer := "NO"
	if given > 2 && given%2 == 0 {
		answer = "YES"
	}
	fmt.Print(answer)

}

// execution time 92ms
