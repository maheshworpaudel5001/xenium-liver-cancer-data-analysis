# xenium-liver-cancer-data-analysis

This repository contains preprocessing workflows and reference-based cell typing pipelines for analyzing human liver data from the **Xenium platform by 10x Genomics**. The dataset includes both **healthy** and **diseased (cancerous)** liver tissue samples, enabling spatial transcriptomic comparisons between normal and pathological liver states.

## 📊 Data
Source: [10x Genomics – Human Liver Data (Xenium)](https://www.10xgenomics.com/datasets/human-liver-data-xenium-human-multi-tissue-and-cancer-panel-1-standard)

📥 Data Access
To download and use the Xenium dataset:

Visit the dataset page

Download the dataset ZIP file(s) (Liver cancer -> xenium_data/diseased and Non-diseased -> xenium_data/non_diseased)

Extract and place them under xenium_data/ directory in this repo

## 📌 Project Goals

- Preprocess raw Xenium spatial transcriptomics data.
- Perform **quality control and normalization** steps.
- Conduct **reference-based cell type annotation** using external single-cell RNA-seq datasets.
- Explore spatial distribution of cell types across healthy and cancerous liver tissues.
- Lay the foundation for further downstream analyses such as **differential expression**, **spatial domain discovery**, and **tumor microenvironment characterization**.
- 📈 Preliminary Results: Analysis results and figures will be added as the project progresses.


## 🗂️ Repository Structure

```bash
xenium_liver_cancer/
|
├── xenium_data/                      # Input Xenium datasets (healthy & diseased)
    |-diseased
    |-non_diseased
├── scripts/                   # Modular Python/R scripts for pipeline steps
├── results/                   # Output figures, cell type labels, etc.
├── environment.yml            # Conda environment YAMLs
├── README.md                  # Project overview
└── ....                       # python classes and helper functions

**Tools and Technologies**
- Python: Main programming language for data preprocessing and analysis.
- Scanpy: For single-cell and spatial transcriptomics analysis.
- Anndata: Data structure for annotated data matrices.
- Zarr: Efficient storage of large, chunked, compressed, N-dimensional arrays.
- R (optional): For additional analysis and visualization (e.g., Seurat).
- Jupyter Notebooks: Interactive analysis and visualization.
- Conda: Environment and dependency management.

** 📌 To Do**
 ✅ Setup project structure

 Preprocess Xenium liver cancer and healthy data

 Perform reference-based cell typing

 Visualize spatial cell distributions

 Add documentation and analysis figures

## 📚 Documentations

- [FeatureMatrixLoader](documents/feature_matrix_loader.md)
- [CellStatloader](documents/cell_stat_loader.md)

🙋 Acknowledgments
10x Genomics for providing the Xenium platform and datasets.

The broader open-source community for tools used in spatial transcriptomics.

