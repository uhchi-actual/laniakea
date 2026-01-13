import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURATION ---
NUM_GALAXIES = 2000     # Count of particles
UNIVERSE_SIZE = 100     # Coordinate range (-100 to 100)

def initialize_universe():
    """
    Creates the raw data for our universe.
    Returns a matrix of shape (NUM_GALAXIES, 3) for X, Y, Z.
    """
    # Vectorized initialization for performance
    positions = np.random.uniform(-UNIVERSE_SIZE, UNIVERSE_SIZE, (NUM_GALAXIES, 3))
    return positions

def render_snapshot(positions):
    """
    Takes the data and draws a static frame with UHCHI colors.
    """
    # COLORS
    UHCHI_GREY = '#212121'  # Background
    UHCHI_CYAN = '#1a6a69'  # Galaxies
    UHCHI_RED  = '#b71c1c'  # The Attractor/Singularity

    fig = plt.figure(figsize=(10, 10), facecolor=UHCHI_GREY) 
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_facecolor(UHCHI_GREY)
    ax.grid(False)
    ax.axis('off') 
    ax.set_xlim([-UNIVERSE_SIZE, UNIVERSE_SIZE])
    ax.set_ylim([-UNIVERSE_SIZE, UNIVERSE_SIZE])
    ax.set_zlim([-UNIVERSE_SIZE, UNIVERSE_SIZE])

    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], s=2, c=UHCHI_CYAN, alpha=0.8)
    ax.scatter(0, 0, 0, s=100, c=UHCHI_RED, alpha=1.0)

    plt.show()

# --- MAIN EXEC ---
if __name__ == "__main__":
    galaxies = initialize_universe()
    render_snapshot(galaxies)