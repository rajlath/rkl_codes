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
	doors = "";
	for i:=0; i <nod; i++{
         doors += str(readInt)
	}

	}
	fmt.Println(doors)


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





