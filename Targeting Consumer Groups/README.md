## Project Summary
Data of new protein beverage products launched between 2020-2023 were collected from a commercial products database. The texts of 'product claims/description' were processed and the main topics were extracted. The main topics of each new 'product claims/description' provide us further understanding of which consumer group the product is targeting. For example, for new protein beverage products launched globally, there are 3 major targeting consumers groups: 1) Consumers who care most about the nutrition; 2) Consumers who care most about certified ingredients; 3) Consumers who care most about increased performance during workout and muscle building.

#### Problem Statement
The information of targeted consumer groups is implicitly embedded in the 'product claims & descriptions'. It is nearly impossible for humans to read through tens of thousands of product descriptions and extract the “hidden” topics. The insights of targeting consumer groups of the new products can provide guidance for product developers on new product development.

#### Dataset:
Product data of protein beverage products launched in 2020-2023, 19420 products (rows) x 23 features (columns). Data is not provided as it is collected from a market research company.

#### Steps
#### Step 1: Data Pre-processing
Data was processed to filter out invalid or duplicate samples. For example, some products are double counted as new product launches for the events of new packaging or importation to a region. These samples were filtered out before analysis. Valid data have < 1% missing values.

#### Step 2: Text processing
The texts of product claims/description were processed using NLP package `spacy` and customized tokenizers to provide the corpus for topic modeling.

#### Step 3: Topic modeling
Both K-means clustering and Latent Dirichlet Allocation (LDA) techniques were used and compared for topic modeling. But LDA was selected because it provided more semantics of the topics. Numbers of topics were determined based on both the coherence score of the LDA models and reviewing the clusters of top words.


