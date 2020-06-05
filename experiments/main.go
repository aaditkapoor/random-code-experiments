package main

import (
	"fmt"
)

// A benchmark of all popular algorithms (searching, sorting etc)
// Measuring time to search for a number (10000+ numbers) and measuring time.

func binarySearch(array []int, target int, lowIndex int, highIndex int) int {
	if highIndex < lowIndex {
		return -1
	}
	mid := int((lowIndex + highIndex) / 2)
	if array[mid] > target {
		return binarySearch(array, target, lowIndex, mid)
	} else if array[mid] < target {
		return binarySearch(array, target, mid+1, highIndex)
	} else {
		return mid
	}
}

// StylerInterface Style Interface
type StylerInterface interface {
	getText() string
	printText()
}

// Style Base Style
type Style struct {
	text string
}

func (s *Style) getText() string {
	return s.text
}

func (s *Style) printText() {
	fmt.Println(s.text)
}

// BoldStyle BoldStyle type
type BoldStyle struct {
	Style
}

// BoldStyleInterface Bold
type BoldStyleInterface interface {
	boldStyle()
}

// BoldStyle BoldStyle decorator
func (b *BoldStyle) boldStyle(base interface{}) {
	fmt.Println("BOLD")
	b.Style.printText()
}

func main() {
	s := Style{text: "Hello, World"}
	s.printText()
	bold := BoldStyle{Style{text: s.text}}
	bold.printText()
}
