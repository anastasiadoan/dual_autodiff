# Use a Debian-based Python image compatible with manylinux wheels
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install necessary system dependencies for building and running Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    libjpeg-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Jupyter Notebook
RUN pip install jupyter

# Copy the wheel file into the container
COPY wheelhouse/dual_autodiff_x-0.0.1b2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl /app/wheelhouse/

# Install the wheel file using pip
RUN pip install /app/wheelhouse/dual_autodiff_x-0.0.1b2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

# Copy the Jupyter notebook into the container
COPY TutorialNotebook_x.ipynb /app/

# Expose the default notebook port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
