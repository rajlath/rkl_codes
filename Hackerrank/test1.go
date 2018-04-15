package main

import (
	"fmt"
	"strings"
)

func main() {
	words := "11100010101"
	fmt.Printf("Number of l's in %s is: ", words)

	fmt.Printf("%d %d\n", strings.Count(words, "1"), strings.Count(words, "1")-strings.Count(words, "11"))
}
