package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var nameCount int
	var name string
	names := make(map[string]int)
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanf(reader, "%d\n", &nameCount)
	for i := 0; i < nameCount; i++ {
		fmt.Fscanf(reader, "%s\n", &name)
		if names[name] == 0 {
			fmt.Println("OK")
		} else {
			fmt.Printf("%v%v\n", name, names[name])
		}
		names[name]++
	}
}
