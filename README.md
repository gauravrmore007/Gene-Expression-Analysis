# 🧬 Gene Expression Analysis (scRNA-seq)

This project performs a basic single-cell RNA-seq (scRNA-seq) analysis using Python and the Scanpy library. It includes steps for preprocessing, clustering, visualization, and marker gene detection.

---

## 📁 Project Structure

gene_project/
├── data/ # Contains the .h5 dataset (download manually)
├── results/ # Stores generated plots and outputs
├── script.py # Main analysis script
├── gene_expression_analysis.py # Alternative or extended script
├── Requirement.txt # List of Python dependencies


---

## 📥 Dataset

Download the sample dataset from 10x Genomics:

📎 [PBMC 3k filtered_feature_bc_matrix.h5 (HDF5)](https://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_3k/pbmc_3k_filtered_feature_bc_matrix.h5)

Save this file into the `data/` folder and rename it if needed (e.g., `your_file.h5`).

---

## ▶️ How to Run

1. **Install required packages**:
   ```bash
   pip install -r Requirement.txt

2. **Run the analysis**:
    ```bash
   python script.py


## 🔬 Pipeline Steps
- Load and filter scRNA-seq data
- Normalize and transform
- PCA + UMAP for visualization
- Cluster with Leiden algorithm
- Detect marker genes

## 📊 Outputs
- UMAP plot of clusters
- PCA plot
- Marker gene heatmap

## 🧠 Extensions
- Add sample comparison (e.g. healthy vs diseased)
- Train ML model for cell type classification

## 👨‍💻 Author
Gaurav More
