#63
// Magic.go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	allMagics := map[int]bool{}
	for x := 1; x < 10001; x += 1 {
		if is_Magic(strconv.Itoa(x)) {
			allMagics[x] = true
		}
	}
	file, _ := os.Open(os.Args[1])
	scans := bufio.NewScanner(file)
	for scans.Scan() {
		input := strings.Fields(strings.TrimSpace(scans.Text()))

		a, b := input[0], input[1]
		bi, _ := strconv.Atoi(b)
		ai, _ := strconv.Atoi(a)
		allvalids := make([]string, 0)
		for x := ai; x < bi; x += 1 {
			if allMagics[x] == true {
				allvalids = append(allvalids, strconv.Itoa(x))
			}
		}

		if len(allvalids) > 0 {
			fmt.Println(strings.Join(allvalids, " "))
		} else {
			fmt.Println("-1")
		}
	}

}
func is_Magic(st string) bool {
	l := len(st)
	if l != len(removeDuplicates(st)) {
		return false
	}
	visited := map[string]string{}
	a, b := st[:1], st[:1]
	j := 0
	flag := 1
	for flag > 0 {
		if _, ok := visited[b]; !ok {

			visited[b] = b
			bint, _ := strconv.Atoi(b)
			j = (bint + j) % l
			b = string(st[j])
		} else {
			break
		}

	}

	if a == b && len(visited) == l {
		return true
	}
	return false

}

func removeDuplicates(a string) string {
	result := ""
	seen := map[rune]rune{}
	for _, val := range a {
		if _, ok := seen[val]; !ok {
			result += string(val)
			seen[val] = val
		}
	}
	return result
}
