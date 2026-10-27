# FIN494-workspace — v1.3

Your local research project contains supplied code and a clearly labeled synthetic dataset. Follow the separate **assignment** and **installation guide** included in the teaching bundle or linked in Canvas.

## Project contents

| File | Purpose |
|---|---|
| `DATA_DICTIONARY.md` | Source, units, missing values, and calculation rules |
| `sample_data/synthetic_prices.csv` | Eight invented observations; keep this input unchanged |
| `check_python.py`, `check_R.R` | Short runtime checks; each should report 2% |
| `analyze_prices.py`, `analyze_prices.R` | Read a file, inspect it, calculate returns, save and reopen results |
| `pyproject.toml`, `uv.lock`, `.python-version` | Python requirements, resolved packages, and selected interpreter version |
| `SETUP_REPORT.md` | Assignment response template |
| `outputs/` | Created when you run the analysis; these small synthetic outputs belong in this exercise's Git history |

The ZIP includes the Git/AI ignore settings. Keep those settings when extracting the whole project folder.

## Run the baseline

In Cursor's project terminal, after installing uv:

```bash
uv python install 3.12.14
uv sync --locked
uv run --locked python check_python.py
uv run --locked python analyze_prices.py
```

In the R terminal, with this project as the working directory:

```r
source("check_R.R")
source("analyze_prices.R")
```

Both analyses initially select `SYN_A`: 4 output rows and 3 usable returns. Each script writes its own CSV into `outputs`. Open the CSVs in Cursor and compare them. R and Python may format decimals or quote fields differently; the values should agree.

**Save this baseline with your Git GUI before changing the analysis.** Then change only the focus setting from `SYN_A` to `SYN_B` in both analysis scripts, rerun, verify the results, and review/commit the change. Keep the source CSV and the two runtime-check scripts unchanged.

For this tiny exercise, outputs are overwritten on each run; your baseline commit preserves the earlier version. Future research projects may use a different output-storage policy.

The scripts use only Python standard-library modules and base R. The assignment requires Cursor Pro plus ChatGPT Plus or Claude Pro (or approved equivalents). API keys and extra usage purchases are not required. The full guide explains R integration, GUI history, and optional Codespaces.
