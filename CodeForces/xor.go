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
	k := readInt()
	arr := make([]int, n)

	for i:=1; i<n+1; i+=1{
		arr[i] = i
	}
	current_xor := 0
	for i := 0; i < k; i+=1{
		current_xor ^= arr[i]
	}
	fmt.Println(arr)
	max_xor := current_xor
    for i:= k-1; i < n; i+=1{
		current_xor ^= arr[i-k]
		current_xor ^= arr[i]
		if current_xor > max_xor{
			max_xor = current_xor
		}

	}
	fmt.Println(max_xor)





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

func readString() string{
	scanner.Scan()
	ans := scanner.Text()
	return ans
}

func readInt() int{
	 scanner.Scan()
	 ans, _ := strconv.ParseInt(scanner.Text(), 10, 0)
	 return int(ans)
	}

func readInt64() int64{
	scanner.Scan()
	ans, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	return ans
}

func readIntArr(size int) []int{
	arr := make([]int, size)
	for i:=0; i < size; i++{
		arr[i] = readInt()
	}
	return arr
}


