package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scanner *bufio.Scanner

func may_be(arr []int64, np, qty int64) int64 {
	hours := int64(0)
	for i := int64(0); i < np; i++ {
		hrs := arr[i] / qty
		if arr[i]%qty == 0 {
			hours += hrs
		} else {
			hours += hrs + 1
		}
	}
	return hours
}

func readInt64Array(n int64) []int64 {
	res := make([]int64, n)
	for i := int64(0); i < n; i++ {
		res[i] = readInt64()
	}
	return res
}
func readInt64() int64 {
	v, _ := strconv.ParseInt(readString(), 10, 64)
	return v
}
func readString() string {
	scanner.Scan()
	return scanner.Text()
}

func main() {
	scanner = bufio.NewScanner(os.Stdin)
	test_cnt := readInt64()
	for i := int64(0); i < test_cnt; i += 1 {
		nh := readInt64Array(2)
		fmt.Println(nh)
		arr := readInt64Array(3)
		fmt.Println(arr)

	}

}
