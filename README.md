# Intro to Testing — Workshop

Six small banking functions, each already written and working. Your job is to
write the tests.

You are scored on how many deliberately broken versions of these functions your
tests can detect. There are five broken versions of each function, so 30 points
in total. A broken version counts as caught when one of your tests fails against
it — which only happens if your test actually checks the behaviour that version
gets wrong.

## Getting started

```bash
git clone https://github.com/airwallex-community/intro-testing-workshop-application.git
cd intro-testing-workshop-application

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Set your name

Open `student.yaml` in the repo root and fill in your name — this is what
appears on the leaderboard:

```yaml
name: "Ada Lovelace"
project: ""          # leave blank unless told otherwise
```

Then create a branch and push. Any branch name works as long as it is not
`main`, `master`, or `feature-branch-1`:

```bash
git checkout -b my-branch
```

## Writing the tests

Each function has its own directory containing the implementation and a test
file with stubs to fill in:

| # | Directory | Function |
|---|---|---|
| 1 | `Function 1: Receive Contribution/` | `receive_contribution` |
| 2 | `Function 2: Calculate Interest/` | `calculate_interest` |
| 3 | `Function 3: Categorise Transaction/` | `categorise_transaction` |
| 4 | `Function 4: Transfer Funds/` | `transfer_funds` |
| 5 | `Function 5: Apply Transaction/` | `apply_transaction` |
| 6 | `Function 6: Process Batch Transactions/` | `process_batch_transactions` |

**Read the docstring first.** It is the specification: it tells you the valid
input ranges, what gets returned, and which errors are raised. Every broken
version breaks something the docstring promises.

Run your tests from the repo root:

```bash
pytest                                        # everything
pytest "Function 1: Receive Contribution/"    # one function
pytest --cov                                  # with coverage
```

## Getting on the leaderboard

Push your branch:

```bash
git add -A
git commit -m "Tests for function 1"
git push -u origin ada-lovelace
```

Every push runs the pipeline. Your **coverage** appears on the leaderboard within
a minute or two. Your **score** is calculated at the same time but stays hidden
until the reveal at the end of the session.

Push as often as you like — only your most recent push counts.

### Reading your results

Open the **Actions** tab, click your run, and read the summary. It shows your
coverage, how many broken versions you caught per function, and — most usefully —
whether any of your tests **fail against the working code**. A test that fails
against the correct implementation is a broken test: it can never detect
anything, so it scores nothing. Fix those first.

## Two things worth knowing

**Coverage is not the same as detection.** You can execute every line of a
function and still catch nothing, because coverage measures which lines ran, not
whether you checked the result. `assert` is what catches bugs.

**Boundaries are where the bugs live.** If a docstring says "amounts *exceeding*
10,000", then 10,000 itself is a different case from 10,001. Several of the
broken versions are exactly that kind of off-by-one.

## Troubleshooting

**`ModuleNotFoundError`** — run `pytest` from the repo root, not from inside a
function directory. `pytest.ini` puts the function directories on the import path.

**Windows: clone fails** — the directory names contain a colon, which Windows
does not allow in filenames. Use WSL, a Mac or Linux machine, or a Codespace.
