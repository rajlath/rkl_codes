package main

import(
		"bufio"
		"os"
)



var local=false
var scanner *bufio.Scanner





func main(){
	setup()
	case_cnt = readInt()
	for (i:=1; i <case_cnt; i++ ){
		students = readInt()
		updates  = readInt()
		var a [5]int


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




