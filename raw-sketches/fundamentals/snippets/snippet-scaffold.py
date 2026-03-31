"""
####################
# SNIPPET INFRASTRUCTURE & DX OPTIMIZATION
####################

DATE - 2026-03-30

MILESTONES:
- Implement and master VS Code Snippets [X]
- Refine label ordering and synchronous repetition [X]
- Document the developer experience (DX) workflow [X]

PROGRESS:
- Mastered $0 (Final Cursor Position) and label ordering, including synchronous repetition for speed.
- Adopted professional notation (.cls / .fprint) to avoid syntax collisions and maintain a clean workflow.
- Structured JSON snippets to balance logic with visual showcasing in the repository.

FAILURES:
- Initial friction with JSON structure (commas and escape characters).
    RIGHT VERSION: Rebuilding from scratch to internalize syntax instead of just copying.
"""

####################################
import os

# CONSTANTS
README_PATH = "python/fundamentals/snippets/snippets-showcase.md"

context = {}

# FUNCTIONS

def showcasing_os_snippet():
    """
    Shortcut: .cls
    Purpose: Cross-platform terminal clearing.
    See logic: python/fundamentals/snippets/snippets-showcase.md
    """
    # This command handles both Windows (nt) and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" [LOG] System: Terminal Cleared | Status: Success ")

def showcasing_fprint_snippet():
    """
    Shortcut: .fprint
    Purpose: Linear flow (Label -> Key -> Value) with auto-mirroring.
    See logic: python/fundamentals/snippets/snippets-showcase.md
    """
    # Example variables created via snippet
    esposa = "Marjorie"
    esposo = "Kauan"
    
    # The snippet generates the declaration and the print simultaneously
    print(f" Spouse: {esposa} | Husband: {esposo} ")

def showcasing_rawdoc_snippet():
    """
    Shortcut: .rawdoc
    Purpose: Generates full documentation scaffold and boilerplate.
    See logic: python/fundamentals/snippets/snippets-showcase.md
    """
    print(" [INFO] .rawdoc: Injected full structure (Docstring + Imports + Main Loop) ")

# MAIN LOOP
if __name__ == "__main__":
    # Execution sequence to test the new workflow
    showcasing_os_snippet()
    showcasing_fprint_snippet()
    showcasing_rawdoc_snippet()