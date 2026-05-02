#  Life Energy Dashboard 🚀 
import json 
json_path = r"D:\01_Coding\Python Projects\scores.json"
try:
    with open(json_path, "r") as f:
        weekly_scores = json.load(f)
except FileNotFoundError:
    weekly_scores = []

def user_input():
    study = float(input("How many hours have you studied: "))
    phone = float(input("How many hours have you used Phone: "))
    sleep = float(input("How many hours have you slept: ")) 
    waste = float(input("How many hours you did nothing or wasted: "))

    total = study + phone + sleep + waste 

    # Validation
    if study < 0 or phone < 0 or sleep < 0 or waste < 0:
        print("❌ Please enter values above zero. ")
        return user_input()
    
    if total > 24:
        print("❌ Total hours cannot exceed 24. ")
        return user_input() 
    
    return study, phone, sleep, waste 

def calculate(study, phone, sleep, waste):
    productive = study 
    distracted = phone + waste 

    total_active_time = productive + distracted 

    if total_active_time == 0:
        print("⚠ No activity recorded. ")
        return 

    life_score = (productive / total_active_time ) * 100
    print(f"🔥 Life Score : {round(life_score, 2)} / 100")

    if life_score >= 70:
        print("✅ Good Discipline Level. ")
    elif life_score >= 40:
        print("⚠ Average - Improve Focus ")
    else:
        print("🏮 Low Discipline - Danger Zone ")
    return life_score 
    
# Weekly Score System
def weekly_report(scores):
    if len(scores) == 0:
        print("⚠ No weekly data yet.")
        return 
    
    avg = sum(scores) / len(scores) 

    print("\n📊 WEEKLY REPORT")
    print(f"Days Tracked: {len(scores)}")
    print(f"Average Life Score: {round(avg, 2)}")

    if avg >= 70:
        print("💪 Excellent Week! ")
    elif avg >= 40: 
        print("⚠ Moderate Week - Improve consistency")
    else: 
        print("🔴 Weak Week - Too much distraction")


# Main Flow
data = user_input()
score = calculate(*data) 

if score is not None:
    weekly_scores.append(score) 
    with open(json_path, "w") as f:
        json.dump(weekly_scores, f) 
    print("✅ Saved to Json File")

    check = input("\nDo you want weekly report? (yes/no): ").lower()
    if check == "yes":
        weekly_report(weekly_scores) 