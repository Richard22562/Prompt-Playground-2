from groq import generate_response
def reinforcement_learning_activity():
    prompt=input("Enter a prompt for the AI model: ").strip()
    if not prompt:
        print("Please enter a prompt")
        return
    initial_response=generate_response(prompt, temperature=0.3,max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")
    try:
        rating=int(input("Rate the response (1-5): ").strip())
        if rating<1 or rating>5:
            rating=3
    except ValueError:
        rating=3
    feedback=input("Provide feedback: ").strip()
    improved_response=f"{initial_response} (Improved with feedback: {feedback})"
    print(f"\nImproved AI Response: {improved_response}")
def role_based_prompt_activity():
    category=input("Enter a category (e.g., science, history): ").strip()
    item=input(f"Enter a specific {category} topic: ").strip()
    if not category or not item:
        print("Please fill in both fields.")
        return
    teacher_prompt=f"You are a teacher. Explain {item} in simple terms"
    expert_prompt=f"You are an expert in {category}. Explain {item} in detail"
    teacher_response=generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response=generate_response(expert_prompt, temperature=0.3, max_tokens=1024)
    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")
def run_activity():
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role Based Prompts")
    choice=input("> ").strip()
    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice")
if __name__=="__main__":
    run_activity()