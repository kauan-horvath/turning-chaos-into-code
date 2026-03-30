# 🛠️ VS Code Custom Snippets Showcase

This document outlines the custom-built infrastructure used to maintain high standards of documentation, logging consistency, and development speed across this repository.

---

## 1. 🏗️ `.rawdoc` | The Architecture Scaffold
This is the "Golden Standard" for every new Python file. It automates the generation of a complete project structure, including a rigorous documentation header and standard boilerplate.

### **Final Result Preview:**
```python
"""
####################
# PROJECT TITLE
####################

DATE - 2026-03-30

MILESTONES:
- MILE1 [ ]
- MILE2 [ ]
- MILE3 [ ]

PROGRESS:
WHAT - SHORT EXPLAIN

FAILURES:
WHAT - SHORT EXPLAIN
    RIGHT VERSION: Explain fix
"""

####################################
import os

CONST = None

context = {}

# FUNCTIONS

def aux_function():
    pass

def logic_function():
    pass

# MAIN LOOP

if __name__ == "__main__":
    pass
```

### **Snippet Source (JSON):**
```json
"Rigor Document Standard (Blank)": {
  "prefix": ".rawdoc",
  "body": [
    "\"\"\"",
    "####################",
    "# ${1:TITLE}",
    "####################",
    "",
    "DATE - ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DAY}",
    "",
    "MILESTONES:",
    "- ${2:MILE1} [ ]",
    "- ${3:MILE2} [ ]",
    "- ${4:MILE3} [ ]",
    "",
    "PROGRESS:",
    "${5:WHAT} - ${6:SHORT EXPLAIN}",
    "",
    "FAILURES:",
    "${7:WHAT} - ${8:SHORT EXPLAIN}",
    "\tRIGHT VERSION: ${9:Explain fix}",
    "\"\"\"",
    "",
    "####################################",
    "import os",
    "",
    "CONST = ${10:None}",
    "",
    "context = {}",
    "",
    "# FUNCTIONS",
    "",
    "def aux_function():",
    "\tpass",
    "",
    "def logic_function():",
    "\tpass",
    "",
    "# MAIN LOOP",
    "",
    "if __name__ == \"__main__\":",
    "\t${0:pass}"
  ]
}
```

---

## 2. 📊 `.fprint` | Linear Debugging Log
A sophisticated alternative to standard `print()`. It enforces a visual design for console logs while simultaneously declaring variables.

### **Final Result Preview:**
```python
user_id = 101
status = "Active"
print(f" ID: {user_id} | Account: {status} ")
```

### **Snippet Source (JSON):**
```json
"Formatted Print (Linear Flow)": {
  "prefix": ".fprint",
  "body": [
    "${2:key} = ${3:value}",
    "${5:key} = ${6:value}",
    "print(f\" ${1:Label}: {${2:key}} | ${4:Label}: {${5:key}} \")$0"
  ]
}
```

---

## 3. 🧹 `.cls` | Terminal Housekeeping
A quick utility for maintaining a clean output. It detects the operating system automatically to run the correct terminal command.

### **Snippet Source (JSON):**
```json
"Clear Terminal": {
  "prefix": ".cls",
  "body": [
    "os.system('cls' if os.name == 'nt' else 'clear')$0"
  ]
}
```

---

### 🧠 Developer's Insight
> *"Give me six hours to chop down a tree and I will spend the first four **sharpening the axe**."* — **Abraham Lincoln**

By automating the structural parts of coding, I free up mental bandwidth to focus on complex logic and visual design. These snippets represent the bridge between **rigorous engineering** and **aesthetic efficiency**.

>> Estimated time: 2.5 hours of learning and architecture compilation
