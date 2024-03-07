import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="P1: Browser Interactive App with Plot")

# Create a sidebar with a slider input
with ui.sidebar():
    # Add slider for specifying the number of bins in the histogram. 
    # The ui.input_slider function is called with five arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input value. 
    # 2. A string label (e.g., "Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins (e.g., 0).
    # 4. An integer representing the maximum number of bins (e.g., 100).
    # 5. An integer representing the initial value of the slider (e.g., 20).
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20, step=1)
    # Include additional controls for histogram customization:
    # Checkbox to toggle the normalization of the histogram.
    ui.input_checkbox("normalize_histogram", "Normalize Histogram", True)
    # Text input for the histogram title.
    ui.input_text("histogram_title", "Histogram Title", "Distribution of Random Data")
    # Dropdown for the color of the histogram bars. Choose from a list of 10 colors.
    ui.input_select("histogram_color", "Histogram Color", 
                    choices=["skyblue", "salmon", "green", "gold", "purple",
                             "orange", "pink", "lavender", "red", "lightgreen"],
                    selected="skyblue")

@render.plot(alt="A histogram showing random data distribution")
def histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer
    count_of_points: int = 437
    # Set random seed to ensure reproducibility
    np.random.seed(1385491)  
    # Generate random data:
    # - np.random.randn(count_of_points) generates 'count_of_points' samples from a standard normal distribution
    # - Each sample is then scaled by 15 and shifted by 100
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    # Create a histogram of the random data using matplotlib's hist() function:
    # - 1st argument is the data array
    # - 2nd argument specifies the number of bins, set by input slider's current value
    # - 'density' parameter, when True, normalizes histogram so total area under histogram equals 1
    # - 'color' parameter is set by the dropdown's current selection
    plt.hist(random_data_array, bins=input.selected_number_of_bins(), density=input.normalize_histogram(), color=input.histogram_color())
    # Set the title of the histogram based on user input
    plt.title(input.histogram_title())
    # Add labels to the x and y axes. The y-axis label changes based on whether the histogram is normalized.
    plt.xlabel('Value')
    plt.ylabel('Density' if input.normalize_histogram() else 'Count')



