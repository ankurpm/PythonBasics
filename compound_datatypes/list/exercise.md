## 🐍 Python List Exercises

### 1. Basic Operations and Access (Beginner)

* **Task:** Create a list named `temperatures` storing the following daily high temperatures for a week: `[25, 28, 24, 26, 30, 27, 29]`.
    * **a.** Print the **first** temperature.
    * **b.** Print the **last** temperature using negative indexing.
    * **c.** Print the **total number of days** (the length of the list).
    * **d.** Change the temperature for the **third day** (index 2) to **22**. Print the updated list.

---

### 2. List Slicing and Iteration (Intermediate)

* **Task:** Use the list of cities: `['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Rome']`.
    * **a.** Create a new list called `european_cities` that contains only the cities from index 1 up to (but not including) index 5, using **slicing**.
    * **b.** **Iterate** through the original city list and print each city name along with its index (e.g., "City 0: New York").

---

### 3. List Manipulation and Methods (Intermediate)

* **Task:** Start with an empty list named `inventory`.
    * **a.** Use the **`.append()`** method to add the items `'apple'`, `'banana'`, and `'cherry'` one by one.
    * **b.** Use the **`.insert()`** method to add `'orange'` at the **second position** (index 1).
    * **c.** Use the **`.remove()`** method to remove `'banana'`.
    * **d.** Use the **`.pop()`** method to remove and print the **last item** in the list.
    * **e.** Print the final `inventory` list.

---

### 4. List Comprehension and Conditionals (Advanced)

* **Task:** Start with a list of numbers: `numbers = [1, 5, 8, 12, 15, 20, 23, 28, 30]`.
    * **a.** Use a **list comprehension** to create a new list called `even_squares` that contains the **square** of every **even number** from the original list.
    * **b.** The new list should look like: `[4, 144, 400, 784, 900]`. Print `even_squares`.

---

### 5. Nested Lists (Advanced)

* **Task:** Create a nested list named `student_data` to store the name and grade for three students:
    * `[['Alice', 95], ['Bob', 88], ['Charlie', 72]]`
    * **a.** Access and print **Bob's grade**.
    * **b.** **Add a new student** to the list: `['Diana', 91]`.
    * **c.** Change **Charlie's grade** from 72 to **75**.
    * **d.** Iterate through the `student_data` list and print a sentence for each student (e.g., "Alice achieved a grade of 95.").
