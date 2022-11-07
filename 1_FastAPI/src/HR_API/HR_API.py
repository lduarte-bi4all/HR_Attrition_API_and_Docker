from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

# Load the instance of FastAPI into a variable called an APP.
app = FastAPI()


class model_input(BaseModel):

    Age: float
    DailyRate: float
    DistanceFromHome: float
    HourlyRate: float
    MonthlyIncome: float
    MonthlyRate: float
    NumCompaniesWorked: float
    PercentSalaryHike: float
    TotalWorkingYears: float
    YearsAtCompany: float
    YearsInCurrentRole: float
    YearsSinceLastPromotion: float
    YearsWithCurrManager: float
    WorkLifeBalance: float
    TrainingTimesLastYear: float
    StandardHours: int
    BusinessTravel_Non_Travel: int
    BusinessTravel_Travel_Frequently: int
    BusinessTravel_Travel_Rarely: int
    Department_Human_Resources: int
    Department_Research_and_Development: int
    Department_Sales: int
    EducationField_Human_Resources: int
    EducationField_Life_Sciences: int
    EducationField_Marketing: int
    EducationField_Medical: int
    EducationField_Other: int
    EducationField_Technical_Degree: int
    Gender_Female: int
    Gender_Male: int
    JobRole_Healthcare_Representative: int
    JobRole_Human_Resources: int
    JobRole_Laboratory_Technician: int
    JobRole_Manager: int
    JobRole_Manufacturing_Director: int
    JobRole_Research_Director: int
    JobRole_Research_Scientist: int
    JobRole_Sales_Executive: int
    JobRole_Sales_Representative: int
    MaritalStatus_Divorced: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    OverTime_No: int
    OverTime_Yes: int


col_rename = {
    "BusinessTravel_Non_Travel": "BusinessTravel_Non-Travel",
    "Department_Human_Resources": "Department_Human Resources",
    "Department_Research_and_Development": "Department_Research & Development",
    "EducationField_Human_Resources": "EducationField_Human Resources",
    "EducationField_Life_Sciences": "EducationField_Life Sciences",
    "EducationField_Technical_Degree": "EducationField_Technical Degree",
    "JobRole_Healthcare_Representative": "JobRole_Healthcare Representative",
    "JobRole_Human_Resources": "JobRole_Human Resources",
    "JobRole_Laboratory_Technician": "JobRole_Laboratory Technician",
    "JobRole_Manufacturing_Director": "JobRole_Manufacturing Director",
    "JobRole_Research_Director": "JobRole_Research Director",
    "JobRole_Research_Scientist": "JobRole_Research Scientist",
    "JobRole_Sales_Executive": "JobRole_Sales Executive",
    "JobRole_Sales_Representative": "JobRole_Sales Representative",
}

HR_model = joblib.load("HR_model_load.sav")


@app.post("/attrition_prediction")
def attrition_pred(input_parameters: model_input):
    print("here")
    data_dict = {k: [v] for (k, v) in input_parameters.dict().items()}
    data_df = pd.DataFrame.from_dict(data_dict)
    data_df.rename(columns=col_rename, inplace=True)

    prediction = HR_model.predict(data_df)

    if prediction[0] == 0:
        msg = "The Person is not thinking of leaving the company"
    else:
        msg = "The Employee is not happy with its current situation."

    return msg


if __name__ == "__main__":
    uvicorn.run(app="HR_API:app", port=5000, reload=True)
