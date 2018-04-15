package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var local = false
var scanner *bufio.Scanner

func main() {
	setup()
	noc := readInt()
	doors := ""
	for i := 0; i < noc; i++ {
		doors += strconv.Itoa(readInt())

	}
	fmt.Printf("%d %d\n",strings.Count(doors, "1")-strings.Count(doors, "11"), strings.Count(doors, "1"))

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

func readIntArr(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = readInt()
	}
	return arr
}
