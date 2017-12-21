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
	for i := 0; i < noc; i++{
		n := readInt()
		arr := readIntArr(n)
		cnt := 0
		for ndx1,val1 := range(arr)	{
			for ndx2, val2 := range(arr){
				if ndx1 != ndx2 && val1 != val2{
					if (val1%2==0 && val2%2==0) || (val1%2!=0 && val2%2!=0){
						cnt += 1
					}
				}
			}

		}
		fmt.Println(cnt/2)

	}



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





