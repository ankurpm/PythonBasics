🟢 Level 1 — Basic Function Understanding

1️⃣ Simple Function
Write a function square(num) that returns the square of a number.

2️⃣ Default Parameters
Write a function greet(name, greeting="Hello")
It should return:
"Hello John"
If greeting is not provided, use default.

🟡 Level 2 — *args and **kwargs

3️⃣ Using *args
Write a function multiply_all(*args) that multiplies all numbers passed to it.

Example: multiply_all(2, 3, 4) → 24

4️⃣ Using **kwargs
Write a function build_profile(**kwargs) that returns a dictionary with all provided keyword arguments.

Example: build_profile(name="Ankur", role="Engineer")

5️⃣ Combine *args and **kwargs

Write a function:

def report(*args, **kwargs):

It should:

Print all positional arguments

Print all keyword arguments

🟠 Level 3 — Keyword-only & Positional-only
6️⃣ Keyword-Only Argument

Write a function:

def calculate(price, *, tax=0.1):


Return total price after tax.

Make sure tax must be passed as keyword.

7️⃣ Positional-Only Argument

Write a function:

def divide(a, b, /):


Ensure both parameters must be positional-only.

Test that keyword call fails.

🔴 Level 4 — Higher Order Functions
8️⃣ Function as Argument

Write a function:

def apply_operation(a, b, operation):


Where operation is another function.

Example:

apply_operation(5, 3, add)
apply_operation(5, 3, subtract)

9️⃣ Write a Decorator

Create a decorator @logger that:

Prints "Function started"

Executes function

Prints "Function ended"

Apply it to a sample function.

🔥 Level 5 — Advanced / Interview-Level
🔟 Flexible Logging Wrapper

Write a decorator that:

Accepts *args and **kwargs

Measures execution time

Prints function name

Returns original result

Should work for ANY function signature.

💎 Bonus (Very Advanced)

Write a function:

def forward(*args, **kwargs):


That calls another function passed via kwargs like:

forward(1, 2, func=add)


It should:

Extract function

Forward positional arguments

Return result