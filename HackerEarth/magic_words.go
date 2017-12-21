package main

import(
		"bufio"
		"os"
		"strconv"
		"fmt"
)



var local=false
var scanner *bufio.Scanner

var primes = [12]int{67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113}

func abs(a int) int{
    if a < 0{
        return a * -1
    }else{
        return a
    }
}

func get_nearest(i int) int{
	mins := 300
	nearest:=0
	for _,x := range(primes){
		dist := abs(x - i)
		if dist < mins{
			mins = dist
			nearest = x
		}
	}
	return nearest
}




func main(){
	setup()
	noc := readInt()
	for i := 0; i < noc; i++{
		_ = readInt()
		wrd := readString()
		ans := ""
		for _,ch := range(wrd){
			nearest := get_nearest(int(ch))
			ans += string(nearest)

		}
		fmt.Println(ans)
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




