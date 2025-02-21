# Active Inference Loop

## Overview

The Active Inference Loop project visualizes the concept of active inference using the Manim animation engine. It demonstrates the interactions between an agent and its environment, showcasing various states and actions within the active inference framework.

## Video Demonstration

You can watch the video demonstration
![Video Demonstration](public/ActiveInferenceLoop.gif)

## Requirements

- Python 3.7 or higher
- Manim Community Edition

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/skoghoern/active_inference_animations
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install manim
   ```

## Usage

To run the animation, use the following command:

```bash
manim -pql active_inference_loop.py ActiveInferenceLoop
```

- `-pql` stands for preview in low quality. You can adjust the quality settings as needed.

## Project Structure

- `active_inference_loop.py`: Contains the main code for the active inference loop animation.
- `public/`: Directory containing SVG assets for the agent and environment visuals.

## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.
