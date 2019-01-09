package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)

func init() {
	scanner.Split(bufio.ScanWords)
}

func scanString() string {
	scanner.Scan()
	return scanner.Text()
}

func scanInt64() int64 {
	scanner.Scan()
	v, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	return v
}

func scanInt() int {
	scanner.Scan()
	v, _ := strconv.Atoi(scanner.Text())
	return v
}

func scanInts(n int) []int {
	l := make([]int, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		l[i], _ = strconv.Atoi(scanner.Text())
	}

	return l
}

func scanInts64(n int64) []int64 {
	l := make([]int64, n)
	for i := int64(0); i < n; i++ {
		scanner.Scan()
		l[i], _ = strconv.ParseInt(scanner.Text(), 10, 64)
	}

	return l
}

func scanBool() bool {
	scanner.Scan()
	v, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	return v == 1
}

func scanBools(n int64) []bool {
	l := make([]bool, n)
	for i := int64(0); i < n; i++ {
		scanner.Scan()
		v, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		l[i] = v == 1
	}

	return l
}

func main() {
	n := scanInt()

	m := [100000]int{}

	for i := 0; i < n; i++ {
		r := scanInt()
		for j := 0; j < r; j++ {
			num := scanInt()
			m[num]++
		}
	}

	for i := 1; i < len(m); i++ {
		if m[i] == n {
			fmt.Printf("%d ", i)
		}
	}
}

func abs(a int64) int64 {
	if a >= 0 {
		return a
	}

	return -a
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}

	return b
}
