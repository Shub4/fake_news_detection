# Fake News Detection

In this Project the goal is to create Fake News Detection model using NLP and Machine Learning algorithms to combat the problem of fake content circulated in news. This model is trained on the dataset with thousands of  news collected from different sources particularly from North America.
Dataset Description
One dataset inlcudes news related to USA election having 4,009 records and the other includes news from all over the western countries particularly North America with 69,045 records.
Attributes contains:
•	Serial number
•	Title: raw content from different news platforms
•	Text: raw content from different news platforms
•	Labels: represent class as Fake and True


### Related Work

#### 1. Fake News from Social Platforms
Social platforms includes social media, websites, blogging pages, forums sometimes cause panic among the society when there is  widespread fake news being circulated including lots of misinformation which can lead to some concerning issues. This could create a massive impact on the people’s mind resulting in accidents, educational shock, riots, etc.

#### 2.	Natural Language Processing
The main reason of utilizing NLP is to work with the specialization of system understanding speech and to detect actions in various languages. The sentiment analysis extract emotions on the particular subject. Here we are using tree bank method. 

#### 3.	Machine Learning Classification
Since our data is class oriented , supervised classification model are being chosen achieve more accurate results. There are three algorithms that are adopted in this project for classifying the fake news.

#### 3a.	Naïve Bayes
This works on the bayes theorem of probability.Naive Bayes assumes that one function in the category has nothing to do with another. The NB models are good at representing simple behaviors in data not complex, but can be reshaped easily.

#### 3b.	KNN (k-Nearest Neighbors)
This works on the principle of euclidean distance and is a cluster vased model. KNN classifies positions based on the measured distance from the neighboring k with respect to them. 

#### 3c.	Random Forest
Random Forest are built on the concept of building many decision tree algorithms, after which the decision trees get a separate result. The results, which are predicted by large number of decision tree, are taken up by the random forest. Unlike NB it can work easily on complex behaviors of data, but it can result in overfitting also.


### Results

The confusion matrix for all algorithms:
![image](https://user-images.githubusercontent.com/83857444/138891092-fb79071b-cf8d-43b6-b543-79a764381306.png)
![image](https://user-images.githubusercontent.com/83857444/138891197-6492a715-2626-472b-b676-d037a01c8581.png)
![image](https://user-images.githubusercontent.com/83857444/138891224-ed17f0e4-6b63-4693-a0c1-a363a4df43ff.png)

Accuracy Score:
     ![image](https://user-images.githubusercontent.com/83857444/138891241-816a7dbf-2427-4bcb-b899-63fb17713230.png)


Mean Absolute Error:
     ![image](https://user-images.githubusercontent.com/83857444/138891273-17169476-b912-469b-aaf9-8124cb9322c8.png)

 
### Conclusion:
* Here we will be focusing on improved False Negative as we want to predict fake news correctly.KNN is lagging on most of the metrics maintaining lowest performance. Naïve Bayes has good Recall than Random forest but it is somewhat equal and RF recall can be further improved by increasing n_estimators. 
*	Naïve Bayes comes out to be fastest to train the model following by RF and KNN.
*	Accurancy is quite improved in Random forest which is 5.8% more than NB and f-Score is 3.4% more.
*	Though training RF is time consuming but it has shown significant improvement in performance and predicting better than the other two models with the overall accuracy of 90% which has potential for further improvements with parameter tunning.

### Skills
*	NLP, Sentiment Analysis
*	Feature extraction from raw text using TF-IDF, CountVectorizer
*	Sklearn
*	Flask
*	Html
