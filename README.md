
![giphy](https://github.com/user-attachments/assets/de4338d0-17ae-4301-80eb-034546c257d2)

# Coronavirus twitter analysis (2020)

This project analyzes geotagged tweets from 2020 to track the spread of coronavirus-related discussions on social media. Using MapReduce, we process a large dataset of 1.1 billion tweets to extract insights about hashtag usage across different languages and countries.

**Dataset and Structure**

The dataset contains all geotagged tweets sent in 2020, stored in daily zip files, each containing 24 JSON-formatted text files. The project consists of mapper and reducer scripts, visualization tools, and an alternative reducer for time-series analysis.

**Implementation**

The mapping phase extracts hashtags, counts occurrences by language and country, and saves results in separate files. The reducing phase aggregates hashtag counts across all mapped files. Visualization scripts generate bar graphs of top hashtags and line plots showing hashtag trends over time.

**Running the Project**

Clone the repository, ensure Python and required libraries are installed, then execute the mapping phase with 
```
nohup ./run_maps.sh &
```
reduce with 
```
python3 src/reduce.py
```
and generate visualizations using 
```
python3 src/visualize.py or python3 src/alternative_reduce.py
```

**Results and Future Work**

The analysis provides insights into hashtag usage by country and language, with visualizations highlighting key trends.

Using visualize.py:

![country#coronavirus](https://github.com/user-attachments/assets/a5ce2ae7-7335-4e16-9073-569df51e6aab)

![lang#coronavirus](https://github.com/user-attachments/assets/c0f3454b-a993-44ee-9549-e996ad9cc386)

![country#코로나바이러스](https://github.com/user-attachments/assets/e11a6d6c-ea4a-41b0-8c48-18233b3a3e0e)

![lang#코로나바이러스](https://github.com/user-attachments/assets/cddd07eb-20e9-48e4-b238-8b683adf1919)

Using alternative_reduce.py:

![alternative_reduce py#corona](https://github.com/user-attachments/assets/0945726e-3124-4b69-9be0-cefde67dd411)


