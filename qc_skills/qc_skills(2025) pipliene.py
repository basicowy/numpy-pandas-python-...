#%%
from idlelib.editor import darwin

#Loading data as .csv file
#Creating pandas data_frame based on loaded .csv file
import kagglehub
import pandas as pd
from os import listdir, path
path_to_the_data = kagglehub.dataset_download("ahsanneural/future-jobs-and-skills-demand-2025")
files = listdir(path_to_the_data)
true_path = path.join(path_to_the_data, files[0])
data_frame = pd.read_csv(true_path)
#%%
#First look at our data_frame
data_frame.head()
#%%
#I'm extracting only data that is interesting for me, in this case I leave only rows that poses information about Quantum Computing industry
qc_info_df = data_frame.loc[data_frame["industry"] == "Quantum Computing",["industry","skills_required"]]
#I don't need rows where industry or skills_requried is nan so I drop them
qc_info_df = qc_info_df.dropna(subset=["industry","skills_required"])
#I would like to know which skill is most required skill for position in Quantum Computing industry so I need to split every row on two rows
qc_info_df["skills_required"] = qc_info_df["skills_required"].apply( lambda x : [i.lower().strip() for i in x.split(',')])
qc_info_df = qc_info_df.explode("skills_required").reset_index(drop=True)
qc_info_df.head()

#%%
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x="skills_required",data=qc_info_df,kind="count",hue="skills_required")
plt.title("Quantum Computing Skills")
plt.tight_layout()
plt.show()