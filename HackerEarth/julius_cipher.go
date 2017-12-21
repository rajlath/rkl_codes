package main

import(
		"bufio"
		"os"
		"strconv"
		"fmt"
)



var local=false
var scanner *bufio.Scanner

func is_palindrome(s string) bool{
	l := len(s)
	for i:=0; i<l/2; i++{
		if s[i] != s[l-i-1]{
			return false
		}
	}
	return true
}

func main(){
	setup()

	noc := readInt()
	for i := 0; i < noc; i++{
		s := readString()
		if is_palindrome(s) == true{
			fmt.Println("Palindrome")
		}else{
			product := int64(1)
			for _,x := range(s){
				mult := int64(x - 96)
				product *= int64(mult)
			}
			fmt.Println(product)
		}


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





