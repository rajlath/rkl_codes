package main

import (
	"fmt"
	"math"
)

func main() {
	var i, x, have, power, days int
	fmt.Scan(&i)
	for x = 0; x < i; x++ {
		fmt.Scan(&have)
		fmt.Scan(&power)
		days = 1
		for have > 0 {
			needed := int(math.Pow(float64(days), float64(power)))
			if needed < have {
				days += 1
				have -= needed
			} else {
				break
			}

		}
		fmt.Println(days - 1)

	}
}
