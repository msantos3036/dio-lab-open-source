package main

import "fmt"

func parte1() {
	fmt.Println("Números divisíveis por 3:")

	for i := 1; i <= 100; i++ {
		if i%3 == 0 {
			fmt.Println(i)
		}
	}
}

func parte2() {
	fmt.Println("\nJogo Pin Pan:")

	for i := 1; i <= 100; i++ {

		if i%3 == 0 {
			fmt.Println("Pin")
		} else if i%5 == 0 {
			fmt.Println("Pan")
		} else {
			fmt.Println(i)
		}

	}
}

func main() {

	parte1()
	parte2()

}
