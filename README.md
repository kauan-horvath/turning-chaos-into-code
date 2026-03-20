# Turning Chaos into Code

This repository is a systematic log of my journey through software engineering and logic. 
It serves as a laboratory where I transform complex ideas and creative chaos into structured, functional code.

## 🛠 Tech Stack
- **Python**: Focused on automation, design logic, and data structure.
- **Future modules**: Planned expansions for web and creative coding.

## 📂 Organization
- **/python**: All Python-related development.
  - `core-projects`: End-to-end applications and refined solutions.
  - `daily-challenges`: Consistent practice with AI-evaluated logic.
  - `raw-sketches`: Early stage concepts and experimental scripts.

---

> *"Design is not just what it looks like and feels like. Design is how it works."*

```python
# Kauan Horvath - Contact Interface + 🥚

MY_DATA = {
    "LinkedIn": "  in/kauanhorvath  ",
    "Instagram": "  @Just_Horvath  ",
    "E-mail": "  kauanhorvath1996@gmail.com  ",
    "Whatsapp": "  +55 11 95491 0195  "
}

def start_hiring_process(data_source):
    print("\n--- [ CONTACT INTERFACE ] ---\n")
    
    for platform, value in data_source.items():
        key = platform.lower()
        
        if key == "linkedin":
            print(f"LinkedIn: know_more('{value}')")
        elif key == "instagram":
            print(f"Instagram: take_a_look('{value}')")
        elif key == "e-mail":
            print(f"E-mail: send_proposal('{value}')")
        elif key == "whatsapp":
            print(f"Whatsapp: send_a_zapzap('{value}')")

if __name__ == "__main__":
    print("Feel free to contact me if you're looking for a junior developer!")
    start_hiring_process(MY_DATA)
    print("\nLooking forward to hearing from you!")
```
