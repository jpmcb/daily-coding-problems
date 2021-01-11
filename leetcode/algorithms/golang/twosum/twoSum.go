package main

import "fmt"

func main() {
	fmt.Printf("%v\n", twoSum([]int{2, 7, 5, 11}, 7))
}

// Leetcode - Two Sum
// https://leetcode.com/problems/two-sum/

// A sloution must exist - there is always 1 pair of numbers that satisfy the target sum
// therefore for all numbers (x1, x2, ... xn), xa + xb = solution
// We can find the inverse with xa = target - xb
func twoSum(nums []int, target int) []int {

	// Memory O(n)
	// - store a running inverse of possible solutions
	dict := make(map[int]int)

	for i, num := range nums {
		// If the current number is in the dictonary ...
		_, ok := dict[num]
		if ok {
			// Then we have found xa and can return the indexes
			return []int{i, dict[num]}
		} else {
			// Store the inverse ndex and the target key
			dict[target-num] = i
		}
	}

	return []int{0, 0}
}
