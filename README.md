# megumi
  
Extract words specific for the documents.
Help to create standard dictionary for translation..

## Usage
  
1. Download [idf file](https://github.com/SmartDataAnalytics/Wikipedia_TF_IDF_Dataset/blob/master/en/wiki_tfidf_terms.csv.gz) and extract
1. Download [main.exe](dist/main.exe)
1. Run as below
    - main.exe "input file" "idf file" "output file"
1. Output csv is word and tfidf score descending by tfidf score
  
# megumi
  
文書に特有の単語を抽出する。
翻訳用の標準的な辞書の作成に役立ちます。

## 使い方
  
1. [idfファイル](https://github.com/SmartDataAnalytics/Wikipedia_TF_IDF_Dataset/blob/master/en/wiki_tfidf_terms.csv.gz)をダウンロードして解凍
1. [main.exe](dist/main.exe)のダウンロード
1. 以下のように実行します。
    - main.exe "入力ファイル" "idfファイル" "出力ファイル"
1. 出力csvはwordとtfidf scoreの降順です。
  
## Example
  
### Input
  
> In information retrieval, tf–idf, TF*IDF, or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.[1] It is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general. tf–idf is one of the most popular term-weighting schemes today. A survey conducted in 2015 showed that 83% of text-based recommender systems in digital libraries use tf–idf.[2]
  
> Variations of the tf–idf weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query. tf–idf can be successfully used for stop-words filtering in various subject fields, including text summarization and classification.
  
> One of the simplest ranking functions is computed by summing the tf–idf for each query term; many more sophisticated ranking functions are variants of this simple model.

### Output: 
  
|token|tfidf|
|-----|-----|
|tf|65.04194026389581|
|idf|61.57461624616373|
|weighting|25.635316210661735|
|document|19.563411752300684|
|query|15.239514206269591|
|retrieval|14.944575816662159|
|ranking|14.509206851720396|
|tfidf|14.506969480885603|
|text|13.055136144740828|
|corpus|12.588079034137126|
|word|11.359222987673595|
|recommender|10.980608956269442|
|summarization|10.761394683095121|
|frequency|10.351774982426583|
|user|10.111710445318149|
|term|9.965700434089669|
|functions|8.910784875230357|
|summing|8.11393629594858|
|words|7.929476273337833|
|proportionally|7.837471391027724|
|statistic|7.741930504105061|
|filtering|7.328932644131853|
|computed|6.983668267367072|
|inverse|6.9281422289953785|
|simplest|6.694726182148463|
|information|6.654330413800743|
|relevance|6.608805974111417|
|adjust|6.483526312445102|
|searches|6.430557742705098|
|offset|6.331891082076768|
|numerical|6.324596558008198|
|used|6.027642079597936|
|modeling|6.02381578169289|
|schemes|5.808622080427418|
|sophisticated|5.775417881436428|
|83|5.660280714204174|
|libraries|5.561636864322329|
|variants|5.465797548458463|
|variations|5.172289834653813|
|tool|5.089804659417794|
|increases|5.026169495253225|
|reflect|4.983888637116863|
|engines|4.9714345121978685|
|helps|4.952684857449507|
|classification|4.891164000801256|
|mining|4.86164834943676|
|scheme|4.693224303850337|
|documents|4.614930547743218|
|factor|4.584463922513713|
|survey|4.447361760665859|
|contain|4.387819625249927|
|number|4.381088601169297|
|scoring|4.353852251799439|
|search|4.3135024968490105|
|digital|4.135135922202109|
|successfully|4.1330617192185235|
|fields|4.126854451963461|
|simple|4.120263911645035|
|value|4.0741879003004415|
|showed|4.0081772980055455|
|frequently|3.9943052982365317|
|stop|3.9272181402011466|
|conducted|3.8826466262193597|
|intended|3.759324708901775|
|appear|3.7565126933822617|
|appears|3.7204102225039417|
|systems|3.7012698370848796|
|model|3.6693774738439844|
|subject|3.659790060127381|
|collection|3.5312991765183455|
|fact|3.4996554792953205|
|today|3.1526217027158467|
|popular|3.015713785236854|
|short|2.947475365099555|
|important|2.946537214586398|
|2015|2.686353455005336|
|given|2.6736455104303416|
|various|2.642608105109048|
|central|2.625883945927053|
|times|2.559738810374047|
|general|2.4962387908417933|
|use|2.4477392854681965|
|based|2.2947358532419564|
|including|1.8159686747208046|
