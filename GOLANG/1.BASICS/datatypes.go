package main // main its an executable file anything else means a library which can be imported by other files
import "fmt"
func main(){
	var i int
	var f float64
	var b bool
	var s string
	
	i = 42
	f = 3.14
	b = true
	s = "Hello, Go!"
	fmt.Println("Integer : %d DoubleIntger : %d", i,i*2)
	fmt.Println("Float : %f", f)
	fmt.Println("Boolean : %t", b)
	fmt.Println("String : %s", s)
}
// %s → string

// %d → integer (decimal)

// %f → floating-point number

// %t → boolean

// %v → default format (works for almost any type)

// %T → print the type of a value