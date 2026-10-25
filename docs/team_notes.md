# Team Notes

## Phase 1 decisions

- **Scope / region:** Karnataka, India (proposed, confirm in team meeting)
- **Dataset schema:** see `data/data_dictionary.md`
- **Target:** 100+ rows, source recorded for every row
- **Raw data file:** `data/raw/practices_raw.csv` (start from `practices_template.csv`)

## Phase 2 source split

| Member | Sources |
|---|---|
| a | Research papers (Google Scholar, ResearchGate) |
| b | ICAR / Karnataka agriculture dept. publications |
| c | FAO Ecocrop and GAEZ (environment values) |

Each member collects into their own CSV (`practices_a.csv`, `practices_b.csv`, `practices_c.csv`) in `data/raw/`, then we merge into `practices_raw.csv`.

## Git conventions

- Work on `feature/<phase>-<name>` branches, PR into `dev`, one teammate reviews.
- `main` stays stable.

## Meeting log

| Date | Notes |
|---|---|
|  |  |