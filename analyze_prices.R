# Read DATA_DICTIONARY.md first. The supplied prices are entirely synthetic.
# Run with the project as working directory: source("analyze_prices.R")
# Windows/macOS fallback: source(file.choose(), chdir = TRUE); select this file.

focus_security <- "SYN_A" # The assignment changes this one setting to SYN_B.

data_path <- file.path("sample_data", "synthetic_prices.csv")
if (!file.exists(data_path)) {
  stop("Open R in FIN494-workspace; see the working-folder step in the guide.")
}
prices <- read.csv(data_path, na.strings = c("", "NA"),
                   colClasses = c("character", "character", "numeric"))
stopifnot(identical(names(prices), c("security_id", "date", "price")))
prices$date <- as.Date(prices$date, format = "%Y-%m-%d")

# Each security/date pair should describe one observation.
stopifnot(!anyNA(prices$security_id), !anyNA(prices$date),
          all(nzchar(trimws(prices$security_id))),
          !anyDuplicated(prices[c("security_id", "date")]),
          all(is.na(prices$price) |
              (is.finite(prices$price) & prices$price > 0)))
prices <- prices[order(prices$security_id, prices$date), ]

# Shift prices within each security. Preserve missing observations.
prices$previous_price <- ave(prices$price, prices$security_id,
                            FUN = function(x) c(NA_real_, head(x, -1L)))
prices$price_return <- prices$price / prices$previous_price - 1
result <- prices[prices$security_id == focus_security, ]
if (!nrow(result)) stop("focus_security was not found in the source file.")

dir.create("outputs", showWarnings = FALSE)
output_path <- file.path("outputs", "returns_R.csv")
write.csv(result, output_path, row.names = FALSE, na = "")

# Reopen the saved artifact as part of the workflow.
saved <- read.csv(output_path, na.strings = "")
cat("Input:", normalizePath(data_path, winslash = "/"), "\n")
cat(sprintf("Source: %d rows | %d securities | %d missing price\n",
            nrow(prices), length(unique(prices$security_id)), sum(is.na(prices$price))))
cat("Dates:", format(min(prices$date)), "through", format(max(prices$date)), "\n")
cat(sprintf("Selected: %s | %d rows | usable returns: %d\n", focus_security,
            nrow(result), sum(!is.na(result$price_return))))
cat("Output:", normalizePath(output_path, winslash = "/"), "\n")
cat(sprintf("Reopened %d saved rows. Returns are decimals; 0.02 means 2%%.\n",
            nrow(saved)))
