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
	dicts := make(map[int]int)
	for i:=0; i<n;i++{
		ins := readInt()
		dicts[ins] += 1
	}
	cnt := 0
	for i:= range(dicts){
		if dicts[i] == 2{
			cnt += 1
		}else{
			if dicts[i] > 2{
				cnt += (dicts[i] *(dicts[i]-1))/2
			}
		}

	}
	fmt.Println(cnt)
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