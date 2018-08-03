package main
import "fmt"
import "io/ioutil"
import "math"
import "os"

func main() {
	for T := ScanInt(1, 1e4); T > 0; T-- {
		NewLine()
		var freq [26]int
		sum := 0
		for n := range freq {
			freq[n] = ScanInt(0, 1e9)
			sum += freq[n]
		}
		max := (sum - 1) / 2
		if max <= 0 {
			fmt.Println(max)
			continue
		}
		sofar := 0
		n := -1
		for sofar < sum - max {
			n++
			sofar += freq[n]
		}
		if sum - sofar >= max {
			fmt.Println(max)
			continue
		}
		fn := freq[n]
		if fn > sofar - fn - 1 {
			fn = sofar - fn - 1
			if fn < 0 {
				fn = 0
			}
		}
		if max > sum - sofar + fn {
			max = sum - sofar + fn
		}
		fmt.Println(max)
	}
}
func ScanInt(low, high int) int {
	return int(ScanInt64(int64(low), int64(high)))
}
func NewLine() {
	if CheckInput {
		for n, b := range RemainingInput {
			if b != ' ' && b != '\t' && b != '\r' {
				Assert(b == '\n')
				RemainingInput = RemainingInput[n+1:]
				return
			}
		}
		Assert(false)
	}
}
func ScanInt64(low, high int64) int64 {
	x := Btoi(ScanToken())
	Assert(low <= x && x <= high || !CheckInput)
	return x
}

var RemainingInput []byte

func init() {
	var e error
	RemainingInput, e = ioutil.ReadAll(os.Stdin)
	if e != nil {
		panic(e)
	}
}
func Assert(condition bool) {
	if !condition {
		panic("assertion failed")
	}
}

func Btoi(s []byte) int64 {
	if s[0] == '-' {
		x := Btou(s[1:])
		Assert(x <= - math.MinInt64)
		return - int64(x)
	} else {
		x := Btou(s)
		Assert(x <= math.MaxInt64)
		return int64(x)
	}
}
var CheckInput = true

func ScanToken() []byte {
	for n, b := range RemainingInput {
		if b == ' ' || b == '\t' || b == '\r' {
			continue
		}
		if b == '\n' {
			Assert(!CheckInput)
			continue
		}
		RemainingInput = RemainingInput[n:]
		break
	}
	Assert(len(RemainingInput) > 0)
	n := 1
	for ; n < len(RemainingInput); n++ {
		b := RemainingInput[n]
		if b == ' ' || b == '\t' || b == '\r' || b == '\n' {
			break
		}
	}
	token := RemainingInput[:n]
	RemainingInput = RemainingInput[n:]
	return token
}

func Btou(s []byte) uint64 {
	Assert(len(s) > 0)
	var x uint64
	for _, d := range s {
		Assert('0' <= d && d <= '9')
		d -= '0'
		if x >= math.MaxUint64 / 10 {
			Assert(x == math.MaxUint64 / 10 && d <= math.MaxUint64 % 10)
		}
		x = x * 10 + uint64(d)
	}
	return x
}