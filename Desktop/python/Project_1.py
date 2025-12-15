import pandas as pd
import matplotlib as plt 
import logging

logging.basicConfig(filename = 'error log',level = logging.ERROR)

def load_data(file_paths):
    dfs = []
    for file_path in file_paths:
        try:
            file = pd.read_csv("C:/Users/HP USERS/Desktop/python/sensor_dataset.csv")
            dfs.append(file)
        except Exception as e:
            logging.error(f"Error loading {file_path}: {str(e)}")
    if not dfs:
        logging.error("No data loaded !")
        return None
    return pd.concat(dfs, ignore_index = True)
    
def clean_data(file):
    try:
        file = file.dropna()
        return file
    except Exception as e:
        logging.error(f"Error cleaning data: {str(e)} ")
        return None

def analysis(file):
    try:
        mean = file.mean(numeric_only = True)
        median = file.median(numeric_only = True)
        std = file.std(numeric_only = True)
        results = {"mean" : mean, "median" : median, "std" : std}
    except Exception as e:
        logging.error(f"Error in  performing Analysis: {str(e)}")
        return None
        # min = file.min(numeric_only = True)
        # max = file.max(numeric_only = True)

def visualizations(file):
    try:
        for column in file.select_dtypes(include = ['int64', 'float64']).columns:
            plt.hist(file[column], bins = 10)
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequemcy")
            plt.savefig(f"{column}_Histogram.png")
            plt.close()
    except Exception as e:
        logging.error(f"Error in generating visuals: {str(e)}")
        
def report(results, file_paths):
    try:
        with open(file_paths, "w") as f:
            for key, values in results.items():
                f.write(f"{key}:{values}\n")
    except Exception as e:
        logging.error(f"Error in writing report: {str(e)}")


def main():
    file_paths = ["C:/Users/HP USERS/Desktop/python/sensor_dataset.csv"]
    file = load_data(file_paths)
    if file is not None:
        file = clean_data(file)
    if file is not None:
        results = analysis(file)
        if results:
            visualizations()
            report(results, "analysis_report.txt")
            print("Analysis Complete ! Report and visualizations generated. ")
            
if __name__== "_main_":
    main()


    
    

        
           

























































# import pandas as pd
# def upload():
#     file = pd.read_csv
#     ("C:/Users/HP USERS/Desktop/python/sensor_dataset.csv")
#     return file

# # print(file.head(2))
# # upload()
# def clean_data(file):
#     file_clean = file.dropna()
#     print(file.isna().sum())
#     return file_clean

# # file = pd.read_csv("C:/Users/HP USERS/Desktop/python/sensor_dataset.csv")  
# # file.dropna()
# # clean_data(file)
# def analyse_data(file):
#     result = {
#         "mean" : file.mean(numeric_only = True).to_dict(),
#         "min" : file.min(numeric_only = True).to_dict(),
#         "max" : file.max(numeric_only = True).to_dict(),
#         "std" : file.std(numeric_only = True).to_dict()
#         }
#     return result

# def visualize_data(file):
#     file.hist(fgsize = (10, 8))
#     plt.tight_layout()
#     plt.savefig("visualisation.png")

# def report(result):
#     with open("Rapport.txt", "w") as f:
#         for stat, values in result.items():
#             f.write(f"\n --- {stat.upper()} ---\n")
#         for i, v in values.items():
#             f.write(f"{i}:{v}\n")
                                 

    