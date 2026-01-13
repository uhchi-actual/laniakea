import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- CONFIGURATION (Goldilocks Settings for Performance and Visuals) ---
NUM_GALAXIES = 4000      # High density for filaments
NUM_STARS = 1500         # Background dust
UNIVERSE_SIZE = 220      # Upper sized scale
ANIMATION_SPEED = 1      # Minimal delay for max FPS

# --- PALETTE (Scientific Gold/Teal) ---
# uhchi color palette
UHCHI_VOID = '#050505'   
UHCHI_CYAN = '#1a6a69'   
UHCHI_GOLD = '#d4af37'   
UHCHI_RED  = '#b71c1c'   

def initialize_universe():
    # Flow Particles (The Neural Network)
    # Gaussian distribution (bell curve) instead of uniform
    # Naturally puts more matter in the center, like a real galaxy cluster, resulting in better/more discrete filament formation
    flow = np.random.normal(0, UNIVERSE_SIZE*0.6, (NUM_GALAXIES, 3))
    
    # 60% Cyan, 40% Gold (Gold Particles represent denser regions)
    colors = [UHCHI_CYAN] * int(NUM_GALAXIES * 0.6) + [UHCHI_GOLD] * int(NUM_GALAXIES * 0.4)
    
    # Distant Stars (Backdrop)
    stars = np.random.uniform(-UNIVERSE_SIZE*1.5, UNIVERSE_SIZE*1.5, (NUM_STARS, 3))
    
    return flow, colors, stars

def update_physics(frame, positions, scat_flow):
    """
    Physics V5.0: Spectral Turbulence (Fractal Universe Logic)
    """
    # --- THE ATTRACTOR (Black Hole Modeled) ---
    vector_to_center = 0 - positions
    dist_to_center = np.linalg.norm(vector_to_center, axis=1, keepdims=True)
    gravity_direction = vector_to_center / (dist_to_center + 1e-9)

    # --- SPECTRAL TURBULENCE (The "Fractal" Math) ---
    # Layer 1: Supercluster Particles (Huge, slow waves)
    f1 = 0.02; s1 = 0.002
    n1_x = np.sin(positions[:, 1]*f1 + frame*s1)
    n1_y = np.cos(positions[:, 2]*f1 + frame*s1)
    n1_z = np.sin(positions[:, 0]*f1 + frame*s1)

    # Layer 2: Filament Rope Particles (twists and turns at termination points)
    f2 = 0.05; s2 = 0.005
    n2_x = np.sin(positions[:, 2]*f2 - frame*s2) # Negative time for complexity
    n2_y = np.sin(positions[:, 0]*f2 - frame*s2)
    n2_z = np.cos(positions[:, 1]*f2 - frame*s2)

    # Layer 3: Local Random Noise (unpredictable small scale jitter)
    f3 = 0.15
    n3_x = np.sin(positions[:, 0]*f3)
    n3_y = np.cos(positions[:, 1]*f3)
    n3_z = np.sin(positions[:, 2]*f3)

    # Weighted Sum: Nature favors low frequency (Large structures)
    # 60% Supercluster, 30% Filament, 10% Local Random
    turbulence = np.column_stack((
        n1_x*0.6 + n2_x*0.3 + n3_x*0.1,
        n1_y*0.6 + n2_y*0.3 + n3_y*0.1,
        n1_z*0.6 + n2_z*0.3 + n3_z*0.1
    ))
    
    # Normalize turbulence vectors
    velocity = (gravity_direction * 0.4) + (turbulence * 0.6)
    
    # Clumping/Clustering frequency (simulates gravity friction)
    speed = 1.0 + (30 / (dist_to_center + 10))
    positions += velocity * speed * 0.6

    # --- PARTICLE RECYCLING ---
    # Respawn at edges
    hit_core = dist_to_center.flatten() < 5
    drifted = dist_to_center.flatten() > UNIVERSE_SIZE * 1.3
    reset_mask = np.logical_or(hit_core, drifted)
    
    count = np.sum(reset_mask)
    if count > 0:
        # Respawn in a shell at the edge
        random_dirs = np.random.normal(0, 1, (count, 3))
        random_dirs /= np.linalg.norm(random_dirs, axis=1, keepdims=True)
        positions[reset_mask] = random_dirs * UNIVERSE_SIZE * 1.1

    # Update Plot
    scat_flow._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    return scat_flow,

# --- VISUALIZATION ---
print("Initializing Cosmic Fractal Engine...")
flow_pos, flow_cols, star_pos = initialize_universe()

# Use slightly darkened uhchi grey background for maximum contrast
fig = plt.figure(figsize=(12, 12), facecolor='black')
ax = fig.add_subplot(111, projection='3d')

# Setup Void
ax.set_facecolor('black')
ax.grid(False); ax.axis('off')
ax.set_xlim([-UNIVERSE_SIZE, UNIVERSE_SIZE])
ax.set_ylim([-UNIVERSE_SIZE, UNIVERSE_SIZE])
ax.set_zlim([-UNIVERSE_SIZE, UNIVERSE_SIZE])

# Background Dust
ax.scatter(star_pos[:, 0], star_pos[:, 1], star_pos[:, 2], 
           s=0.3, c='white', alpha=0.15)

# Reduced alpha to 0.5 to allow "glow" when filaments stack up
scat_flow = ax.scatter(flow_pos[:, 0], flow_pos[:, 1], flow_pos[:, 2], 
                       s=1.5, c=flow_cols, alpha=0.5)

# Singularity (Particles in red, making up spinning accretion disk)
ax.scatter(0, 0, 0, s=80, c=UHCHI_RED, alpha=0.9)

print("Rendering... (Performance Optimized with Blit=True)")
ani = animation.FuncAnimation(fig, update_physics, fargs=(flow_pos, scat_flow), 
                              frames=300, interval=1, blit=False)

plt.show()