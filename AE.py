import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

THRESH_1 = 25
BRACKET_1 = 1.750

THRESH_2 = 50
BRACKET_2 = 2.250

THRESH_3 = 75
BRACKET_3 = 2.750

THRESH_4 = 85
BRACKET_4 = 5

THRESH_5 = 95
BRACKET_5 = 6

BRACKET_6 = 10


def get_salary(hours_worked):
    if 0 <= hours_worked <= THRESH_1:
        return hours_worked * BRACKET_1
    elif THRESH_1 < hours_worked <= THRESH_2:
        return (THRESH_1 * BRACKET_1) + ((hours_worked - THRESH_1) * BRACKET_2)
    elif THRESH_2 < hours_worked <= THRESH_3:
        return (THRESH_1 * BRACKET_1) + ((THRESH_2 - THRESH_1) * BRACKET_2) + ((hours_worked - THRESH_2) * BRACKET_3)
    elif THRESH_3 < hours_worked <= THRESH_4:
        return (THRESH_1 * BRACKET_1) + ((THRESH_2 - THRESH_1) * BRACKET_2) + ((THRESH_3 - THRESH_2) * BRACKET_3) + ((hours_worked - THRESH_3) * BRACKET_4)
    elif THRESH_4 < hours_worked <= THRESH_5:
        return (THRESH_1 * BRACKET_1) + ((THRESH_2 - THRESH_1) * BRACKET_2) + ((THRESH_3 - THRESH_2) * BRACKET_3) + ((THRESH_4 - THRESH_3) * BRACKET_4) + ((hours_worked - THRESH_4) * BRACKET_5)
    elif hours_worked > THRESH_5:
        return (THRESH_1 * BRACKET_1) + ((THRESH_2 - THRESH_1) * BRACKET_2) + ((THRESH_3 - THRESH_2) * BRACKET_3) + ((THRESH_4 - THRESH_3) * BRACKET_4) + ((THRESH_5 - THRESH_4) * BRACKET_5) + ((hours_worked - THRESH_5) * BRACKET_6)
    

def get_total_salary(hours_worked, night_hours, sales = 0):
    return get_salary(hours_worked) + (night_hours * 7) + 315

hour_list = [n for n in range(121)]
df = pd.DataFrame({
    "Hours": hour_list
})

df['Salary'] = df['Hours'].apply(get_salary)
df['Total Salary'] = df['Salary'] + 315


st.title("AE Calculator!!")
col1, col2 = st.columns(2)
with col1:
    hours = st.number_input(
        "Insert hours", value=80, max_value=120, min_value=20
    )
with col2: 
    night_flights = st.number_input(
        "Night Flights", value = 0, min_value=0
    )
    

st.metric(label="Total", value=f"{(get_total_salary(hours, night_flights, sales=0)):.3f} KWD")

fig = plt.figure(figsize=(12,7))    
sns.lineplot(data=df, x = 'Hours', y='Total Salary')
st.pyplot(fig)

with st.expander("Table"):
    st.dataframe(df.loc[::10], hide_index=True)
    
