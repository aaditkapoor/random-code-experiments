package main

import "fmt"
import "errors"


type Problem struct {
	id int
	problem []string
	solution []string
}


func (p *Problem) addProblem(id int, problem []string, solution []string) {
	p.id = id
	p.problem = problem
	p.solution = solution
}


func getById(problems []Problem, id int) (Problem, error) {
	var p Problem 
	for _,prob := range problems {
		if prob.id == id {
			return prob, nil
		}

	}
	return p, errors.New("a")
}

func main() {
	fmt.Println("hello")

	var problems []Problem = []Problem{Problem{id:10, problem:[]string{"sdad","Dad"}, solution:[]string{"Dasda","dasda"}}}

	p, err := getById(problems, 10)

	if err != nil {
		fmt.Println("error")
	}
	fmt.Println(p)

}