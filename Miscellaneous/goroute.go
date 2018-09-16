package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	fmt.Println("started")
	wg.Add(1)
	go do_something()
	fmt.Println("end")
	wg.Wait()
}

func do_something() {
	fmt.Println("DO Something.")
	wg.Done()
}
