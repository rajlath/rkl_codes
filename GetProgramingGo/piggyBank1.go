package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	amt := [3]float32{0.05, 0.1, 0.25}
	var need float32 = 0.0

	for need < 20.0 {
		curr := amt[r.Intn(3)]
		need += curr
		fmt.Printf("Added %4.2f and now amount is %5.2f\n", curr, need)
	}
}
