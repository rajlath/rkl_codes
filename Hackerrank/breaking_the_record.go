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
	noc := readInt()
	begins := readInt()
	maxr := 0
	minr := 0
	mxs  := begins
	mins := begins
	i    := 0
	for i < (noc - 1) {
		curr := readInt()

		if curr > mxs{
			maxr += 1
			mxs = curr
		}
		if curr < mins{
			minr += 1
			mins = curr
		}

		i += 1

	}
	fmt.Println(maxr, minr)


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

func readIntArr(size int) []int{
		arr := make([]int, size)
		for i:=0; i < size; i++{
			arr[i] = readInt()
		}
		return arr
	}





