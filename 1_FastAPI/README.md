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
You can learn about it in this [Red Had Article](https://www.redhat.com/en/topics/api/what-is-a-rest-api), but it is basically an API that obeys to the REST set of architectural constraints. Which means it is a client-server communication where no information is stored between requests and the interface is uniform in both sides, making it easily usable for clients with useful resources and self-descriptive messages.
___
### What's the difference between GET and POST methods?
*GET* and *POST* are *HTTP(HyperText Transfer Protocol)* request methods. In general, *GET* is used to get data from a specified source, and *POST* to send data in order to create or update resources.

The use cases are sometimes similar, but there are differences between them. For instance, in *POST* the data is confidential (hidden because is passed inside the body of the request) and doesn't have a length limitation(handles large amounts of data), while in GET small data information is passed on the headers.

Follow [this link](https://www.scaler.com/topics/difference-between-get-and-post/) to have a better overview of this topic and spot the request differences [here](https://www.geeksforgeeks.org/difference-between-get-and-post-request-in-vanilla-javascript/).

# Install Postman API platform ![][def]

[def]: postman.png

