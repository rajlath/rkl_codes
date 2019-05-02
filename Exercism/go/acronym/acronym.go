package acronym

import (
	"strings"
)

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {
	//Abbreviate takes in  s a string as parameter.
	//Task is to concat first letter(converted upper case)
	// of all words in the string
	sarray := strings.Fields(s)
	var abbr string
	for _, v := range sarray {
		abbr += strings.ToUpper(string(v[0]))
	}
	return abbr
}
