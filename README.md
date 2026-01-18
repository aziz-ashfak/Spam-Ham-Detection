# Spam-Ham-Detection

# Project Overview
This project aims to detect spam and ham message by using different model. It consists of various components including datasets, source code, static files, templates, and analysis results etc.

## Directory Structure
```
├── .github
   ├── workflows
       ├── main.yml
├── Dataset
   ├── Spam_SMS.csv   # dataset from kaggle

├── ResultAnalysis
    ├── analysis.ipynb              #  analysis accuracy and confusion matrix
    ├── confusion_matrix.npy        #  confusion matrix npy file
    ├── result.csv                  # save accuracy result
    ├── test.py                     # test single prediction 
├── kaggleFullNoteBook 
    ├── thyroid-disease-prediction-Full-NoteBook.ipynb  # my kaggle notebook
├── artifacts 
    ├── model.pkl                  # save the model
    ├── processing_data.csv        # after using text extractor
    ├── vectorizer.pkl              # save preprocessor
├── notebook
    ├── spam-sms-classification-using-nlp.ipynb    # my kaggle full notebook
├── src  
    ├── component
      ├── __init__.py
      ├── data_ingestion.py                    # split data and transform data 
      ├── data_transformation.py               # transform all columns
      ├── model_trainner.py                    # model trainner class
   ├── pipeline
      ├── _init__.py
      ├── predict_pipeline.py                   # prediction function
 ├── _init__.py
 ├── exception.py                               # custom exeption
 ├── logger.py                                  # logging info store method
 ├── utilts.py                                  # save all common function
   
├── static
    ├── styles.css                              # style.css file include     
├── templates
    ├── home.html                               # html file include           
├── .gitignore             
├── LICENSE                                    
├── README.md                                   # reame file
├── app.py                                      # application 
├── requirements.txt                            # requirements file
└── setup.py                                    # setup 
```

## Dataset link 

```bash
https://www.kaggle.com/datasets/mariumfaheem666/spam-sms-classification-using-nlp/data
```
# Describe the project
About Dataset
Data Collection
This corpus has been collected from free or free for research sources at the Internet:
The SMS Spam Collection is a public set of SMS labeled messages that have been collected for mobile phone spam research.
## Describe the preprocessesor 
In this project we use 80% data as trainset and  20% data as testset.In this project we use  one preprocessing method:
      **TfidfVectorizer**: use for input columns
     
## Models we use 
    LogisticRegression
    DecisionTreeClassifier
    ExtraTreesClassifier
    SVC
    RandomForestClassifier
    KNeighborsClassifier
    BaggingClassifier
    AdaBoostClassifier
    MultinomialNB
    GradientBoostingClassifier
    GaussianNB
    BernoulliNB
    ComplementNB

In our analysis our best model is ExtraTreesClassifier with accuracy 99.68% .

## kaggle notebook link
```bash 
https://www.kaggle.com/code/azizashfak/spam-sms-classification-using-nlp
```

## Installation
1. Clone the repository:
   ```bash
   git clone <https://github.com/aziz-ashfak/Spam-Ham-Detection.git>
   ```
2. Navigate to the project directory:
   ```bash
   cd <Spam-Ham-Detection>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Usage
Run the main application script:
```bash
python app.py
   ```
## Github action pipeline 
``` bash 
  ├── .github
   ├── workflows
       ├── main.yml
```
## use cloud servce 
```bash 
link : www.render.com
```
## Use Spam-Ham-Detection web-service link

```bash
https://spam-ham-detection-0jsh.onrender.com/
```
## Contributing
If you would like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the [LICENSE] file included in the repository.

## Author

👤 **Aziz Ashfak**  
📧 Email: [azizashfak@gmail.com](mailto:azizashfak@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/aziz-ashfak](https://www.linkedin.com/in/aziz-ashfak-/)  
🐙 GitHub: [github.com/aziz-ashfak](https://github.com/aziz-ashfak/)  
