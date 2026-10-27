# Two-minute runtime check with synthetic numbers. Base R only.
simple_return <- 102 / 100 - 1
stopifnot(abs(simple_return - 0.02) < 1e-12)
cat(R.version.string, "\n")
cat("R installation:", R.home(), "\n")
cat("Working folder:", getwd(), "\n")
cat(sprintf("R return: %.2f%%\n", 100 * simple_return))
cat("Checks passed.\n")
