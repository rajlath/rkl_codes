package main

import(
		"fmt"
		"bufio"
		"strconv"
		"os"
)


var f [2000005]int
var g [2000005]int
var scanner *bufio.Scanner

func readString() string {
	scanner.Scan()
	return scanner.Text()
}

func readInt() int {
	val, _ := strconv.Atoi(readString())
	return val
}



func main(){
	var n int = 2000005
	scanner = bufio.NewScanner(os.Stdin)
	for i:=0;i<n;i++{
		f[i] = f[i/10] + (i & 1)*(i%10)
	}
	for i:=1;i<n;i++{
		for j:=i; j<n; j+=i{
			g[j] = g[j]+f[i]
		}
	}

	x := readInt()
	for i:=0; i < x; i++{
		m := readInt()
		fmt.Println(g[m])
	}
}