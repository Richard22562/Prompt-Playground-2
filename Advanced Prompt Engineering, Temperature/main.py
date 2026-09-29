from groq import generate_response
import time
def temperature_prompt_activity():
    print("=" * 50)
    print("Prompt engineering: temperature and instructions")
    print("=" * 50)
    base=input("Enter a creative prompt: ").strip()
    for t,label in [(0.1,"LOW(0.1)"),(0.5,"Medium (0.5)"),(0.9,"HIGH (0.9)")]:
        print(f"\n--- {label} ---")
        print(generate_response(base,temperature=t,max_tokens=256))
        time.sleep(1)
    topic=input("choose a topic: ").strip()
    prompts=[
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if im a 10 year old"
        f"Write a pro/con list about {topic}"
        f"Create a fictional news headline from 250 about {topic}"
        ]
    for i, p in enumerate(prompts,1):
        print(f"]n--- Instruction {i} ---")
        print(generate_response(p,temperature=0.7,max_tokens=256))
        time.sleep(1)

if __name__=="__main__":
    temperature_prompt_activity()