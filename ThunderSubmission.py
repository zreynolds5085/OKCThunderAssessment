import pandas as pd
import numpy as np

def calculateTeamStats(df):
    df['distance'] = np.sqrt(df['x']**2 + df['y']**2)
    
    total_FGA = len(df)
    
    df_C3 = df[(abs(df["x"]) > 22) & (df["y"] <= 7.8)]
    df_NC3 = df[(df["distance"] > 23.75) & (df["y"] > 7.8)]
    df_2PT = df[(df["distance"] < 23.75) & (abs(df["x"]) < 22)]
    
    p_C3 = str(round((df_C3.shape[0]/total_FGA)*100, 3))
    p_NC3 = str(round((df_NC3.shape[0]/total_FGA)*100, 3))
    p_2PT = str(round((df_2PT.shape[0]/total_FGA)*100, 3))
    
    sd = {"Corner 3": p_C3 + '%', "Non Corner 3": p_NC3 + '%', "Two Point": p_2PT + '%'}
    
    n_FGA_C3 = df_C3.shape[0]
    n_FGA_NC3 = df_NC3.shape[0]
    n_FGA_2PT = df_2PT.shape[0]
    
    n_FGM_C3 = len(df_C3[df_C3['fgmade'] == 1])
    n_FGM_NC3 = len(df_NC3[df_NC3['fgmade'] == 1])
    n_FGM_2PT = len(df_2PT[df_2PT['fgmade'] == 1])
    
    p_eFG_C3 = str(round(((n_FGM_C3 + .5 * n_FGM_C3) / n_FGA_C3) * 100, 3))
    p_eFG_NC3 = str(round(((n_FGM_NC3 + .5 * n_FGM_NC3) / n_FGA_NC3) * 100, 3))
    p_eFG_2PT = str(round((n_FGM_2PT / n_FGA_2PT) * 100, 3))
    
    eFG = {"Corner 3": p_eFG_C3 + '%', "Non Corner 3": p_eFG_NC3 + '%', "Two Point": p_eFG_2PT + '%'}
    
    print('Shot Distribution: ' + str(sd))
    print('eFG%: ' + str(eFG))
    

df = pd.read_csv("shots_data.csv")

dfA = df[df["team"] == "Team A"]
dfB = df[df["team"] == "Team B"]

print("Team A\n")

calculateTeamStats(dfA)

print("\nTeam B\n")

calculateTeamStats(dfB)