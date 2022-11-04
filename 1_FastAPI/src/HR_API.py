import joblib
import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

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


HR_model = joblib.load("HR_model_trained.sav")


@app.post("/attrition_prediction")
def attrition_pred(input_parameters: model_input):

    # input_data = input_parameters.json()
    # input_dictionary = json.loads(input_data)

    # age = input_dictionary['Age']
    # daylirate = input_dictionary['DailyRate']
    # distancefromhome = input_dictionary['DistanceFromHome']
    # hourlyrate = input_dictionary['HourlyRate']
    # monthlyincome = input_dictionary['MonthlyIncome']
    # monthlyrate = input_dictionary['MonthlyRate']
    # numcompaniesworked = input_dictionary['NumCompaniesWorked']
    # percentsalaryhike = input_dictionary['PercentSalaryHike']
    # totalworkingyears = input_dictionary['TotalWorkingYears']
    # yearsatcompany = input_dictionary['YearsAtCompany']
    # yearsincurrentrole = input_dictionary['YearsInCurrentRole']
    # yearssincelastpromotion = input_dictionary['YearsSinceLastPromotion']
    # yearswithcurrmanager = input_dictionary['YearsWithCurrManager']
    # worklifebalance = input_dictionary['WorkLifeBalance']
    # trainingtimeslastyear = input_dictionary['TrainingTimesLastYear']
    # standardhours = input_dictionary['StandardHours']
    # non_travel = input_dictionary['BusinessTravel_Non_Travel']
    # travel_frequently = input_dictionary['BusinessTravel_Travel_Frequently']
    # travel_rarely = input_dictionary['BusinessTravel_Travel_Rarely']
    # human_resources = input_dictionary['Department_Human_Resources']
    # research_and_development = input_dictionary['Department_Research_and_Development']
    # sales = input_dictionary['Department_Sales']
    # education_field_human_resources = input_dictionary['EducationField_Human_Resources']
    # life_sciences = input_dictionary['EducationField_Life_Sciences']
    # marketing = input_dictionary['EducationField_Marketing']
    # medical = input_dictionary['EducationField_Medical']
    # education_other = input_dictionary['EducationField_Other']
    # technical_degree = input_dictionary['EducationField_Technical_Degree']
    # female = input_dictionary['Gender_Female']
    # male = input_dictionary['Gender_Male']
    # healthcare_rep = input_dictionary['JobRole_Healthcare_Representative']
    # jr_human_resoures = input_dictionary['JobRole_Human_Resources']
    # laboratory_technician = input_dictionary['JobRole_Laboratory_Technician']
    # manager = input_dictionary['JobRole_Manager']
    # manufacturingdirector = input_dictionary['JobRole_Manufacturing_Director']
    # researchdirector = input_dictionary['JobRole_Research_Director']
    # researchscientist = input_dictionary['JobRole_Research_Scientist']
    # salesexecutive = input_dictionary['JobRole_Sales_Executive']
    # salesrepresentative = input_dictionary['JobRole_Sales_Representative']
    # divorced = input_dictionary['MaritalStatus_Divorced']
    # married = input_dictionary['MaritalStatus_Married']
    # single = input_dictionary['MaritalStatus_Single']
    # overtimeno = input_dictionary['OverTime_No']
    # overtimeyes = input_dictionary['OverTime_Yes']

    # input_list = [age, daylirate, distancefromhome, hourlyrate, monthlyincome, monthlyrate,
    #               numcompaniesworked, percentsalaryhike, totalworkingyears, yearsatcompany, yearsincurrentrole,
    #               yearssincelastpromotion, yearswithcurrmanager, worklifebalance, trainingtimeslastyear,
    #               standardhours, non_travel, travel_frequently, travel_rarely, human_resources, research_and_development,
    #               sales, education_field_human_resources, life_sciences, marketing, medical,
    #               education_other, technical_degree, female, male, healthcare_rep, jr_human_resoures,
    #               laboratory_technician, manager, manufacturingdirector, researchdirector,
    #               researchscientist, salesexecutive, salesrepresentative, divorced, married,
    #               single, overtimeno, overtimeyes]

    # prediction = HR_model.predict([input_list])
    data_dict = {k: [v] for (k, v) in input_parameters.dict().items()}
    data_df = pd.DataFrame.from_dict(data_dict)
    data_df.rename(columns=col_rename, inplace=True)

    prediction = HR_model.predict(data_df)

    if prediction[0] == 0:
        msg = "The Person is not thinking of leaving the company"
    else:
        msg = "The Employee is not happy with its current situation."

    return {prediction: prediction[0], msg: msg}


if __name__ == "__main__":
    uvicorn.run(app="HR_API:app", port=5000, debug=True, reload=True)
