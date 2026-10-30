from pathlib import Path
import argparse
import pandas as pd

KEY_CANDIDATES=["user_id","task_activity_id","reward_id","wallet_txn_id","withdrawal_id","referral_id","event_id","record_id"]
DATE_CANDIDATES=["timestamp","_at","date"]
NUMERIC_CANDIDATES=["amount","points","reward_points"]

def main():
    ap=argparse.ArgumentParser(description="Run basic data-quality checks.")
    ap.add_argument("--input",default="data/sample"); ap.add_argument("--output",default="reports/generated")
    args=ap.parse_args(); inp=Path(args.input); out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    issues=[]
    for file in inp.glob("*.csv"):
        df=pd.read_csv(file,dtype="string")
        name=file.stem
        for col in df.columns:
            missing=int(df[col].isna().sum() + (df[col].astype("string").str.strip()=="").sum())
            if missing:
                issues.append([name,col,"Missing/blank",missing,"High" if col.endswith("_id") else "Medium","Investigate; quarantine if required field"])
        for key in [c for c in KEY_CANDIDATES if c in df.columns]:
            dup=int(df[key].duplicated(keep=False).sum())
            if dup: issues.append([name,key,"Duplicate candidate key",dup,"High","Check key scope and source lineage"])
        for col in [c for c in df.columns if any(x in c.lower() for x in DATE_CANDIDATES)]:
            parsed=pd.to_datetime(df[col],errors="coerce",utc=True)
            invalid=int((df[col].notna() & parsed.isna()).sum())
            if invalid: issues.append([name,col,"Invalid timestamp",invalid,"High","Quarantine and correct producer"])
        for col in [c for c in df.columns if any(x in c.lower() for x in NUMERIC_CANDIDATES)]:
            num=pd.to_numeric(df[col],errors="coerce")
            invalid=int((df[col].notna() & num.isna()).sum())
            negative=int((num<0).sum())
            if invalid: issues.append([name,col,"Invalid numeric",invalid,"High","Reject malformed numeric values"])
            if negative: issues.append([name,col,"Negative numeric",negative,"High","Check business rule and sign convention"])
        if "status" in df.columns:
            norm=df["status"].fillna("").str.strip().str.lower()
            variants=int((norm != df["status"].fillna("").str.lower()).sum())
            if variants: issues.append([name,"status","Whitespace variation",variants,"Low","Normalize then map to approved enum"])
    result=pd.DataFrame(issues,columns=["dataset","field","issue_type","records_affected","severity","recommended_action"])
    result.to_csv(out/"quality_issues.csv",index=False)
    print(f"Quality audit complete: {len(result)} issue groups. Output: {(out/'quality_issues.csv').resolve()}")
    print("Checks are generic; validate business-specific rules and foreign keys with source owners.")
if __name__=="__main__": main()
