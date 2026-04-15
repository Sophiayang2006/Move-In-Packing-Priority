import gradio as gr
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


# Sample items to test the app
items_list = [
    {"label": "TV + Stand", "weight": 7, "fragility": 9, "priority": 8},
    {"label": "Winter Clothes", "weight": 4, "fragility": 1, "priority": 3},
    {"label": "Laptop Bag", "weight": 2, "fragility": 10, "priority": 10},
    {"label": "Bookshelf", "weight": 9, "fragility": 2, "priority": 4},
    {"label": "Kitchen Box", "weight": 6, "fragility": 5, "priority": 7},
    {"label": "Mirror", "weight": 3, "fragility": 10, "priority": 6},
    {"label": "Bedframe", "weight": 10, "fragility": 1, "priority": 5},
    {"label": "Desk Lamp", "weight": 2, "fragility": 7, "priority": 9},
]


# Calculate how important each item is
def calc_score(item):
    weight_part = 10 - item["weight"]

    if weight_part < 0:
        weight_part = 0

    score = (item["fragility"] * 0.5) + (item["priority"] * 0.35) + (weight_part * 0.15)
    return round(score, 2)


# Turn items into text for the input box
def start_text():
    text = ""

    for item in items_list:
        text += item["label"] + ", " + str(item["weight"]) + ", " + str(item["fragility"]) + ", " + str(item["priority"]) + "\n"

    return text.strip()


# Load example data
def load_sample_data():
    return start_text()


# Read and check user input
def parse_input(text):
    lines = text.strip().split("\n")
    items = []
    errors = []
    line_number = 1

    for line in lines:
        line = line.strip()

        if line == "":
            line_number += 1
            continue

        parts = line.split(",")

        if len(parts) != 4:
            errors.append("Line " + str(line_number) + " is wrong.")
            line_number += 1
            continue

        label = parts[0].strip()

        if label == "":
            errors.append("Line " + str(line_number) + " has no name.")
            line_number += 1
            continue

        try:
            weight = int(parts[1].strip())
            fragility = int(parts[2].strip())
            priority = int(parts[3].strip())
        except:
            errors.append("Line " + str(line_number) + " needs numbers.")
            line_number += 1
            continue

        items.append({
            "label": label,
            "weight": weight,
            "fragility": fragility,
            "priority": priority
        })

        line_number += 1

    if len(items) < 2:
        errors.append("Add at least 2 items.")

    if len(errors) > 0:
        return None, "\n".join(errors)

    return items, None


# Quick Sort algorithm with steps
def quick_sort_steps(items):
    arr = [dict(item) for item in items]
    steps = []

    def make_copy():
        return [dict(x) for x in arr]

    def add_step(action, text, pivot, a, b, low, high):
        steps.append({
            "action": action,
            "array": make_copy(),
            "text": text,
            "pivot": pivot,
            "a": a,
            "b": b,
            "low": low,
            "high": high
        })

    def split(low, high):
        middle = (low + high) // 2
        pivot_score = calc_score(arr[middle])

        add_step("pivot", "Pivot is " + arr[middle]["label"], middle, -1, -1, low, high)

        i = low
        j = high

        while i <= j:
            while calc_score(arr[i]) > pivot_score:
                i += 1

            while calc_score(arr[j]) < pivot_score:
                j -= 1

            if i <= j:
                add_step("compare", "Comparing items", middle, i, j, low, high)

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    add_step("swap", "Swapped items", -1, i, j, low, high)

                i += 1
                j -= 1

        return i

    def sort_parts(low, high):
        if low >= high:
            return

        middle = split(low, high)
        sort_parts(low, middle - 1)
        sort_parts(middle, high)

    sort_parts(0, len(arr) - 1)

    add_step("done", "Sorting finished", -1, -1, -1, 0, len(arr) - 1)

    return steps, arr


# Draw the bar chart
def make_plot(arr, step):
    labels = []
    scores = []
    bar_colors = []

    for i in range(len(arr)):
        item = arr[i]
        labels.append(item["label"])
        scores.append(calc_score(item))

        color = "skyblue"

        if i == step["pivot"]:
            color = "pink"

        elif i == step["a"] or i == step["b"]:
            color = "gold"

        bar_colors.append(color)

    fig, ax = plt.subplots()
    ax.barh(labels, scores, color=bar_colors)

    return fig


# Make final results table
def make_table(arr):
    table = []

    rank = 1
    for item in arr:
        table.append([rank, item["label"], calc_score(item)])
        rank += 1

    return table
