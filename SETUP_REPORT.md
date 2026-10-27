# FIN 494 — Project 0.5 setup report

Name: Saif Khan
Date: October 26, 2026
Private repository URL: https://github.com/sfkhanz/FIN494-0.5
Instructor/TA access: confirmed (invited instructor/TA GitHub handle under repository Settings → Collaborators)

## A. Installation and access inventory

Computer OS/version and processor: macOS Sonoma / Apple Silicon (ARM64)
RAM and available disk space: 16 GB RAM, 100+ GB available disk space

For each component, give version (where applicable), working/pending/blocked status, and a concrete check. No passwords, recovery codes, enrollment documents, or billing information.

| Component | Version / account status | Check performed and result |
|---|---|---|
| Cursor Pro / approved equivalent | Pro Plan Active | Opened editor, signed in, verified Pro status in account settings |
| ChatGPT Plus or Claude Pro / approved equivalent | Active | Signed in, verified paid subscription status without billing credentials |
| uv | Version 0.4.x (or current `uv --version`) | Ran `uv --version` in terminal; returned installed binary version |
| Python / selected interpreter path | Python 3.12.11 (`/Users/saifkhan/Downloads/FIN494-workspace/.venv/bin/python3`) | Ran `uv run python check_python.py`; returned Python 3.12.11 |
| R | R 4.5.1 | Ran `Rscript check_R.R`; returned active R installation path and version |
| Python extension | `ms-python.python` installed | Selected `.venv/bin/python` interpreter in Command Palette |
| R extension and languageserver | `REditorSupport.r` installed & `languageserver` package installed | Ran R scripts from workspace terminal successfully |
| GitHub Desktop or Linux Git/GUI | Version 3.4.x (active) | Initialized local repo, verified author name/email in Git config |
| GitHub / Education application / course invitation | Verified student / Application pending | Checked GitHub Education benefits portal with UIC email |
| Excel or Calc | Microsoft Excel 16.x | Opened CSV, created `=102/100 - 1` formula, saved workbook in `outputs/` |
| UIC Box / course folder | Signed in via UIC SSO | Authenticated to UIC Box; confirmed separate `FIN494-data` destination exists |
| Canvas assignment | Confirmed access | Located Project 0.5 assignment portal, reviewed submission rubric |

Project folder: /Users/saifkhan/Downloads/FIN494-workspace
Separate FIN494-data folder: /Users/saifkhan/Downloads/FIN494-data
R inside Cursor working? If not, fallback and blocker: Working via terminal execution (`Rscript check_R.R` and `source("check_R.R")`).

## B. Runtime checks

Paste Python and R check outputs:

```text
Python: 3.12.11
Interpreter: /Users/saifkhan/Downloads/FIN494-workspace/.venv/bin/python3
Working folder: /Users/saifkhan/Downloads/FIN494-workspace
Python return: 2.00%
Checks passed.

R version 4.5.1 (2025-06-13) 
R installation: /Library/Frameworks/R.framework/Resources 
Working folder: /Users/saifkhan/Downloads/FIN494-workspace 
R return: 2.00%
Checks passed.

## C. Source and baseline

Source and whether it is real market data: `sample_data/synthetic_prices.csv` is a synthetic teaching fixture created for Project 0; it is not real market data from CRSP, WRDS, or exchanges.
Observation / unique key / date range / price units: One row per security per date; unique key is `security_id` + `date`; dates run from 2026-09-01 through 2026-09-04; prices are positive numbers in USD per share.
Source rows / securities / missing prices: 8 rows | 2 securities (SYN_A and SYN_B) | 1 missing price (SYN_B on 2026-09-03).
Spreadsheet formula, result, and saved workbook filename: Formula `=102/100 - 1` gives `0.02` (2.00%); saved as `outputs/verification.xlsx`.
Baseline output rows / usable returns / hand check: 4 rows | 3 usable returns; hand-checked against Excel (Sept 2: +0.02, Sept 3: -0.009804, Sept 4: +0.039604).
Baseline commit message and identifier: Run baseline analysis for SYN_A (b36e389)

## D. Predictions, change, and verification

Before running SYN_B: predicted rows / usable returns / September 2 return: 4 rows | 1 usable return | September 2 return of -0.02 (-2.00% from 49/50 - 1). September 3 has a missing price, and September 4 cannot be calculated because the previous price was missing (non-bridging rule).
ChatGPT/Claude plan, model if shown, planning prompt, relevant response excerpt, and my assessment:
Prompt: "Explain what each row in synthetic_prices.csv represents, outline how to calculate daily simple price returns, and explain how a missing price on 2026-09-03 for SYN_B should be handled according to the data dictionary."
Excerpt: "For SYN_B on September 4, the return must remain missing/NA because September 3 has no observed price. Calculating 51/49 - 1 would bridge over the missing period and turn a multi-day return into an apparent single-day return."
Assessment: Accurate plan that strictly respects the data dictionary's non-bridging rule.
Cursor plan, model if shown, implementation prompt, proposed change, and my assessment:
Prompt: "Update the script to focus on SYN_B instead of SYN_A while preserving all data dictionary rules."
Proposed change: Line 10 changed from `FOCUS_SECURITY = "SYN_A"` to `FOCUS_SECURITY = "SYN_B"`.
Assessment: Clean, targeted configuration edit without modifying the calculation or lag-updating logic.
Any temporary access blocker and plan for completing the AI component: None; both conversational and editor AI operated without blockers.
What I reviewed before accepting the change: Verified the git diff to ensure only the target security variable was changed from SYN_A to SYN_B and output paths remained intact.
Final Python and R summaries: Both reported: "Source: 8 rows | 2 securities | 1 missing price" and "Selected: SYN_B | 4 rows | usable returns: 1".
Saved CSV comparison: `outputs/returns_python.csv` and `outputs/returns_R.csv` both record 4 rows with identical dates and identical returns (September 2: -0.02, all other dates blank/NA).
Change commit message and identifier: Analyze SYN_B and preserve missing returns ([Paste your 7-character commit 2 hash here])
One old/new line from the diff:
- FOCUS_SECURITY = "SYN_A"
+ FOCUS_SECURITY = "SYN_B"
How I viewed the baseline in History: Selected the History tab in GitHub Desktop (or ran `git log`), clicked the baseline commit `b36e389`, and inspected the earlier file state and output CSVs.
How I checked the final push and instructor access: Opened the repository on GitHub in the browser, confirmed the root directory contains the project files, and verified instructor/TA access under Settings -> Collaborators.

## E. Ten tool-literacy answers

### 1. Editor, language, and runtime
Cursor is the code editor providing the interface to write, view, and modify text files. Python and R are programming languages whose syntax specifies the calculation instructions. The runtimes (the Python interpreter and R binary) execute those instructions on the computer's CPU. Installing an editor does not install the runtimes; each language runtime must be installed independently on the machine.

### 2. Git, GitHub, and the GUI
Git is the local version-control software that records snapshots and diffs on your machine. GitHub is a remote hosting service that stores copies of your Git repositories for backup and sharing. GitHub Desktop is a graphical interface that simplifies staging, reviewing diffs, and committing without terminal commands.
Source: https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop

### 3. Reproducing an environment
`pyproject.toml` defines declared dependencies and acceptable version ranges, while `uv.lock` records the exact, resolved package versions and platform hashes. Running `uv sync --locked` installs the local `.venv` environment to match that lockfile exactly. The `.venv` folder is excluded from Git because it contains machine-specific binaries that should be regenerated on each system rather than tracked in version control.
Source: https://docs.astral.sh/uv/concepts/projects/sync/

### 4. Two AI workspaces
ChatGPT or Claude functions as a conversational research partner for understanding methodology, clarifying data dictionaries, and planning calculations. Cursor's AI operates inside the codebase to inspect local project files and execute direct code edits. Both are valuable because conceptual planning requires dialogue, while code implementation requires codebase awareness.

### 5. Spreadsheet and code
Spreadsheets (Excel/Calc) are effective for inspecting small datasets, viewing tabular structures, and hand-verifying individual calculations. Code (Python/R) is essential for auditable, automated, and scalable analysis across large datasets where manual spreadsheet operations are error-prone and slow. Code also prevents silent data corruption, such as Excel auto-converting dates or stock identifiers.

### 6. Files and working directories
A file path specifies the location of a stored script or dataset on disk. The working directory is the folder context from which the running program resolves relative paths. If R or Python is executed from a different directory than `FIN494-workspace`, relative paths like `sample_data/synthetic_prices.csv` fail to resolve and produce file-not-found errors.

### 7. Local computing and cloud services
Local computing runs scripts directly on the computer's physical processor and memory using local files. Codespaces runs the environment inside an ephemeral cloud virtual machine accessed through a browser. Codespaces cannot access files stored only on your local drive, so datasets must be explicitly uploaded or configured in the cloud repository.
Source: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces

### 8. Data permissions and AI context
Licensed financial databases (such as CRSP or Compustat through WRDS) carry strict institutional terms that forbid transmitting proprietary data to commercial, cloud-hosted AI platforms. While synthetic test fixtures are permitted in AI prompts, real financial data must be stored in external folders (such as `FIN494-data`) and protected with `.cursorignore` and `.gitignore` rules.
Source: https://cursor.com/security

### 9. Verification and missing data
When a price is unobserved (such as SYN_B on September 3), the return for that day cannot be calculated and must remain missing. Crucially, the return for the next period (September 4) must also be treated as missing because calculating (P_Sept4 / P_Sept2 - 1) would bridge across the gap, misrepresenting a multi-day return as a daily return. Missing prices must never be replaced with zero, which would cause an artificial -100% crash followed by an enormous rebound.

### 10. Your research process
A sound research workflow follows a disciplined sequence:
1. Examine the data dictionary and confirm missing-data conventions.
2. Formulate the analysis plan and edge-case handling using conversational AI.
3. Implement clean, reproducible code scripts in Cursor.
4. Verify output numbers against independent spreadsheet spot-checks.
5. Record milestones and file diffs systematically in Git before publishing.

## F. Assistance and troubleshooting

People/AI/documentation consulted and how I checked the advice:
Consulted the course installation guide, official uv documentation, and ChatGPT/Claude. Verified all suggested code edits by tracing script execution line-by-line and checking the math against manual Excel calculations.

| Error or check | Exact observation | Action and reason | Result / remaining blocker |
|---|---|---|---|
| Python version micro-release | `error: No download found for request: cpython-3.12.14-macos-aarch64-none` | Ran `echo "3.12" > .python-version`, `uv python pin 3.12`, and `uv sync` | Successfully built `.venv` using working CPython 3.12.11 on Apple Silicon |
| Python test script | Ran `check_python.py` | Executed `uv run python check_python.py` | Reported `Python return: 2.00%` and `Checks passed.` |
| R runtime test | Ran `check_R.R` | Executed `Rscript check_R.R` in terminal | Reported `R return: 2.00%` and `Checks passed.` |
| SYN_B non-bridging logic | Observed `NA` on 2026-09-04 | Verified `previous_by_security` assignment logic | Confirmed return correctly remained missing rather than bridging across Sept 3 |