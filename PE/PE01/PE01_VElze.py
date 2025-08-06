# DS623 PE01 – Matrix Operations
# Topic: Determinant, Transpose, and Inverse of a 2x2 Matrix
# Real-life theme: Dancing with Matrices in STEM Education – because even matrices need to know when to pivot

# 🎯 Function to get and validate user input
def get_matrix_input():
    while True:
        try:
            # Prompt with real-world compass direction labels to guide user layout understanding
            user_input = input(
                "Enter four numbers separated by a space for your 2x2 matrix in this order:\n"
                "(NW NE SW SE)\n"
                "That means: top-left, top-right, bottom-left, bottom-right\n"
                "Example: 3 2 1 8 creates the matrix:\n[[3, 2],\n [1, 8]]\n"
                "Type your four numbers (separated by a space) here>"
            )
            # Attempt to split and convert input into four float numbers
            elements = list(map(float, user_input.strip().split()))
            if len(elements) != 4:
                raise ValueError
            return elements
        except ValueError:
            print("❌ Invalid input. Please enter exactly four numeric values like: 3 2 1 8")

# 💡 Function to compute determinant of a 2x2 matrix
def compute_determinant(a, b, c, d):
    return a * d - b * c

# 🔄 Function to compute transpose of a 2x2 matrix
def compute_transpose(a, b, c, d):
    # Swap rows and columns
    return [[a, c], [b, d]]

# 🔁 Function to compute inverse of a 2x2 matrix using the formula:
# Inverse = 1/det * [[d, -b], [-c, a]]
def compute_inverse(a, b, c, d, det):
    return [
        [round(d / det, 3), round(-b / det, 3)],
        [round(-c / det, 3), round(a / det, 3)]
    ]

# 🎨 Function to display matrix exactly like [[3 2] [1 8]]
def display_matrix(matrix, strip_decimals=False):
    formatted_rows = []
    for row in matrix:
        formatted_row = []
        for el in row:
            # Strip .0 from floats that are whole numbers
            if strip_decimals and el == int(el):
                formatted_row.append(str(int(el)))
            else:
                formatted_row.append(f"{el:.4g}" if isinstance(el, float) else str(el))
        formatted_rows.append("[{}]".format(" ".join(formatted_row)))
    print("[{}]".format("\n ".join(formatted_rows)))

# 🧠 Main function to control program flow
def main():
    # Step 1: Get matrix values from user
    a, b, c, d = get_matrix_input()
    
    # Step 2: Display the matrix layout
    matrix = [[a, b], [c, d]]
    print("\nYour matrix:")
    display_matrix(matrix, strip_decimals=True)

    # Step 3: Calculate and display determinant
    det = compute_determinant(a, b, c, d)
    print("\nThe determinant tells us if the matrix is invertible and gives us a sense of its 'scaling power'.")
    print("Determinant:", round(det, 3))

    # Step 4: If determinant is zero, inverse does not exist
    if det == 0:
        print("* * * Inverse does not exist because the determinant is zero. This matrix cannot be reversed. * * *")
    else:
        # Step 5: Calculate and display transpose
        transpose = compute_transpose(a, b, c, d)
        print("\nThe transpose flips the matrix over its diagonal, swapping rows with columns.")
        print("Transposed:")
        display_matrix(transpose, strip_decimals=True)

        # Step 6: Calculate and display inverse
        inverse = compute_inverse(a, b, c, d, det)
        print("\nThe inverse 'undoes' the matrix — like rewinding your steps. When multiplied, it gives the identity matrix.")
        print("Inversed:")
        display_matrix(inverse)  # Keep full float format
        print("\n")

# 🏁 Entry point
if __name__ == "__main__":
    main()

# REFERENCE: OpenAI. (2025). ChatGPT’s assistance with matrix operations for PE01 [Large language model]. https://openai.com/chatgpt
