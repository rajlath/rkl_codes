package bob

import (
	"strings"
	"unicode"
)

// Hey should have a comment documenting it.
func Hey(remark string) string {
	remark = strings.trimspace(remark)

	switch remark {
	case remark == "":
		return "Fine. Be that way!"
	case any(remark, unicode.IsUpper()) && !any(remark, unicode.IsLower()):
		return "Whoa, chill out!"
	case remark[len(remark)-1] == '?':
		return "Sure."
	default:
		return "Whatever."

	}
}
