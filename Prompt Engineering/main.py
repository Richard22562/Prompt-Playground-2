from groq import generate_response
def run_activity():
    print("Zero-Shot,One-Shot,Few-Shot Activity")
    category=input("Enter a category(eg.animal,food,science,etc): ").strip()
    item=input(f"Enter a specific {category} to classify: ")
    if not category or not item:
        print("Please fill all the fields")
        return
    zero_shot=f"is {item} a {category}? Answer yes or no"
    print("\n---Zero Shot Learning---\n")
    print(f"Response: {generate_response(zero_shot,temperature=0.3,max_tokens=1024)}")
    one_shot=f"""Example:
    Category: fruit
    Item: apple
    Answer: Yes, apple is a fruit
    Now you try:
    category: {category}
    item:{item}
    answer:"""
    print("\n---One Shot Learning---\n")
    print(f"Response: {generate_response(one_shot,temperature=0.3,max_tokens=1024)}")
    few_shot=f"""Example:
    Category: fruit
    Item: apple
    Answer: Yes, apple is a fruit
    Now you try:
    category: {category}
    item:{item}
    answer:"""

    print("\n---Few Shot Learning---\n")
    print(f"Response: {generate_response(few_shot,temperature=0.3,max_tokens=1024)}")
if __name__ == "__main__":
    run_activity()


    
