package main

import "fmt"

type Graph struct {
	data map[int]int
}


func (graph *Graph) addEdge(u, v int) {
	graph.data = make(map[int]int)
	graph.data[u] = v
}

func main() {
	graph := Graph{data:nil}

	graph.addEdge(1, 2)
		graph.addEdge(2, 2)
	graph.addEdge(3, 2)
	graph.addEdge(4, 2)
	graph.addEdge(5, 2)
	graph.addEdge(6, 2)
	graph.addEdge(7, 2)
	graph.addEdge(8, 2)
	graph.addEdge(9, 2)


	fmt.Println(graph)

}