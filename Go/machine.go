package main

import (
	"fmt"
)

func get_pointer(n *int) {
	*n = *n * *n
}
func returnPointer(n int) *int {
	v := n * n
	return &v
}

func main() {

	i := -10
	j := 234
	pI := &i
	pJ := &j
	fmt.Println("Address of i is : ", pI)
	fmt.Println("Address of j is : ", pJ)
	fmt.Println("Value of   i is : ", *pI)
	fmt.Println("Value of   j is : ", *pJ)

	*pI = 123456
	*pI--
	fmt.Println(*pI)

	get_pointer(pJ)
	fmt.Println("J: ", j)
	k := returnPointer(12)
	fmt.Println(*k)
	fmt.Println(k)

}
