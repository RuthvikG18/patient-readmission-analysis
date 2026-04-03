import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def set_style():
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['figure.figsize'] = (10, 6)

def plot_readmission_distribution(df, save_path=None):
    counts = df['readmitted'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=counts.index, y=counts.values, ax=ax)
    ax.set_title('Patient Readmission Distribution')
    ax.set_xlabel('Readmission Status')
    ax.set_ylabel('Number of Patients')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_age_vs_readmission(df, save_path=None):
    age_read = df.groupby('age')['readmitted_binary'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=age_read, x='age', y='readmitted_binary', ax=ax)
    ax.set_title('30-Day Readmission Rate by Age Group')
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Readmission Rate')
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_top_diagnoses(df, save_path=None):
    readmitted = df[df['readmitted_binary'] == 1]
    top_diag = readmitted['diag_1'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_diag.values, y=top_diag.index, ax=ax, orient='h')
    ax.set_title('Top 10 Primary Diagnoses in Readmitted Patients')
    ax.set_xlabel('Count')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_time_in_hospital(df, save_path=None):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='readmitted', y='time_in_hospital', ax=ax)
    ax.set_title('Hospital Stay Duration vs Readmission Status')
    ax.set_xlabel('Readmission')
    ax.set_ylabel('Days in Hospital')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_medications_heatmap(df, save_path=None):
    med_cols = ['metformin', 'insulin', 'glipizide', 'glyburide', 'pioglitazone']
    mapping = {'No': 0, 'Steady': 1, 'Up': 2, 'Down': 3}
    med_df = df[med_cols].replace(mapping).apply(pd.to_numeric, errors='coerce')
    fig, ax = plt.subplots()
    sns.heatmap(med_df.corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Medication Usage Correlation')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()