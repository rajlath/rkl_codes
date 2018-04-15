/*
2
ab
abab
ab
aabb
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var scanner *bufio.Scanner

func main() {
	scanner = bufio.NewScanner(os.Stdin)
	ins := readInt()
	for i := 0; i < ins; i += 1 {
		pattern := readString()
		target := readString()
		s := target
		r := strings.NewReplacer(pattern, "")

		for {
			target1 := r.Replace(target)
			if len(target1) == len(target) {
				break
			} else {
				target = target1
			}

		}

		if len(target) == 0 {
			fmt.Println(len(s) / 2)
		} else {
			fmt.Println((len(s) - len(target)) / len(pattern))

		}

	}

}

func readString() string {
	scanner.Scan()
	return scanner.Text()
}

func readInt() int {
	val, _ := strconv.Atoi(readString())
	return val
}
