# 📚 Bibliothèque ETL

A beginner-friendly Python project for learning data manipulation with **Pandas**, built around a complete **ETL pipeline** (Extract → Transform → Load) applied to a personal book library.

---

## ✨ What It Does

The pipeline reads raw book and author data, cleans and enriches it, then exports a final report ready for analysis. A Jupyter notebook provides statistics and visualizations on top of the output.

**Sample data includes 15+ books** (Le Petit Prince, 1984, Dune, etc.) with authors from 13 different nationalities.

---

## 🗂️ Project Structure

```
bibliotheque_etl/
├── data/
│   ├── livres.csv          ← raw book data (title, author, year, rating, genre)
│   └── auteurs.json        ← author metadata (nationality, birth/death year)
├── src/
│   ├── extract.py          ← Step 1: read CSV & JSON files
│   ├── transform.py        ← Step 2: clean, merge, and enrich data
│   └── load.py             ← Step 3: save output and print summary
├── output/
│   └── rapport_final.csv   ← generated report (auto-created on run)
├── pipeline.py             ← main entry point
└── analyse.ipynb           ← analysis notebook with charts
```

---

## ⚙️ Installation

Requires **Python 3.7+**.

```bash
pip install pandas jupyter
```

---

## 🚀 Usage

### Run the full pipeline

```bash
python pipeline.py
```

This will:
1. Load `data/livres.csv` and `data/auteurs.json`
2. Clean the data (drop missing titles, remove duplicates, fill missing ratings)
3. Enrich it (merge with author info, compute book age, categorize ratings)
4. Export the result to `output/rapport_final.csv`
5. Print a summary to the console

### Explore analyses in the notebook

```bash
jupyter notebook analyse.ipynb
```

---

## 🔄 Pipeline Steps

### 1 — Extract (`src/extract.py`)
- Reads `livres.csv` into a Pandas DataFrame
- Reads `auteurs.json` and converts it to a DataFrame
- Prints column types, shape, and missing value counts

### 2 — Transform (`src/transform.py`)
- **Cleans** the books DataFrame: drops rows with no title, removes exact duplicates, fills missing ratings with the column mean, strips whitespace
- **Enriches** by merging books with author data on author name (left join)
- **Adds computed columns:**
  - `age_livre` — how many years ago the book was published
  - `categorie_note` — rating label (⭐ Excellent / 👍 Bon / 😐 Moyen / 👎 Mauvais)
  - `auteur_vivant` — whether the author is still alive

### 3 — Load (`src/load.py`)
- Exports the final DataFrame to `output/rapport_final.csv` (UTF-8 with BOM for Excel compatibility)
- Prints a summary: total books, unique authors, genres, average rating, oldest and newest book

---

## 📊 Analysis Notebook

`analyse.ipynb` covers:

| Section | Content |
|---|---|
| General stats | Descriptive statistics for year, rating, and book age |
| By genre | Book count per genre (bar chart) |
| Rating by genre | Average rating per genre (horizontal bar chart) |
| Top 5 books | Highest-rated books with author and genre |
| Top authors | Authors with the most books in the library |
| By nationality | Distribution of books by author nationality |

---

## 🧠 Pandas Concepts Practised

| Concept | Used in |
|---|---|
| `pd.read_csv()` / `json.load()` | `extract.py` |
| `df.dropna()` / `df.fillna()` | `transform.py` |
| `df.drop_duplicates()` | `transform.py` |
| `df.str.strip()` | `transform.py` |
| `pd.merge()` | `transform.py` |
| `df['col'].apply(fn)` | `transform.py` |
| `df.groupby()` | `load.py`, `analyse.ipynb` |
| `df.to_csv()` | `load.py` |
| `df.value_counts()` | `analyse.ipynb` |

---

## 📄 License

MIT — free to use, modify, and share.
