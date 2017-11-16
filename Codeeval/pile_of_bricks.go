#65
package main

import (
	"bufio"
	"fmt"

	"os"
	"sort"
	"strings"
)

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func main() {
	file, _ := os.Open(os.Args[1])
	scans := bufio.NewScanner(file)
	for scans.Scan() {
		ins := strings.Split(scans.Text(), "|")
		br := strings.Split(ins[1], ";")
		h, h1, h2 := make([]int, 2), make([]int, 2), make([]int, 2)
		fmt.Sscanf(ins[0], "[%d,%d] [%d,%d]", &h1[0], &h1[1], &h2[0], &h2[1])
		h[0], h[1] = abs(h1[0]-h2[0]), abs(h1[1]-h2[1])
		sort.Ints(h)
		b, b1, b2 := make([]int, 3), make([]int, 3), make([]int, 3)
		var r []int
		for _, i := range br {
			var j int
			fmt.Sscanf(i, "(%d [%d,%d,%d] [%d,%d,%d])", &j, &b1[0], &b1[1], &b1[2], &b2[0], &b2[1], &b2[2])
			b[0], b[1], b[2] = abs(b1[0]-b2[0]), abs(b1[1]-b2[1]), abs(b1[2]-b2[2])
			sort.Ints(b)
			if b[0] <= h[0] && b[1] <= h[1] {
				r = append(r, j)
			}
		}
		if len(r) > 0 {
			sort.Ints(r)
			var r2 []string
			for _, i := range r {
				r2 = append(r2, fmt.Sprint(i))
			}
			fmt.Println(strings.Join(r2, ","))
			continue

		}

		fmt.Println("-")

	}
}
