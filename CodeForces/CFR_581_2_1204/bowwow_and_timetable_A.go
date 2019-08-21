package main

import (
	"fmt"
	"strconv"
)

func main() {
	var given string
	fmt.Scanf("%s", &given)
	lens := len(given)
	answer := (lens - 1) / 2
	oneplus := given[1:]
	if (lens-1)%2 != 0 {
		answer++
		fmt.Println(answer)
		return
	}
	rets := 0
	rets, _ = strconv.Atoi(oneplus)
	if rets == 0 {
		fmt.Println(answer)
		return
	}
	answer++
	fmt.Println(answer)

}
