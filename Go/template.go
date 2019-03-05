package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

func getCommandLine() {
	myResponse := ""
	arguments := os.Args
	if len(arguments) == 1 {
		myResponse = "I need at least one arguments. None provided"
	} else {
		myResponse = arguments[1]
	}

	io.WriteString(os.Stdout, myResponse)
	io.WriteString(os.Stdout, "\n")
}

func getUserInput() {
	var f *os.File
	f = os.Stdin
	defer f.Close()
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		fmt.Println("> ", scanner.Text())
	}
}

func getMaxAndMin() {

	if len(os.Args) == 1 {
		fmt.Println("I need at least one float value here.")
		os.Exit(0)
	} else {
		args := len(os.Args)
		min := 123456789.569
		max := 0.0
		arguments := os.Args
		for n := 1; n < args; n++ {
			val, _ := strconv.ParseFloat(arguments[n], 64)
			if val < min {
				min = val
			}
			if val > max {
				max = val
			}
		}
		fmt.Println("Min :", min)
		fmt.Println("Max :", max)
	}

}

func sumAllCommanLineArgs() {
	if len(os.Args) == 1 {
		fmt.Println("Please give one or more floats.")
		os.Exit(1)
	}
	arguments := os.Args
	sums := 0.0
	for i := 1; i < len(arguments); i++ {
		n, err := strconv.ParseFloat(arguments[i], 64)
		if err == nil {
			sums = sums + n
		} else {
			fmt.Println("Not all values are float.")
			os.Exit(0)
		}
	}
	fmt.Println("Sum of all values:", sums)
}

func showAverageOfValues() {
	if len(os.Args) == 1 {
		fmt.Println("Please give one or more floats.")
		os.Exit(1)
	}
	arguments := os.Args
	sums := 0.0
	for i := 1; i < len(arguments); i++ {
		n, err := strconv.ParseFloat(arguments[i], 64)
		if err == nil {
			sums = sums + n
		} else {
			fmt.Println("Not all values are float.")
			os.Exit(0)
		}
	}
	l := float64(len(arguments) - 1)
	avg := sums / l
	fmt.Println("Average of all values :", avg)
}



func main() {
	//getCommandLine()
	//getUserInput()
	//getMaxAndMin()
	sumAllCommanLineArgs()
	showAverageOfValues()

}
