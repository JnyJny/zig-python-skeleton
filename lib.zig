/// Add two integers and return the result.
/// Uses C calling convention for Python interop.
export fn add_numbers(a: i32, b: i32) i32 {
    return a + b;
}

/// Multiply two floats and return the result.
/// Uses C calling convention for Python interop.
export fn multiply_floats(a: f64, b: f64) f64 {
    return a * b;
}

/// Calculate factorial of a number.
/// Returns -1 for invalid input (negative numbers).
export fn factorial(n: i32) i64 {
    if (n < 0) return -1;
    if (n == 0 or n == 1) return 1;
    
    var result: i64 = 1;
    var i: i32 = 2;
    while (i <= n) : (i += 1) {
        result *= i;
    }
    return result;
}