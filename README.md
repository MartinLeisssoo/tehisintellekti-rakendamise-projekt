# TÜ Kursuste Nõustaja

Tartu Ülikooli kursuste semantilise otsingu ja soovitamise rakendus. Kasutaja kirjutab vabatekstilise päringu (ET/EN), rakendus leiab sobivad kursused embeddingute abil ning LLM põhjendab tulemused arusaadavalt.

## Mida see projekt teeb

- Teeb semantilist kursuseotsingut, mitte ainult märksõna-põhist nimeotsingut.
- Rakendab filtreid (nt semester, EAP, hindamisskaala, õppekeel, linn, õppeaste, õppeviis, valdkond).
- Järjestab tulemused (semantiline / cross-encoder reranker / kohalik LLM reranker).
- Genereerib lõpliku vastuse OpenRouteri kaudu (`google/gemma-3-27b-it`).
- Näitab kursusi koos sobivushinde, lühikirjelduse ja ÕISi lingiga.

## Tehniline arhitektuur

1. Kursuste andmed laetakse failist `andmed/puhastatud_andmed.csv`.
2. Eelarvutatud embeddingud laetakse failist `andmed/embeddings.pkl`.
3. Päring kodeeritakse mudeliga `BAAI/bge-m3`.
4. Tehakse cosine-sarnasusel põhinev kandidaatide leidmine.
5. Kandidaadid järjestatakse (vaikimisi `BAAI/bge-reranker-v2-m3`).
6. LLM koostab lõpliku vastuse ainult valitud kursusekonteksti põhjal.

## Projekti struktuur

```text
.
├── app.py                         # Streamlit põhirakendus
├── pages/1_Arendaja.py            # Arendaja vaade (benchmark + debug)
├── app_logic/                     # Otsingu, filtrite, LLM-i ja andmelaadimise loogika
├── app_ui/                        # Benchmarki UI komponendid
├── andmed/
│   ├── puhastatud_andmed.csv      # Puhastatud kursuseandmed
│   ├── embeddings.pkl             # Eelarvutatud embeddingud
│   └── toorandmed_aasta.csv       # Toorandmestik
├── andmetega_tutvumine.ipynb      # EDA
├── andmete_puhastamine.ipynb      # Andmete puhastus
├── build_embeddings.py            # Embeddingute uuesti arvutamine
├── Testjuhtumid.csv               # Benchmark testjuhud
├── projektiplaan.md               # CRISP-DM projektiplaan
└── environment.yml                # Conda keskkond
```

## Kiire käivitamine

### 1) Loo keskkond

```bash
conda env create -f environment.yml
conda activate oisi_projekt
```

### 2) Lisa API võti

Loo projekti juures `.env` fail:

```bash
OPENROUTER_API_KEY=your-key-here
```

Võid kasutada ka süsteemi keskkonnamuutujat või Streamlit secretsi.

### 3) Käivita rakendus

```bash
streamlit run app.py
```

Ava `http://localhost:8501`.

## Arendaja vaade ja benchmark

- Arendaja vaade asub Streamlit multipage menüüs (`Arendaja`).
- Seal saab:
  - jooksutada testikomplekti failist `Testjuhtumid.csv`,
  - võrrelda retrieval/reranker/LLM etappide täpsust,
  - vaadata detailseid vigu ja salvestatud benchmark tulemusi.

## Embeddingute uuendamine

Kui kursuseandmed muutuvad, arvuta embeddingud uuesti:

```bash
python build_embeddings.py
```

Pärast seda taaskäivita Streamlit rakendus.

## Tehnoloogiad

- Python 3.10
- Streamlit
- pandas, numpy, scikit-learn
- sentence-transformers
- OpenAI SDK (OpenRouter API jaoks)

## Piirangud

- Andmed on lokaalne snapshot, mitte reaalajas ÕISi peegel.
- Tulemus sõltub andmete puhastuse kvaliteedist ja embeddingute ajakohasusest.
- LLM võib mõnikord anda ebatäpse põhjenduse; seetõttu on benchmark ja käsitsi hindamine olulised.
