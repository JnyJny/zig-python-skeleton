const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const zigmath_module = b.createModule(.{
        .root_source_file = b.path("src/zigmath.zig"),
        .target = target,
        .optimize = optimize,
    });

    const zigmath = b.addLibrary(.{
        .name = "zigmath",
        .root_module = zigmath_module,
        .linkage = .dynamic,
    });

    zigmath.linkLibC();
    b.installArtifact(zigmath);

    const test_step = b.step("test", "Run library tests");
    const zigmath_tests = b.addTest(.{
        .root_module = zigmath_module,
    });
    const run_zigmath_tests = b.addRunArtifact(zigmath_tests);
    test_step.dependOn(&run_zigmath_tests.step);
}