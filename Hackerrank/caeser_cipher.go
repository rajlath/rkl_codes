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
	readInt()
	txt := readString()
	off :=rune(readInt())
	enc :=""
	tmp := rune(0)
	for _,ch := range(txt){

		if ch >= 65 && ch <= 90{
			tmp = (ch - 65 + off)%26
			fmt.Println(tmp)
			enc += string(tmp + 65)
		}else if ch >= 97 && ch <= 122{
			tmp = (ch - 97 + off)%26
			enc += string(tmp + 97)
		}else{
			enc += string(ch)
		}


	}
	fmt.Println(enc)
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





