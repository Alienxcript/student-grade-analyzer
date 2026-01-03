#analyzer for the students performance 
import pandas as pd 

def analyze_students_score(input_csv, output_csv="finalized_results.csv"):
    df = pd.read_csv(input_csv)

    score_cols = ["math score", "reading score", "writing score"]

    #total and average
    df["total_score"] = df[score_cols].sum(axis=1)
    df["average_score"] = df[score_cols].mean(axis=1)

    #assign the grades using another function 
    def grade_assign(avg):
        if avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"
        
    df["grade"] = df["average_score"].apply(grade_assign)

    #student rankings
    df["rank"] = df["average_score"].rank(ascending=False, method="min").astype(int)

    #sort rank
    df.sort_values("rank").head()

    #save results
    df.to_csv(output_csv, index=False)

    return df




if __name__ == "__main__":
    analyze_students_score("StudentsPerformance.csv")