This project is on Email Spam CLassification using bag of words model and a Naive Bayes Classifier. This was done as a part of my graduate course - Elements of Artificial Intelligence.
The data files are compressed to distribute them efficiently
via github. To extract, type:

tar -xzf data.tar.gz

The problem is primarily split into two parts:
* Training the emails in the training directory using bag of words model
* Classifying the emails in the test directory using a Naïve Bayes Classifier

In the first part, to train the emails using bag of words model, first, the emails in training directory have been tokenized into independent words and put into two bags (spam and notspam). A count of the spam and notspam words is calculated and stored as a dictionary.
Probability of spam emails is calculated as 
<b>P(spam|words) = number of spam files/total number of files</b>
Probability of notspam emails is calculated as 
<b>P(notspam|words) = number of notspam files/total number of files</b>

In the second part, to classify the emails in the test directory, ideally, we need to calculate the probability of each email belonging to spam and notspam. For this, we need to multiply the probability of each word in the email occurring in spam and not spam. In some cases, a word present in test directory email might not be present in the train directory. In this case, the probability value becomes zero and the model will not be able to classify it as spam or notspam, due to which an accuracy of 82.14565387627252. To improve this, a laplace smoothening has been done after tokenizing the words (reference - [https://towardsdatascience.com/unfolding-na%C3%AFve-bayes-from-scratch-2e86dcae4b01](https://towardsdatascience.com/unfolding-na%C3%AFve-bayes-from-scratch-2e86dcae4b01) and [https://en.wikipedia.org/wiki/Additive_smoothing](https://en.wikipedia.org/wiki/Additive_smoothing)). The missing words have been represented as "UnKnown" in the words dictionary 

Since all the probability values are small, multiplying them will give a very small value, leading to underflow error. To overcome this, we take log of these values and add each of the log probabilities (since log(x*y) = log(x) + log(y)) -> reference: [https://towardsdatascience.com/unfolding-na%C3%AFve-bayes-from-scratch-2e86dcae4b01](https://towardsdatascience.com/unfolding-na%C3%AFve-bayes-from-scratch-2e86dcae4b01)
Hence, in the testing step, we tokenize all the test emails and sum up the log probabilities of each of the tokenized words. If the sum of spam is higher than that of notspam, we tag it as spam, else we tag it as notspam and the result is written to output-file.

Finally, to calculate accuracy of our model, we read the actual classified values from test-groundtruth.txt and the predicted values from output-file and use scikit-learn accuracy-score method to find accuracy. The accuracy observed is 96.51527016444791

## Running the code:
The code is run using the command  <b>python3 spam.py training-directory testing-directory output-file</b>.

Please ensure that the train directory files are inside a folder "training-directory" which has two folders within it - spam and notspam and test directory files are inside a folder "testing-directory"
