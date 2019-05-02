package main

import (
	"math/rand"
	"sort"
	"time"
)

func randIntsArray(min, max, len int, sorted bool) []int {
	rets := make([]int, len)
	rand.Seed(time.Now().UnixNano())
	for i := range rets {

		rets[i] = min + rand.Intn(max-min+1)
	}
	if sorted {
		sort.Ints(rets)
	}
	return rets
}
