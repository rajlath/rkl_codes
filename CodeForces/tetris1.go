package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewScanner(os.Stdin)

func nextInt() int {
	in.Scan()
	r := 0
	for _, c := range in.Bytes() {
		r *= 10
		r += int(c - '0')
	}
	return r
}

func main() {
	in.Split(bufio.ScanWords)
	n, k, c, r, s := nextInt(), nextInt(), 0, 0, 0
	a, t := make([]int, n), make([]int, n)
	for i := range a {
		a[i] = nextInt()
	}
	for i := range a {
		t[i] = nextInt()
		if t[i] == 0 {
			c += a[i]
		} else {
			s += a[i]
		}
		if i >= k && t[i-k] == 0 {
			c -= a[i-k]
		}
		if r < c {
			r = c
		}
	}
	fmt.Println(r + s)
}