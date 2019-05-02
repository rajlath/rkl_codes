package main

import (
	"fmt"
	"math/rand"
	"time"
)

const DISTANCE = 62100000
const SECONDSPERDAY = 86400

func main() {
	spacelines := [3]string{
		"SpaceX", "Space Adventures", "Virgin Galactic",
	}
	mode := [2]string{"One-way", "Round-trip"}

	var spaceline, TripType string
	var speed int

	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	fmt.Printf("%-21s %-11s %-15s %-30s\n", "Spaceline", "Trip Days", "Trip Type", "Price")
	for i := 0; i < 10; i++ {
		spaceline = spacelines[r.Intn(3)]
		speed = r.Intn(15) + 16
		TripDays := DISTANCE / speed / SECONDSPERDAY
		cost := int(float32(TripDays) * 1.2)
		TripType = mode[r.Intn(2)]

		if TripType == "Round-trip" {
			cost = cost * 2
		}
		fmt.Printf("%-20s %10d %-15s %15d\n", spaceline, TripDays, TripType, cost)

	}
}
