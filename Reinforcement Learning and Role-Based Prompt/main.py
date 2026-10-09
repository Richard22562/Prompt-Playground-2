from groq import generate_response


def reinforcement_learning_activity():
    prompt = input("Enter a prompt for the AI model: ").strip()
    if not prompt:
        print("Please enter a prompt.")
        return


    # Initial response
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response:\n{initial_response}")


    # Rating
    try:
        rating = int(input("Rate the response (1-5): ").strip())
        if rating < 1 or rating > 5:
            rating = 3
    except ValueError:
        rating = 3


    # Ask if user wants improvement
    improve_choice = input("Would you like an improved response based on your rating/feedback? (y/n): ").strip().lower()
    if improve_choice == "y":
        feedback = input("Provide feedback: ").strip()
        improvement_prompt = (
            f"Original prompt: {prompt}\n"
            f"Initial response: {initial_response}\n"
            f"User rating: {rating}/5\n"
            f"User feedback: {feedback}\n"
            "Please generate an improved response based on the feedback and rating."
        )
        improved_response = generate_response(improvement_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nImproved AI Response:\n{improved_response}")


def role_based_prompt_activity():
    category = input("Enter a category (e.g., science, history): ").strip()
    item = input(f"Enter a specific {category} topic: ").strip()


    if not category or not item:
        print("Please fill in both fields.")
        return


    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in detail."


    teacher_response = generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)


    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")


def run_activity():
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()


    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    run_activity()




