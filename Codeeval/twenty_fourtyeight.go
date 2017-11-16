#65
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func slide(a []int) []int {
	lastNum, lastNumId, lastZero := -1, -1, -1
	for i := 0; i < len(a); i++ {
		if a[i] == 0 {
			if lastZero == -1 {
				lastZero = i
			}
		} else {
			if lastNum == a[i] {
				a[lastNumId] = 2 * lastNum
				lastNum = -1
				a[i] = 0
				if lastZero == -1 {
					lastZero = i
				}
			} else {
				lastNum = a[i]
				if lastZero == -1 {
					lastNumId = i
				} else {
					lastNumId = lastZero
					a[lastZero] = a[i]
					a[i] = 0
					lastZero++
				}
			}
		}
	}
	return a
}

func main() {
	data, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer data.Close()
	scanner := bufio.NewScanner(data)
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), ";")
		t := strings.Split(s[2], "|")
		var n int
		fmt.Sscan(s[1], &n)
		m := make([][]int, n)
		for i := 0; i < n; i++ {
			u := strings.Fields(t[i])
			m[i] = make([]int, n)
			for j := 0; j < n; j++ {
				fmt.Sscan(u[j], &m[i][j])
			}
		}

		l := make([]int, n)
		for i := 0; i < n; i++ {
			switch s[0] {
			case "LEFT":
				copy(l, m[i])
				l = slide(l)
				copy(m[i], l)
			case "RIGHT":
				for j := 0; j < n; j++ {
					l[j] = m[i][n-1-j]
				}
				l = slide(l)
				for j := 0; j < n; j++ {
					m[i][n-1-j] = l[j]
				}
			case "UP":
				for j := 0; j < n; j++ {
					l[j] = m[j][i]
				}
				l = slide(l)
				for j := 0; j < n; j++ {
					m[j][i] = l[j]
				}
			case "DOWN":
				for j := 0; j < n; j++ {
					l[j] = m[n-1-j][i]
				}
				l = slide(l)
				for j := 0; j < n; j++ {
					m[n-1-j][i] = l[j]
				}
			}
		}

		r := make([]string, n)
		for i := 0; i < n; i++ {
			u := make([]string, n)
			for j := 0; j < n; j++ {
				u[j] = fmt.Sprint(m[i][j])
			}
			r[i] = strings.Join(u, " ")
		}
		fmt.Println(strings.Join(r, "|"))
	}
}
