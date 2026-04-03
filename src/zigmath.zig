const std = @import("std");

/// Add two integers and return the result.
/// This function is exported with C ABI for use from Python via ctypes.
export fn add(a: i32, b: i32) i32 {
    return a + b;
}

/// Compute factorial of a non-negative integer.
/// Returns 1 for input 0, -1 for negative input.
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

test "add function" {
    const testing = std.testing;
    try testing.expect(add(2, 3) == 5);
    try testing.expect(add(-1, 1) == 0);
    try testing.expect(add(0, 0) == 0);
}

test "factorial function" {
    const testing = std.testing;
    try testing.expect(factorial(0) == 1);
    try testing.expect(factorial(1) == 1);
    try testing.expect(factorial(5) == 120);
    try testing.expect(factorial(-1) == -1);
}