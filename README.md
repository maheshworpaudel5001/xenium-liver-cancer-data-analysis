# xenium-liver-cancer-data-analysis

This repository contains preprocessing workflows and reference-based cell typing pipelines for analyzing human liver data from the **Xenium platform by 10x Genomics**. The dataset includes both **healthy** and **diseased (cancerous)** liver tissue samples, enabling spatial transcriptomic comparisons between normal and pathological liver states.

## Data
    Source: [10x Genomics – Human Liver Data (Xenium)](https://www.10xgenomics.com/datasets/human-liver-data-xenium-human-multi-tissue-and-cancer-panel-1-standard)


## 📌 Project Goals

- Preprocess raw Xenium spatial transcriptomics data.
- Perform **quality control and normalization** steps.
- Conduct **reference-based cell type annotation** using external single-cell RNA-seq datasets.
- Explore spatial distribution of cell types across healthy and cancerous liver tissues.
- Lay the foundation for further downstream analyses such as **differential expression**, **spatial domain discovery**, and **tumor microenvironment characterization**.


## 📚 Documentations

- [FeatureMatrixLoader Tutorial](docs/feature_matrix_loader.md)
