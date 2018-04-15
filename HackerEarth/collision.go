package main

import (
	"fmt"
	"strings"
)

func main() {
	var noc, noe int
	fmt.Scan(&noc)
	for i := 0; i < noc; i++ {
		fmt.Scan(&noe)
		ast := make([]int, noe)
		for j := 0; j < noe; j++ {
			fmt.Scan(&ast[j])
		}
		var ans []int
		for _, element := range ast {
			if len(ans) == 0 || element >= 0 || ans[len(ans)-1]*element >= 0 {
				ans = append(ans, element)
				continue
			}
			for (len(ans) > 0) && (ans[len(ans)-1] >= 0) && (ans[len(ans)-1]+element < 0) {
				ans = ans[:len(ans)-1]
			}

			if len(ans) == 0 || ans[len(ans)-1] < 0 {
				ans = append(ans, element)
				continue
			}
			if ans[len(ans)-1]+element == 0 {
				ans = ans[:len(ans)-1]
			}
		}

		if len(ans) == 0 {
			fmt.Println("NOTHING")
		} else {
			fmt.Println(strings.Trim(fmt.Sprint(ans), "[]"))
		}

	}

}
