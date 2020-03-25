from bokeh.models import Div

header = Div(text="""<h1>Clustering COVID-19 research papers</h1>""")

overview = Div(text="""<p>This tool was developoed as a part of the <a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">Kaggle COVID-19 Open Research Dataset Challenge (CORD-19)</a>.
The goal of the challenge is to gain as much insight into COVID-19 as possible by analyzing prior research. However, there are ~29000 papers included in this dataset which is impossible for
a single researcher to go through. Therefore, we need to apply natural language processing (NLP) techniques to make it easier to find related papers, and papers on a particular topic.</p>""")

methodology = Div(text="""<h3>Methodology:</h3><p>To find related papers we used the following methods:
<ol>
<li>Load the dataset using code from <a href="https://www.kaggle.com/dgunning/browsing-research-papers-with-a-bm25-search-engine">this kaggle kernel</a></l1>
<li>Tokenize the abstracts using <a href="https://allenai.github.io/scispacy/">scispacy</a> and vectorize using <a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">sklearn's TfidfVectorizer</a></li>
<li>Embed the vectors into a lower dimensional space using <a href="https://umap-learn.readthedocs.io/en/latest/">UMAP</a></li>
<li>Cluster the embedding using <a href="https://hdbscan.readthedocs.io/en/latest/index.html">HDBSCAN</a> to find related abstracts</li>
<li>Rank each point by its distance to a representative point within the cluster to find relevant documents within a cluster.</li>
<li>Use Bokeh to create widgets to visualize and interact with the embedding</li>
</ol>
</p>
""")

resources = Div(text="""<h3>Resources:</h3>
<ul>
<li><a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">COVID-19 Open Research Dataset Challenge (CORD-19)</a><</li>
<li>The interactive code was based on <a href="https://github.com/MaksimEkin/COVID19-Literature-Clustering">this repository</a> by <a href="https://github.com/MaksimEkin/">github user MaksimEkin</a></li>
</ul>
""")

description_search = Div(text="""<h3>Search by keyword:</h3><p>Search keywords to show abstracts containing those keywords. It will search abstracts, 
titles, journals, and authors. Please keep in mind that only 140 characters of abstracts are kept in the plot. Press enter when ready. 
Clear and press enter to reset the plot.</p>""")

description_slider = Div(text="""<h3>Filter by cluster:</h3><p>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to the right to show all points.</p>""")

description_checkbox = Div(text="""<h3>Ignore outlying points:</h3><p1>The checkbox below can be used to ignore documents that are not part of a cluster.</p1>""")

description_meta_slider = Div(text="""<h3>Explore metadata for a cluster</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the rows that belong to that cluster.</p1>""")

notes = Div(text="""<h3>Notes:</h3><p>The notebook and source code used to generate this widget can be found <a href="https://github.com/gclen/covid19-kaggle">here</a></p>""")




