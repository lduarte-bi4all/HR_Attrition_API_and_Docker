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

You can check more examples on [this link](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/). There you will also see an example using **Pickle**, which is one of the most popular ways to serealize objects in Python. 

**Joblib** is an alternative to Pickle. It's part of Scipy's ecosystem and is more efficient on objects that carry large Numpy arrays. Learn more about its vantages in this [stackoverflow discussion](https://stackoverflow.com/questions/12615525/what-are-the-different-use-cases-of-joblib-versus-pickle#:~:text=joblib%20is%20usually,zlib%20or%20lz4.).