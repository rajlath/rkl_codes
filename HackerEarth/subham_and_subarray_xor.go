package main

import(
		"bufio"
		"os"
		"strconv"
		"fmt"
)

var local=false
var scanner *bufio.Scanner


func main(){
	setup()
	n := readInt()
	pre := make([]int, n+1)

	arr := readIntArr(n)
	var i,j,k int
	pre[0] = arr[0]
	for i:=1; i<n; i++{
		pre[i] = arr[i] + pre[i-1]
	}

	ans := 0
	for i=1; i < n-1; i++{
		for j = i+1; j < n ; j++{
			for k = i; k < j; k++{
				var1 := pre[i] ^ (pre[j] - pre[k])
				ans = max(ans, var1)

				var2 := arr[i] ^ (pre[j] - pre[k])
				ans = max(ans, var2)

			}
		}
	}
	fmt.Println(ans)
}

func setup(){
	source := os.Stdin
	if local == true{
		file,_ := os.Open("input.txt")
		source = file
	}
	scanner = bufio.NewScanner(source)
	scanner.Split(bufio.ScanWords)
}
func readInt() int{
	scanner.Scan()
	ans, _ := strconv.ParseInt(scanner.Text(), 10, 0)
	return int(ans)
   }
func readIntArr(size int) []int{
	arr := make([]int, size)
	for i:=0; i < size; i++{
		arr[i] = readInt()
	}
	return arr
}

func max(a int, b int) int{
	if a >= b{
		return a
	}else{
		return b
	}
}
