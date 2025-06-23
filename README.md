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
   python script.py

🧪 Analysis Steps
Load and filter single-cell data

Normalize and log-transform gene counts

Identify highly variable genes

Perform PCA and UMAP for visualization

Cluster cells using Leiden algorithm

Identify marker genes for each cluster

📊 Output Examples
Clustered UMAP plot: figures/umap_clusters.png

PCA plot: figures/pca_plot.png

Marker heatmap: figures/markers.png

📌 Notes
The .h5 file must be placed in the data/ folder.

File name should match the one in the script (your_file.h5) or be updated accordingly.

🧠 Future Ideas
Compare healthy vs diseased samples

Build a web app for interactive exploration

Use machine learning to classify cell types
