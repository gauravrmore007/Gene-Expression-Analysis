# script.py
import scanpy as sc
import os
import matplotlib.pyplot as plt

# === Setup ===
input_file = "data/your_file.h5"  # <-- Change this to match your actual filename
output_dir = "results"
os.makedirs(output_dir, exist_ok=True)

# === Load data ===
print("Loading data...")
adata = sc.read_10x_h5(input_file)
adata.var_names_make_unique()

# === Quality control ===
print("Running quality control...")
adata.obs['n_counts'] = adata.X.sum(axis=1)
adata.obs['n_genes'] = (adata.X > 0).sum(1)

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# === Normalization and transformation ===
print("Normalizing and log-transforming...")
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata

# === Highly variable genes ===
print("Selecting highly variable genes...")
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata = adata[:, adata.var.highly_variable]

# === Scaling and PCA ===
print("Scaling and PCA...")
sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, save="_pca_plot.png", show=False)

# === Neighbors and UMAP ===
print("Computing neighbors and UMAP...")
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata)

# === Clustering ===
print("Clustering cells...")
sc.tl.leiden(adata, resolution=0.5)

# === Plot UMAP ===
print("Saving UMAP plot...")
sc.pl.umap(adata, color=["leiden"], save="_clusters.png", show=False)

# === Marker gene detection ===
print("Finding marker genes...")
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save="_markers.png", show=False)

# === Done ===
print("Analysis complete. Results saved in /results and /figures.")

# Save the processed dataset (optional)
# adata.write(os.path.join(output_dir, "processed_data.h5ad"))
