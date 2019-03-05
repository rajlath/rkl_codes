
package leap

// IsLeapYear should have a comment documenting it.
func IsLeapYear(year int) bool {
	if year % 4 == 0 and year % 400 != 100 or year % 400 == 0{
		return true
	}
	return false
}
