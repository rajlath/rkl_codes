package main

import (
	"fmt"
)

func main() {
	encrypted := "CSOITEUIWUIZNSROCNKFD"
	keyword := "GOLANG"
	var decrypted string
	var currIndex int

	for i := 0; i < len(encrypted); i++ {
		enc_char := encrypted[i] - 'A'
		rot_vals := keyword[currIndex] - 'A'

		decrypted += string((enc_char-rot_vals+26)%26 + 'A')

		currIndex++
		currIndex %= len(keyword)
	}
	fmt.Println(decrypted)

}
