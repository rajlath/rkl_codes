package main

import (
	"bufio"
	"fmt"
	"os"
)

var in = bufio.NewScanner(os.Stdin)

func readInt() int64 {
	if !in.Scan() {
		panic(in.Err())
	}
	res := int64(0)
	mul := int64(1)
	for _, b := range in.Bytes() {
		if b == '-' {
			mul *= -1
			continue
		}
		res = res*10 + int64(b-'0')
	}
	return mul * res
}

func readString() string {
	if !in.Scan() {
		panic(in.Err())
	}
	return in.Text()
}

func main() {
	in.Split(bufio.ScanWords)

	n := readInt()
	var lastG, ans int64
	var r, b []int64
	for i := int64(0); i < n; i++ {
		p := readInt()
		switch readString() {
		case "G":
			if lastG == 0 {
				if len(r) > 0 {
					ans += p - r[0]
				}
				if len(b) > 0 {
					ans += p - b[0]
				}
			} else {
				ans += p - lastG
				maxAns := ans + p - lastG
				if len(r) > 0 {
					ma := r[0] - lastG
					for i := range r[1:] {
						if cur := r[i+1] - r[i]; ma < cur {
							ma = cur
						}
					}
					if cur := p - r[len(r)-1]; ma < cur {
						ma = cur
					}
					ans += p - lastG - ma
				}
				if len(b) > 0 {
					ma := b[0] - lastG
					for i := range b[1:] {
						if cur := b[i+1] - b[i]; ma < cur {
							ma = cur
						}
					}
					if cur := p - b[len(b)-1]; ma < cur {
						ma = cur
					}
					ans += p - lastG - ma
				}
				if ans > maxAns {
					ans = maxAns
				}
			}
			lastG = p
			r = r[:0]
			b = b[:0]
		case "R":
			r = append(r, p)
		case "B":
			b = append(b, p)
		default:
			panic("rgb")
		}
	}
	if len(r) > 0 {
		if lastG == 0 {
			ans += r[len(r)-1] - r[0]
		} else {
			ans += r[len(r)-1] - lastG
		}
	}
	if len(b) > 0 {
		if lastG == 0 {
			ans += b[len(b)-1] - b[0]
		} else {
			ans += b[len(b)-1] - lastG
		}
	}
	fmt.Println(ans)
}