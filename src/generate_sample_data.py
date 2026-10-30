from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

# Recreates clearly synthetic sample files for testing only.
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "sample"
OUT.mkdir(parents=True, exist_ok=True)
random.seed(42)
users = []
for i in range(1, 31):
    users.append({"user_id": f"U{i:04d}", "signup_timestamp": (datetime(2026,1,1)+timedelta(days=i*2)).isoformat(),
                  "acquisition_source": random.choice(["organic","referral","social","campaign"]),
                  "account_status": random.choice(["active","inactive","pending"]), "country":"IN"})
pd.DataFrame(users).to_csv(OUT/"Users.csv", index=False)
tasks=[]
for i in range(1,101):
    start=datetime(2026,2,1)+timedelta(hours=i*7)
    status=random.choice(["completed","started","rejected","expired"])
    tasks.append({"task_activity_id":f"TA{i:05d}","user_id":f"U{random.randint(1,30):04d}","task_id":f"T{random.randint(1,12):03d}",
                  "started_at":start.isoformat(),"completed_at":(start+timedelta(minutes=45)).isoformat() if status=="completed" else "",
                  "status":status,"reward_points":random.choice([10,20,25,50]) if status=="completed" else 0})
pd.DataFrame(tasks).to_csv(OUT/"Task_Activity.csv",index=False)
for name, rows in {
"Rewards":[{"reward_id":f"R{i:05d}","user_id":f"U{random.randint(1,30):04d}","source_activity_id":f"TA{random.randint(1,100):05d}","points":random.choice([10,20,25,50]),"status":random.choice(["credited","pending","reversed"])} for i in range(1,61)],
"Wallet":[{"wallet_txn_id":f"W{i:05d}","user_id":f"U{random.randint(1,30):04d}","txn_type":random.choice(["credit","debit","adjustment"]),"amount":round(random.uniform(5,250),2),"currency":"INR","status":random.choice(["success","pending","failed"])} for i in range(1,61)],
"Withdrawals":[{"withdrawal_id":f"WD{i:04d}","user_id":f"U{random.randint(1,30):04d}","requested_amount":round(random.uniform(100,1000),2),"status":random.choice(["requested","processing","paid","rejected"])} for i in range(1,21)],
"Referrals":[{"referral_id":f"REF{i:04d}","referrer_user_id":f"U{random.randint(1,30):04d}","referred_user_id":f"U{random.randint(1,30):04d}","status":random.choice(["invited","registered","qualified","rewarded","expired"])} for i in range(1,16)],
"Feature_Events":[{"event_id":f"E{i:06d}","user_id":f"U{random.randint(1,30):04d}","event_name":random.choice(["app_opened","task_started","task_completed","reward_credited","withdrawal_requested"]),"event_timestamp":(datetime(2026,3,1)+timedelta(minutes=i*23)).isoformat(),"platform":random.choice(["android","ios","web"])} for i in range(1,151)],
"Messy_Data":[{"record_id":"M001","user_id":"U0001","event_timestamp":"2026-03-01T10:00:00","status":"success","amount":"100"},{"record_id":"M002","user_id":"","event_timestamp":"not-a-date","status":"SUCCESS ","amount":"-25"},{"record_id":"M003","user_id":"U9999","event_timestamp":"2026-03-03T12:00:00","status":"unknown","amount":"abc"},{"record_id":"M003","user_id":"U0002","event_timestamp":"2026-03-03T12:00:00","status":"success","amount":"50"}]
}.items():
    pd.DataFrame(rows).to_csv(OUT/f"{name}.csv", index=False)
print(f"Synthetic demo CSVs created in {OUT}. These are not actual VELOOP data.")
