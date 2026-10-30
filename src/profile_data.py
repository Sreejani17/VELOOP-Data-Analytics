from pathlib import Path
import argparse
import pandas as pd

def load_files(folder):
    for path in sorted(folder.glob("*")):
        if path.suffix.lower() == ".csv":
            yield path.stem, pd.read_csv(path, dtype="string", keep_default_na=True)
        elif path.suffix.lower() in {".xlsx", ".xls"}:
            book = pd.read_excel(path, sheet_name=None, dtype="string")
            for sheet, df in book.items():
                yield f"{path.stem}_{sheet}", df

def main():
    parser=argparse.ArgumentParser(description="Profile CSV and Excel datasets.")
    parser.add_argument("--input",default="data/sample")
    parser.add_argument("--output",default="reports/generated")
    args=parser.parse_args()
    inp=Path(args.input); out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    inventory=[]; missing_rows=[]; category_rows=[]; numeric_rows=[]; date_rows=[]
    for name, df in load_files(inp):
        dup=int(df.duplicated().sum())
        inventory.append({"dataset":name,"rows":len(df),"columns":len(df.columns),"duplicate_rows":dup,
                          "missing_cells":int(df.isna().sum().sum()),"fields":", ".join(map(str,df.columns))})
        for col in df.columns:
            n=int(df[col].isna().sum())
            if n: missing_rows.append({"dataset":name,"field":col,"missing_count":n,"missing_pct":round(n/max(len(df),1)*100,2)})
            s=df[col].dropna().astype(str)
            if 0 < s.nunique() <= 30:
                for val,count in s.value_counts().head(30).items():
                    category_rows.append({"dataset":name,"field":col,"value":val,"count":int(count)})
            if any(x in col.lower() for x in ["date","time","timestamp","_at"]):
                parsed=pd.to_datetime(df[col],errors="coerce",utc=True)
                valid=parsed.dropna()
                date_rows.append({"dataset":name,"field":col,"valid_dates":int(valid.size),"invalid_dates":int(parsed.isna().sum()),
                                  "min_utc":str(valid.min()) if len(valid) else "","max_utc":str(valid.max()) if len(valid) else ""})
            if any(x in col.lower() for x in ["amount","points","value","seconds","duration"]):
                num=pd.to_numeric(df[col],errors="coerce")
                valid=num.dropna()
                numeric_rows.append({"dataset":name,"field":col,"valid_numeric":int(valid.size),"invalid_numeric":int(num.isna().sum()),
                                      "negative_count":int((valid<0).sum()),"min":float(valid.min()) if len(valid) else None,
                                      "max":float(valid.max()) if len(valid) else None})
    pd.DataFrame(inventory).to_csv(out/"data_inventory.csv",index=False)
    pd.DataFrame(missing_rows).to_csv(out/"missing_values.csv",index=False)
    pd.DataFrame(category_rows).to_csv(out/"category_profiles.csv",index=False)
    pd.DataFrame(date_rows).to_csv(out/"date_profiles.csv",index=False)
    pd.DataFrame(numeric_rows).to_csv(out/"numeric_profiles.csv",index=False)
    print(f"Profiling complete. Reports: {out.resolve()}")
if __name__=="__main__": main()
