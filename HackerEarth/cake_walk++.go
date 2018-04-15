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
	case_cnt := readInt()
	for i := 0; i < case_cnt; i++ {
		students := readInt()
		updates := readInt()
		scores := make([]int, students, students*2)
		for j := 0; j < students; j++ {
			scores[j] = readInt()
		}
		flag := 0
		for j := 1; j < students; j++ {
			if scores[j] != scores[j-1] {
				flag = 1
			}
		}
		for j := 0; j < updates; j++ {
			x := readInt()
			y := readInt()
			if flag == 0 {
				fmt.Println(0)
				continue
			}

			if scores[0] == x {
				scores[0] = y
			}
			sums := 0
			for j := 0; j < students; j++ {
				if scores[j] == x {
					scores[j] = y
				}
				sums += 2 * (abs(scores[i] - scores[i-1]))
			}
			fmt.Println(sums / 2)

		}
	}
}

func abs(a int) int {
	if a < 0 {
		return 0 - a
	}
	return a
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
