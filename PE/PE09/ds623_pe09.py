# Programming Exercise 09: Plotting PDFs of the Normal Distribution
# Course: DS623 - Math & Statistics for Data Science  
# Student: Verónica Elze (plotting normal distributions with flair!)

# Import necessary libraries (our trusty sidekicks)
import numpy as np
import matplotlib.pyplot as plt

# Define normal distribution pdf manually (avoiding built-ins, like a coding ninja)
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# Function to humorously get a valid mean input
def get_mean():
    while True:
        mu_input = input("Enter mean (µ) or 'q' to quit (if numbers scare you today): ")
        if mu_input.lower() == 'q':
            return None
        try:
            mu = float(mu_input)
            print(f"Mean accepted: µ={mu}. Looks good!")
            return mu
        except ValueError:
            print("Oops! That's not a number. Try again, number warrior!")

# Function to humorously get a valid standard deviation input
def get_sigma():
    while True:
        sigma_input = input("Enter standard deviation (σ) (> 0 please!): ")
        try:
            sigma = float(sigma_input)
            if sigma <= 0:
                print("Hold your horses! σ must be positive. Let's try again.")
                continue
            print(f"Standard deviation accepted: σ={sigma}. Nice choice!")
            return sigma
        except ValueError:
            print("Whoa! Numbers only, please. Give it another shot.")

# Function to humorously get a valid option input
def get_option():
    while True:
        option_input = input("Enter option (1 or 2, choose wisely!): ")
        try:
            option = int(option_input)
            if option not in [1, 2]:
                print("Only 1 or 2 are allowed in this kingdom. Try again!")
                continue
            print(f"Option accepted: Option {option}. Let’s roll!")
            return option
        except ValueError:
            print("Eek! That's not 1 or 2. Once more, brave soul!")

# Get user inputs with flair
mu = get_mean()
if mu is not None:
    sigma = get_sigma()
    option = get_option()

    # X-axis values (our adventurous journey from µ - 5σ to µ + 5σ)
    x = np.arange(mu - 5 * sigma, mu + 5 * sigma, 0.01)

    # Original PDF (the star of our show)
    y_original = normal_pdf(x, mu, sigma)

    # Plot original PDF (blue, like a clear sky)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_original, color='blue', label=f"µ={mu}, σ={sigma}")

    # Additional plots based on your choice (because options matter)
    if option == 1:
        # PDFs shifting left like a dance move
        y_shift1 = normal_pdf(x, mu - sigma, sigma)
        y_shift2 = normal_pdf(x, mu - 2 * sigma, sigma)
        plt.plot(x, y_shift1, color='yellow', label=f"µ={mu - sigma}, σ={sigma}")
        plt.plot(x, y_shift2, color='red', label=f"µ={mu - 2 * sigma}, σ={sigma}")

    elif option == 2:
        # PDFs getting skinnier like New Year's resolutions
        y_scale1 = normal_pdf(x, mu, 0.8 * sigma)
        y_scale2 = normal_pdf(x, mu, 0.6 * sigma)
        plt.plot(x, y_scale1, color='yellow', label=f"µ={mu}, σ={0.8 * sigma}")
        plt.plot(x, y_scale2, color='red', label=f"µ={mu}, σ={0.6 * sigma}")

    # Set y-axis (giving the plot some breathing room)
    plt.ylim(0, 3 * max(y_original))

    # Add charming labels and title
    plt.title("Normal Distribution PDFs – Because Bell Curves are Beautiful!")
    plt.xlabel("x")
    plt.ylabel("PDF")
    plt.legend()
    plt.grid(True)

    # Finally, let the show begin!
    plt.show()
else:
    print("Program exited by user. Maybe next time?")
