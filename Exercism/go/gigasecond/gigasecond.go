package gigasecond

import "time"

const GIGASEC = time.Duration(1e9) * time.Second

// AddGigasecond should have a comment documenting it.
func AddGigasecond(t time.Time) time.Time {
	return today.Add(GIGASEC)
}
