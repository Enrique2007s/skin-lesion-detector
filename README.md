# Skin Lesion Detector (Machine Learning Project)

Skin Lesion Detector is a Data Science and Machine Learning project with the aim of distinguishing between benign and malignant skin lesions, specifically melanoma. The project consists of a binary classification (or more specifically, a Convolutional Neural Network) that can be used to predict whether a skin lesion is benign or malignant by uploading images to a Streamlit dashboard. The project also includes pages with general information about melanomas, how they are presented, and what was discovered during the exploratory data analysis.

To ensure a functional pipeline, the project includes four Jupyter Notebooks covering the steps committed when cleaning, separating, viewing, and using the dataset of over 10,000 images. This helps other developers using this project to know what has been done and why.

The final goal of the project is to improve the detection of melanoma on the skin, which helps by reducing the burden on healthcare systems, economic costs, and improving patient outcomes. By combining Machine Learning and Data Analysis, this project has the potential to become greater than it is and help other people in need.


## Dataset Content
* The dataset is soruced from [Kaggle](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images).

* The dataset contains over 10,000 images of malignant and benign skin lesions(in total). Each image shows a skin lesion that is classified as benign or malignant.

## Business Requirements
Current dermatological workflows rely heavily on manual visual inspection and dermoscopy for every patient presenting with skin lesions. Given that over 80% of biopsied lesions are benign, hospitals are spending 100-500 USD per screening on procedures that produce no clinical benefit, while simultaneously overwhelming specialist capacity.

This project proposes the implementation of a Machine Learning model inside a platform that acts as a second opinion. They system will analyze the image obtained and will return it labeled with either 'benign' or 'malignant', along with a confidence score. This will reduce unnecessary procedures, lower average screening costs, and accelerate diagnostics for both benign and malignant skin lesions.

The business requirements are as follows:

1-) The client is interested in conducting a study to visually analyze the skin lesions of patients and determine whether they are malignant or benign.

2-) The client is interested in developing a machine learning model that can accurately classify skin lesions as malignant or benign based on images of the lesions.

3-) The client is interested in developing a user-friendly dashboard that allows users to upload images of skin lesions and receive real-time predictions of whether the lesion is likely to be malignant.


## Hypothesis and how to validate?
1-) Skin lesions are all unique in size, shape, colour, and symmetry. However, there are certain patterns and characteristics that can help distinguish between benign and malignant skin lesions. We expect benign lesions to have more regular patterns, more uniform colour, and more symmetrical shapes, while malignant lesions may have more irregular patterns, less uniform colour, and less symmetrical shapes.

We expect the model to be able to learn these patterns and characteristics and use them to accurately classify skin lesions as benign or malignant.

**Validation:** The model achieved an accuracy of 0.81 on the test set, confirming it successfully learned distinguishing patterns. It did amazingly well by identifying benign lesions with a recall of 99. However, it struggled with malignant lesions, achieving a recall score of 0.61. This confirms the hypothesis that malignant patterns are more difficult to learn due to their nature in irregularity.

2-) The implementation of the model can reduce melanoma-related deaths by making skin lesion screening more accessible, easy-to-use efficient, and widely available. 

**Validation:** By making the model more accessible to hospitals, skin lesion screening can serve as an automated tool, quickly flagging whether the patient has a benign skin lesion or a malignant skin lesion. Specialists will then be able to focus on patients flagged as malignant or have aggressive forms of melanoma.

3-) The implementation of the model can reduce the number of unnecessary biopsies on benign skin lesions, thereby reducing the burden on healthcare systems, economic costs, and improving patient outcomes.

**Validation:** The model demonstrates exceptional capability in ruling out benign lesions, correctly identifying 1,085 out of 1,101 cases. This means that the model can confidently clear the vast majority of harmless skin lesions. In other words, acting like a filter. By flagging only 16 cases as suspicious, the model could reduce the number of unnecessary cancer screenings performed on non-cancerous lesions. This leads to lower healthcare costs, reduced workloads, and better patient quality of life by avoiding unnecessary procedures.

## The rationale to map the business requirements to the Data Visualizations and ML tasks
* First Business Requirement:
  - As a dermatologist, I want to be able to view a montage of the images used to train the model so I can trust it more. (Skin Lesion visualizer Page)
  - As a client, I can view the average image of benign and malignant skin lesions so I can understand the differences between them. (Skin Lesion Visualizer Page)
  - As a client, I want to learn the general differences between the benign and malignant skin lesions so I can be better informed about melanoma. (Skin Lesion Visualizer Page)

* Second Business Requirement:
  - As a dermatologist, I want to be able to upload an image of a skin lesion and receive the model's opinion on whether it is malignant of benign along with a confidence score. (Skin Lesion Detector Page)
  - As a dermatologist, I want to use sample images to test the model so I can understand its predictions more in-depth. (Skin Lesion Detector Page)
  - As a patient, I want the model to be right so I don't get scared! (model performance metrics Page)
  - As a client, I want a dashboard that is easy to understand and use so I don't get confused. (Instructions and Summary Pages)
 
* Third Business Requirement:
  - As a hospital Administrator, I want to see the overall performance metrics so I can evaluate its clinical utility. (Model Performance Metrics Page)
  - As a researcher, I want to view the classification report to understand the model's precision, recall, and F1-scores for each class. (Model Performance Metrics Page)
  - As a dermatologist, I want to view the model's confusion matrix to understand the model's mistakes and what I need to keep an eye out for. (Model Performance Page)


## ML Business Case
* The goal is to develop a Machine Learning tool that can efficiently and accurately detect if a skin lesion if malignant or benign, thus lowering laboratory workload and price of skin cancer screening.
* The dataset provided by the customer will be used to train the ML tool, and the expected output of said tool is to be able to tell which is benign and which is malignant.
* The model might not do as well predicting benign vs malignant if there is a very dark skin tone.
* The success of the ML tool will be measured by:
  - Accuracy: Achieving at least 80% accuracy on the test dataset.
  - Efficiency: Reducing the time and cost associated with manual inspection processes.
  - Usability: Providing a user-friendly dashboard for quick image uploading and predictions.
  - Trust: Providing visual explanations(montages, average images) to build clinician confidence.

* Extension oportunities:
  - Treatment Monitoring: The ML tool can be extended to monitor changes during treatment to know whether it is working or not.
  - Different Applications: The CNN model architecture no one sees can be retrained to detect other skin conditions.

* Model Success Criteria
  - Visual Difference: A study showing how to visually differentiate a benign lesion from one via average images and montages.
  - Predictive Capability: The capability to predict if a skin lesion is benign or malignant with a confidence score.
  - Accuracy Target: The model achieved an overall accuracy of 81% on the test data. This can be optimized to potentially reach 90% in future iterations.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## CRISP-DM
The CRISP-DM (or Cross Industry Standard Process for Data Mining) is a framework used for guiding Data Science and Machine Learning projects in the real world. It is the most popular and widely used methodology for analytics, data mining, and data science projects.

Business Understanding: The goal of the project was to develop a model that could differentiate between malignant and benign skin lesions. It is meant to help hospitals(specifically dermatologists) to detect melanoma much faster and decrease the costs of skin cancer screening.

Data Understanding: The dataset was obtained from Kaggle, from a dataset called "Melanoma Skin Cancer Dataset of 10000 Images" by Muhammad Hasnain Javid. It has a total of 10,000+ images.

Data Preparation: The data originally came in two files, so the data was split into three. Training, Validating, and Testing. After this, all files that were corrupted or not png/jpg were removed. Images already were consistent in pixel size and color, so there was no need to change it.

Modeling: A CNN (Convolutional Neural Network) was chosen, as they are one of the best ways to train a model using images because they are great at finding patterns like edges and fine textures. The model was developed using Tensorflow and Keras.

Evaluation: The model was evaluated using various metrics such as accuracy, precision, recall, F1-score, a classification report, a confusion matrix, and model training losses.

Deployment: The final model was placed in a Streamlit Dashboard that allows users to upload images and receive real time predictions on whether it is malignant or not, along with a confidence score. 

## Dashboard Design

#### The Instructions Page:
This page provides a summary of each page, along with instructions to use the Melanoma Detector. It also discloses that this ML model should under no circumstance be replaced for a qualified healthcare provider.
<img width="1036" height="868" alt="image" src="https://github.com/user-attachments/assets/888eb9a3-6a67-4391-ba7e-76035c6820a4" />


#### The Summary Page:
This page provides a summary of what melanoma is, where the dataset was obtained from, additional information that can be trusted, business requirements, objectives, and the general process of how the ML pipeline was developed. This is helpful to the users so they know what this project is and what questions it answers, such as "is there a difference between malignant and benign skin lesions.

<img width="1002" height="866" alt="image" src="https://github.com/user-attachments/assets/17d9416f-0457-4714-a4fa-fcf951a10c5b" />
<img width="1000" height="484" alt="image" src="https://github.com/user-attachments/assets/d6d48650-1c1a-46fe-8e48-691894f7b98f" />

#### The Skin Lesion Visualizer Page:
The skin lesion visualizer page is where all the montages and images of benign and malignant images are. It also contains a section below the interactive checkboxes where users can learn the differences beteen benign and malignant lesions. Each checkbox works and all images show up as intended.
<img width="1003" height="745" alt="image" src="https://github.com/user-attachments/assets/dfadb979-587f-46b3-bdeb-ee2f19e3a1dd" />

#### Skin Lesion Detector
The skin lesion detector page is where the model lives. Here, the user is able to upload an image of a skin lesion and receive the model's educated opinion on whether it is malignant or not. Apart from that, the user also receives a confidence score represented as a bar chart. There is also a link directing the user to a series of images that can be tested on the model. The user must make sure to put the melanoma images in, as the model is not trained with other kind of malignant skin lesions and will give biased/incorrect predictions.
<img width="1011" height="751" alt="image" src="https://github.com/user-attachments/assets/3418cf30-3af5-41d0-b0e4-3934ef3db1a8" />
<img width="1015" height="384" alt="image" src="https://github.com/user-attachments/assets/c4fc5dd0-23e9-4030-942f-f425994e63c1" />

#### Project Hypothesis:
The project hypothesis page contains the hypotheses, conclusions, and future improvements. This helps users understand part of the purpose of the project, as well to inform other people, such as clinicians or data analysts, what possible improvements can be made to the model.
<img width="1007" height="823" alt="image" src="https://github.com/user-attachments/assets/6d9b7263-c60e-4921-ad75-c4466d4b8122" />
<img width="1004" height="592" alt="image" src="https://github.com/user-attachments/assets/5554a2b7-e0a0-42d3-b06a-4287665feaa2" />

#### Model Performance:
In the model performance page, users will be able to see how well the model performed and the explanations of each plot shown. This is useful to Data Analysts because when it is their turn to improve the model, they will already not only have something to work on, but will also be able to perform the necessary tests to make sure their model outperforms the previous one.
<img width="1008" height="762" alt="image" src="https://github.com/user-attachments/assets/8c5e936e-361c-4670-a67c-00e809cdf9a0" />
<img width="1010" height="407" alt="image" src="https://github.com/user-attachments/assets/b0e88f2f-c519-4f69-9e59-f57dbc2443cb" />
<img width="1006" height="773" alt="image" src="https://github.com/user-attachments/assets/7ca9b79a-e6c9-4ca0-b3f9-7d9593cfaac1" />
<img width="1017" height="848" alt="image" src="https://github.com/user-attachments/assets/c308e6d9-3ffc-4f3f-8468-ad84a0085cb9" />
<img width="1004" height="823" alt="image" src="https://github.com/user-attachments/assets/97d11924-f258-42f9-8572-19bff38f2147" />
<img width="1010" height="594" alt="image" src="https://github.com/user-attachments/assets/2ee6e224-47c7-4f88-b539-9752e903a0e4" />
<img width="1013" height="832" alt="image" src="https://github.com/user-attachments/assets/3fc511a3-269b-4c41-8a0b-4c221901c692" />
<img width="981" height="846" alt="image" src="https://github.com/user-attachments/assets/d07e5cd2-8000-44cb-8b86-da8021693bbf" />

## Machine Learning Model Justification

#### Architecture of the model

The model is a CNN(Convolutional Neural Network) designed of binary classification (benign vs malignant) skin lesions. the architecture consists of fours convolutional blocks, followed by a global average pooling layer, a dense classifier head, and a final sigmoid output layer.
The network inputs images of size (224x223x3)(RGB) and outputs a probability between 0 and 1, representing the likelihood of the lesion being malignant.

* Design Choices:

Progressive Filter Increase: The number of filters doubles from 16 to 32 to 64. This is a common design patters in that allows early layers to detect simple features such as edges, textures, and colors(which is really helpful in this case). 

3x3 Convolutional Kernels: Using small 3x3 kernels is normal in modern CNN models. 

Same Padding: Padding = 'same' ensures the spatial dimensions of the feature maps remain consistent after each convolution, preserving spatial information through the network.

Batch Normalization: This is applied before and after each convolutional layer. This accelerates training by normalizing the inputs to each layer.

ReLU Activation: Helps mitigate vanishing gradient problem with deep networks.

MaxPooling: Each convolutional block is followed by a 2x2 Maxpooling layer. This decreases the number of parameters and computational load while makin the model more robust to small changes in the input images.

Progressive dropout: The progressive dropout rate increases the further the model learns. This prevents overfitting by randomly droppig neurons during training. They become highe in deeper layers because they contian more complex and task specific features that are prone to overfitting.

L2 Regularization(WeightDecay): A;; conv. and dense layers use L2 regularization with a factor of 5x10^-4/ This penalizes large weights and encourages the model to learn simpler and more generalizable features. Combined with dropout, L2 Reg. prevents overfitting quite nicely, which is needed for medical datasets.

* Optimizer and Loss Function:
Optimizer: Adam with a fixed learning rate of 1x10^-3
loss function: Binary Cross-Entropy, which is the standard for binary classification models
Metrics: Accuracy, which is used to monitor performance during training

#### Model Summary:
<img width="539" height="976" alt="image" src="https://github.com/user-attachments/assets/31834e12-b821-4113-a774-d928f7175f7a" />


## Unfixed Bugs
* No unfixed bugs. However, model performance could have been better if hyperparameter optimization was added to the project.

## Deployment
### Heroku

* The App live link is: [https://YOUR_APP_NAME.herokuapp.com/ ](https://skin-lesion-detector-d087d703e2d2.herokuapp.com/)
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.
joblib
keras
matplotlib
numpy
pandas
pillow
plotly
scikit-learn
seaborn
tensorflow
streamlit
altair

## Credits 

* Dataset: [Kaggle Dataset](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images)
  
* helping videos and information for melanoma cancer information:
  - [How much skin cancer screening costs](https://www.goodrx.com/conditions/skin-cancer/skin-cancer-screening-cost?srsltid=AfmBOoqWdySiClqBRJmTx8iOJqa_Pk9e4ZLXaAUM99NA4laO1DAJfto4)
  - [Economic burden of skin cancer in the USA](https://pmc.ncbi.nlm.nih.gov/articles/PMC11001479/)
  - [Analytics Vidhya](https://www.youtube.com/live/Vb7g3N-NNuM?si=ewqX0VFwAWyipXPC)
  - [series of videos about deep learning](https://youtu.be/aircAruvnKk?si=B3vR-CTtbuX2IoiQ)

 DeepSeek: An amazing tool not only for learning, but also for resolving problems when deploying locally and on Heroku.
 Emmett: Integrated AI in the codespace. Used for logic cleaning and speeding up the creating of plots with suggestions.
 - [Numpy](https://numpy.org/doc/) 
 - [Pandas](https://pandas.pydata.org/docs/)
 - [Matplotlib](https://matplotlib.org/stable/)
 - [Seaborn](https://seaborn.pydata.org/)
 - [Plotly](https://plotly.com/python/)
 - [TensorFlow](https://www.tensorflow.org/)
 - [Keras](https://keras.io/)
 - [Scikit-learn](https://scikit-learn.org/stable/)
 - [Streamlit](https://docs.streamlit.io/)
 - [Github Codespaces](https://github.com/features/codespaces)
 - [Git/GitHub](https://git-scm.com/docs)
 - Some code cells were used as reference from the walkthrough project for detecting malaria inside cells. It really helped me know what I had to do after each step and helped me understand how to develop code that saves models, saves plots, and how to work with a Streamlit Dashboard

No images apart form the dataset and testing images in the melanoma detector page were used.



## Acknowledgements (optional)
* I would like to thank Marcel, my mentor, for helping me develop the end stages of my project. He was very informative and we had a great conversation.
* I would like to thank the person who created this [project](https://github.com/oks-erm/ML-mildew-detection). I guided myself off this project for the readme and end stages of the project.
* I would like to thank Marko, my facilitator who helped me get in contact with my mentor and encouraged me in my final months as as Student in Code Institute
* Lastly, I want to thank my amazing parents. They have supported me throughout the whole way and have given me various suggestions for this project.
