# Saving Your Model
Open yout jupyter notebook where you developed the HR Attrition model, and follow the next steps, adding them to the end of the document.

After developing your model you wan't to save it. Lets do it using `joblib`.
```
import joblib
```
The next cell will create a file for your model and save it in the local working directory.
```
filename = 'HR_model_finalized.sav'
joblib.dump(lr_model, filename)
```
Now you can load the model whenever you want in other files. Let's confirm creating a new variable and comparing results.
```
lr_model_copy = joblib.load('HR_model_finalized.sav') #create a copy
y_preds_copy = lr_model_copy.predict(X_test_scaled) #predict new values
(y_preds == y_preds_copy) #check if both models produce the same results
```

You can check more examples on [this link](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/). There, you will also see an example using **Pickle**, which is one of the most popular ways to serealize objects in Python. 

**Joblib** is an alternative to Pickle. It's part of Scipy's ecosystem and is more efficient on objects that carry large Numpy arrays. Learn more about its advantages in this [stackoverflow discussion](https://stackoverflow.com/questions/12615525/what-are-the-different-use-cases-of-joblib-versus-pickle#:~:text=joblib%20is%20usually,zlib%20or%20lz4.).

# GET and POST methods in REST APIs
These are some concepts you need to be aware of. 
___
### Firstly, what is a REST API?
You can learn about it in this [Red Had Article](https://www.redhat.com/en/topics/api/what-is-a-rest-api), but it is basically an API that obeys to the REST set of architectural constraints. Which means it is a client-server communication where no information is stored between requests and the interface is uniform in both sides, making it easily usable for clients, with useful resources and self-descriptive messages.
___
### What's the difference between GET and POST methods?
*GET* and *POST* are *HTTP(HyperText Transfer Protocol)* request methods. In general, *GET* is used to get data from a specified source, and *POST* to send data in order to create or update resources.

The use cases are sometimes similar, but there are differences between them. For instance, in *POST* the data is confidential (hidden because is passed inside the body of the request) and doesn't have a length limitation(handles large amounts of data), while in GET small data information is passed on the headers.

Follow [this link](https://www.scaler.com/topics/difference-between-get-and-post/) to have a better overview of this topic and spot the request differences [here](https://www.geeksforgeeks.org/difference-between-get-and-post-request-in-vanilla-javascript/).

# Create APIs with Postman platform ![](https://user-images.githubusercontent.com/4249709/29496848-63ad446c-85b1-11e7-904e-a4ddad25e9db.png)


**APIs** are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. For example, the weather bureau's software system contains daily weather data. The weather app on your phone “talks” to this system via APIs and shows you daily weather updates on your phone. Learn more with [this article](https://www.redhat.com/en/topics/api/what-are-pplication-programming-interfaces).
___
**Postman** is an API development tool which helps to build, test and modify APIs. Using its simple and user-friendly interface, you can easily send requests, just fill in the required data, select the HTTP method, and hit the “Send” button.

Go to their [website](https://www.postman.com/) and install the Desktop version or try the Web app. After that, watch this [8 minute beginner tutorial](https://www.youtube.com/watch?v=CLG0ha_a0q8) and get to know the platform, sending your first requests.
___
[**FastAPI**](https://fastapi.tiangolo.com/) is a Web framework for developing RESTful APIs in Python. Follow [this article](https://fastapi.tiangolo.com/#create-it) to create your first API using GET method.

# Create API to deploy your ML model using BaseModel

*Pydantic* is a Python library for data modeling/parsing that has efficient error handling and a custom validation mechanism. You can define your data inside a class that inherits from the **BaseModel** class, making sure it conforms to the fields' constraints defined in it. See this [*BaseModel* usage](https://pydantic-docs.helpmanual.io/usage/models/#basic-model-usage).
___
The API must be deployed with a **python** file because everything must run at once without the need of a graphical interface in a container.
___
Follow the next steps to build and test your machine learning model API:

- Load the instance of *FastAPI*
- Define the input needed data using *BaseModel*
- Create a column rename dictionary because of the spaces in some features labels
- Load your model with *joblib*
- Create a POST request
- Turn the input into a dictionary, create a *pandas* dataframe with it and rename the affected columns
- predict the output and inform the user

Try it yourself and then compare it with the solution in `src` folder.

Use *Postman* to try your API following this steps:

- Create a new collection called 'HR_Model'
- Create a new request called 'Input Data'
- Choose **POST** method and paste the request URL
- Go to *Body* and choose *raw* and **JSON**
- Write all the inputs as follows

    `{

        "Age":22.0,
        "DailyRate":1000.0,
        .
        .
        .
    }`
- Send the request and see the response.

# To be improved
In the `HR_Model_Solution.ipynb` file, the model should be dumped along with the encription of the data. At the moment, in the POST request, the user has to fill all the binary entrances representing categorical features.
