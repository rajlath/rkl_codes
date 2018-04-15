package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var local = false
var scanner *bufio.Scanner

func main() {
	setup()
	n := readInt()
	a, b := 1, 1
	for i := 1; i < n+1; i += 1 {
		for i > b {
			a, b = b, a+b
		}
		if b == i {
			fmt.Print("O")
		} else {
			fmt.Print("o")
		}

	}

}

func setup() {
	source := os.Stdin
	if local == true {
		file, _ := os.Open("input.txt")
		source = file
	}
	scanner = bufio.NewScanner(source)
	scanner.Split(bufio.ScanWords)
}

func readString() string {
	scanner.Scan()
	ans := scanner.Text()
	return ans
}

func readInt() int {
	scanner.Scan()
	ans, _ := strconv.ParseInt(scanner.Text(), 10, 0)
	return int(ans)
}
