You can interact with an embedding of the abstracts [here](https://gclen.github.io/covid19-kaggle/plots/umap_covid-19_interactive.html)

### Methodology

To find related papers we used the following methods:

1. Load the dataset using code from <a href="https://www.kaggle.com/dgunning/browsing-research-papers-with-a-bm25-search-engine">this kaggle kernel</a>
2. Tokenize the abstracts using <a href="https://allenai.github.io/scispacy/">scispacy</a> and vectorize using <a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">sklearn's TfidfVectorizer</a>
3. Embed the vectors into a lower dimensional space using <a href="https://umap-learn.readthedocs.io/en/latest/">UMAP</a>
4. Cluster the embedding using <a href="https://hdbscan.readthedocs.io/en/latest/index.html">HDBSCAN</a> to find related abstracts
5. Rank each point by its distance to a representative point within the cluster to find relevant documents within a cluster.
6. Use Bokeh to create widgets to visualize and interact with the embedding

