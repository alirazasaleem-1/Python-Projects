#  Life Energy Dashboard 🚀 

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
    
# Main Flow
data = user_input()
calculate(*data) 