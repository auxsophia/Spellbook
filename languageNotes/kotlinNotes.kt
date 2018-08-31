/**
* A KT file contains source code written in Kotlin, a statically typed programming
* language developed by JetBrains. Kotlin supports both functional and
* object-oriented styles and is most often used to supplement or replace Java
* when developing business and end user applications.
*/

// This is an end-of-line comment

/* This is a block comment
   on multiple lines. */

// Defining variables
// Assign-once (read-only) local variable:

val a: Int = 1  // immediate assignment
val b = 2   // `Int` type is inferred
val c: Int  // Type required when no initializer is provided
c = 3       // deferred assignment

// Mutable variable:
var x = 5 // `Int` type is inferred
x += 1

// Top-level variables:
val PI = 3.14
var x = 0

fun incrementX() {
    x += 1
}

// String templates
var a = 1
// simple name in template:
val s1 = "a is $a"

a = 2
// arbitrary expression in template:
val s2 = "${s1.replace("is", "was")}, but now is $a"
// evalautes to: a was 1, but now is 2

// Using conditional expressions
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}

// or

fun maxOf(a: Int, b: Int) = if (a > b) a else b

// Using nullable values and checking for null
// A reference must be explicitly marked as nullable when null value is possible.
// @Return null if str does not hold an integer:
fun parseInt(str: String): Int? {
    // ...
}

// Use a function returning nullable value:
fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

    // Using `x * y` yields error because they may hold nulls.
    if (x != null && y != null) {
        // x and y are automatically cast to non-nullable after null check
        println(x * y)
    }
    else {
        println("either '$arg1' or '$arg2' is not a number")
    }
}

// or
// ...
if (x == null) {
    println("Wrong number format in arg1: '$arg1'")
    return
}
if (y == null) {
    println("Wrong number format in arg2: '$arg2'")
    return
}

// x and y are automatically cast to non-nullable after null check
println(x * y)

// Practicing null
var rainbowColor = "violet"

rainbowColor = null
// error: null can not be a value of a non-null type String
// rainbowColor = null

// Declare two variables, greenColor and blueColor. Use two different ways of setting them to null.
var greenColor = null
// Good!

var blueColor? = null
// incomplete code

var blueColor = String? = null
// incomplete code

// Also good!
var blueColor: String? = null

// Practice Time: Nullability/Lists
// Create a list with two elements that are null; do it in two different ways.
// Next, create a list where the list is null.

listOf(null,null)
// returns [null, null]
var list: List<Int?> = listOf(null, null)

// list2 can be null
var list2:List<Int>? = null

// Practice Time: Null Checks
// Create a nullable integer variable called nullTest, and set it to null. Use a
// null-check that increases the value by one if it's not null, otherwise returns
// 0, and prints the result.
var nullTest: Int? = null
println(nullTest?.inc() ?: 0)

// Note: '?:' is called the Elvis operator and functions similarly to the
// ternary operator - it returns the following value if the expression is null.


// Documenting code
/**
 * A group of *members*.
 *
 * This class has no useful logic; it's just a documentation example.
 *
 * @param T the type of a member in this group.
 * @property name the name of this group.
 * @constructor Creates an empty group.
 */
class Group<T>(val name: String) {
    /**
     * Adds a [member] to this group.
     * @return the new size of the group.
     */
    fun add(member: T): Int { ... }
}
