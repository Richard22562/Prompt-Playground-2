from groq import generate_response
def bias_metication_activity():
    print("\n=== BIAS MITIGATION ACTIVITU ==\n")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor): ").strip()
    if not prompt:
        print("Please enter a prompt.")
        return
    initial_response=generate_response(prompt, temperature=0.3,max_tokens=1024)
    print(f"\nIniitial AI Response:\n{initial_response}")
    modified_prompt=input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ").strip()
    if modified_prompt:
        modified_response=generate_response(modified_prompt,temperature=0.3,max_tokens=1024)
        print(f"\nModified AI Response (Neutural):\n{modified_response}")
    else:
        print("No modified prompt entered. Skipping neutral response.")
def run_activity():
    print("\n=== AI Bias Mitigration ===")
    bias_metication_activity()
if __name__=="__main__":
    run_activity()