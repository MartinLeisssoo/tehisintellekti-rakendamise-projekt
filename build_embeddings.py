"""Pre-compute embeddings for all courses and save as a pickle file.

Usage:
    conda activate oisi_projekt
    python build_embeddings.py

This reads toorandmed/puhastatud_andmed.csv, encodes the 'description'
column with BAAI/bge-m3, and saves the resulting numpy array to
toorandmed/embeddings.pkl.  Re-run this script whenever the CSV changes.
"""

import time
import pickle

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

DATA_PATH = "toorandmed/puhastatud_andmed.csv"
OUTPUT_PATH = "toorandmed/embeddings.pkl"
MODEL_NAME = "BAAI/bge-m3"
BATCH_SIZE = 8         # keep very small to avoid OOM on CPU/limited-RAM machines


def main() -> None:
    print(f"Loading data from {DATA_PATH} ...")
    df = pd.read_csv(DATA_PATH)
    print(f"  {len(df)} courses, {len(df.columns)} columns")

    # Validate that 'description' column exists
    if "description" not in df.columns:
        raise ValueError(
            "'description' column not found in CSV. "
            "Available columns: " + ", ".join(df.columns)
        )

    texts = df["description"].fillna("").astype(str).tolist()

    avg_len = sum(len(t) for t in texts) / len(texts)
    print(f"  Avg description length: {avg_len:.0f} chars")

    print(f"Loading embedding model '{MODEL_NAME}' (this may take a few minutes on first run) ...")
    model = SentenceTransformer(MODEL_NAME)

    print(f"Encoding {len(texts)} descriptions (batch_size={BATCH_SIZE}) ...")
    t0 = time.time()
    embeddings = model.encode(texts, batch_size=BATCH_SIZE, show_progress_bar=True)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s  |  shape: {embeddings.shape}")

    # Sanity check
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == len(df)

    print(f"Saving embeddings to {OUTPUT_PATH} ...")
    with open(OUTPUT_PATH, "wb") as f:
        pickle.dump(embeddings, f)

    print("Finished. You can now run: streamlit run app.py")


if __name__ == "__main__":
    main()
