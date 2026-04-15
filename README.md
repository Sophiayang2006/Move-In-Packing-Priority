# Move-In-Packing-Priority-QuickSort

---

## Chosen Problem (1-2 sentences)
I made an app to help decide which boxes to unpack first when moving into a new house. Each box has a name, weight, fragility, and priority. I use a simple formula to give each box a score so I can compare them. The app checks that each item has 4 parts, that the numbers are between 1 and 10, and there are at least 2 items before sorting. The data does not need to be sorted before. On the screen, the user sees bars for each item, with the bar size indicating the score. Colors indicate what is happening: blue is normal, pink is the pivot, gold indicates comparison, purple indicates swapping, and green indicates done. 

---


## Chosen Algorithm (name + why it fits)
I chose Quick Sort because it works well for comparing scores and is fast for small lists like this. It also swaps items in place, so it is easier to show how the list changes step by step. The algorithm picks a middle item as a pivot and compares other items to it to move them into the right place. I made my own Quick Sort and did not use built-in sorting like sort() or sorted() because the assignment says we have to implement it ourselves. 
## Demo (video/gif/screenshot of at least one run)

https://github.com/user-attachments/assets/bd4cf295-a1cb-4130-93f5-37f664019043

---

## Problem Breakdown & Computational Thinking (include a flowchart + the 4 pillars as brief bullets)
Problem Decomposition 
1. Read each item's name, weight, fragility, and priority from the text box 
2. Split each line into 4 parts
3. Check that every line has all 4 parts 
4. Make sure weight, fragility, and priority are numbers from 1 to 10 
5. Give each item one score using the formula 
6. Store all items in a working list 
7. Pick a middle item as the pivot 
8. Compare other items to the pivot score 
9. Swap items if they are on the wrong side 
10. Repeat this on smaller parts of the list
11. Save every pivot, compare, and swap step 
12. Show the saved steps in the chart 
13. Display the final sorted list at the end
Instead of showing the sorting while it is happening, the program saves all the steps first and then plays them back for the user. 
---
Pattern Recognition 

This is a compare and swap problem 

- Pattern: Pick a pivot, compare items, and move them left or right 
- Similar to sorting cards in your hand or lining people up by heights 
- Idea: 
  - Higher score items move to the left 
  - Lower score items move to the right 
  - The same compare and swap steps happen again and again
  - Each time, the part being sorted gets smaller until everything is in the right place
---
Abstraction 

Focus on: 

  - Which item is the pivot
  - Which two items are being compared 
  - When two items are being swapped 
  - The part of the list being sorted right now 
  - The final sorted order
    
Show it by: 

  - A bar chart for all item scores 
  - Different colors for pivot, compare, swap, and done
  - A status message that explains each step in simple words 
  - A final ranked table after sorting finishes

Ignore: 

  - The recursion is happening inside the code 
  - Memory addresses and other computer details 
  - Extra calculations in the background 
  - How the GUI stores data between button clicks

Important: The user does not need to understand hard computer science words. The colors and messages make the sorting easy to follow. 

---

Algorithmic Thinking 

Inputs: 

  - A multiline string typed into a text box 
  - Each line is: label, weight, fragility, priority
  - At least 2 items are needed
  - The numbers must be from 1 to 10

Data types/ Data Structures : 

  - The input starts as a string 
  - Each item is stored as a dictionary with label, weight, fragility, and priority
  - All items are stored in a list 
  - Each saved sorting step is also stored as a dictionary 
  - All steps are stored in a list of step dictionaries.

Processing: 

  - Check the input is correct 
  - Calculate scores from each item 
  - Run quick sort step by step 
  - Save pivot, compare, and swap as a step
  - Send those steps to the GUI for playback

Output: 

  - A bar chart showing items being sorted 
  - Colors to show what is happening 
  - A message explaining each step 
  - A final sorted table of all items and scores

GUI Flow: 

  - The user types the items into the text box 
  - The user presses sort 
  - The program checks the input and sorts the items 
  - The GUI shows the steps one by one 
  - The user can step forward, backward, or auto-play

Constraints: 

  - Each item must have 4 parts 
  - Weight, fragility, and priority must be integers from 1 to 10 
  - At least 2 items are needed 
  - The list is small, so quicksort works well
---
Flowchart 


<img width="808" height="1077" alt="Untitled (Draft)" src="https://github.com/user-attachments/assets/0a28c26a-c5ba-48da-812b-7b03cb068168" />

---

## Steps to Run (local)

Step 1: Download Python from: https://www.python.org/downloads/

Step 2: Open a terminal and verify that Python is installed by running python --version in the terminal

Step 3: Install Gradio

Step 4: Download app.py from the GitHub repo

Step 5: In the terminal, run python app.py

Step 6: While the terminal is open, open https://localhost:7860 in your browser

Step 7: Run the visualization

---

## Requirements
gradio>=4.0.0
matplotlib==3.10.1

---

## Hugging Face Link
https://huggingface.co/spaces/sofhyia/Move-In-Packing-Priority

---


## Testing (what you tried + edge cases)

- Test 1: Smallest Input Test 

I wanted to see if the app works when I only put in 2 items, which is the smallest amount it can take. I thought the app would still work, make a chart, and sort the 2 items properly. The app worked fine; it took both items and sorted them using QuickSort. The app works well even with only 2 items.

<img width="1512" height="982" alt="Screenshot 2026-04-15 at 5 19 37 PM" src="https://github.com/user-attachments/assets/c526b2f8-0376-47f1-8d76-c353a3896d52" />


- Test 2: All Scores are the same 

I wanted to see what happens if every item has the same score. I was checking if the sorting still works and doesn't break. I thought the app would still work, not crash, and just compare the items, and it did just that. 

<img width="1512" height="982" alt="Screenshot 2026-04-15 at 7 05 18 PM" src="https://github.com/user-attachments/assets/2e146c77-d12b-4709-914c-e850f08bda3b" />


- Test 3: Already sorted list

I wanted to see what happens when the list is already in order before using the QuickSort method. I thought the program would not need to change anything because the list was already sorted. The program mostly just checked the items and pricked pivot points. It did not swap anything. The order at the end was the same as the start.

<img width="1512" height="982" alt="Screenshot 2026-04-15 at 7 08 29 PM" src="https://github.com/user-attachments/assets/44adadd2-75eb-464a-a6ca-2a60b879f4f3" />

---

## Author & Acknowledgment (sources + AI use, if any)

Author: Sophia Yang Section: 001 

Sources: CISC 121 Notes 

####AI WAS USED (LEVEL 4): Claude was used to help me understand the problem better and improve my code. First, I wrote a draft version of my program. Then I asked Claude questions to help me understand how QuickSort works and how to fix problems in my code. It also helped me turn my ideas from the 4 pillars into a working program. Claude helped generate a cleaner final version of the code based on my draft, but I reviewed all the code myself, made changes, and made sure I understood how it worked before using it. 

https://claude.ai/share/e44119c0-c171-4085-808b-814b8a057b7b
