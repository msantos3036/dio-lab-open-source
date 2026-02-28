package main

import "fmt"

const ebulicaoK float64 = 373.15

func main() {
	tempK := ebulicaoK
	tempC := tempK - 273.15

	fmt.Printf("Temperatura de ebulição da água: %.2f K\n", tempK)
	fmt.Printf("Temperatura de ebulição da água: %.2f °C\n", tempC)
}
