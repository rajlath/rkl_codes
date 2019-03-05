package twofer

//import "fmt"

//ShareWith()
func ShareWith(name string) string {
	if name == "" {
		name = "You"
	}
	return "One for" + name + ", one for me."
}


