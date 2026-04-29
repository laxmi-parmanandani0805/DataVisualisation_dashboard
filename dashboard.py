import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- 1. DATA GENERATION (Random) ---
np.random.seed(2026)
continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
data_size = 300

data = {
    'Country': [f'Country_{i}' for i in range(data_size)],
    'Continent': np.random.choice(continents, data_size),
    'GDP_per_Capita': np.random.lognormal(mean=9, sigma=1.2, size=data_size),
    'Life_Expectancy': np.random.normal(loc=72, scale=8, size=data_size),
    'Population_Millions': np.random.uniform(1, 1400, data_size),
    'Healthcare_Index': np.random.uniform(20, 100, data_size)
}
df = pd.DataFrame(data)
df['Life_Expectancy'] = df['Life_Expectancy'].clip(45, 90)

# --- 2. USER INPUT FOR PLOT 1 ---
print("--- Enter Your Custom Data for Plot 1 ---")
try:
    user_gdp = float(input("Enter GDP per Capita (e.g., 45000): "))
    user_life = float(input("Enter Life Expectancy (e.g., 82): "))
    user_label = input("Enter a name for your data point (e.g., My Country): ")
    
    # Create user data point
    user_point = pd.DataFrame({
        'GDP_per_Capita': [user_gdp],
        'Life_Expectancy': [user_life],
        'Label': [user_label]
    })
except ValueError:
    print("Invalid numeric input. Using default values for visualization.")
    user_point = pd.DataFrame({'GDP_per_Capita': [30000], 'Life_Expectancy': [75], 'Label': ['Default']})

# --- 3. DASHBOARD STYLING ---
sns.set_theme(style="ticks")
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('Global Intelligence Dashboard (Hybrid Mode)', 
             fontsize=22, fontweight='bold', color='#2c3e50', y=0.98)

# --- 4. THE VISUALIZATIONS ---

# PLOT 1: Wealth vs. Health (USER INPUT ONLY)
# We plot the random data in light grey to provide context
sns.scatterplot(ax=axes[0,0], data=df, x='GDP_per_Capita', y='Life_Expectancy', 
                color='#d1d8e0', alpha=0.3, label='Random Background')

# Plotting the User Input as a bright, solid colored circle
sns.scatterplot(ax=axes[0,0], data=user_point, x='GDP_per_Capita', y='Life_Expectancy', 
                color='#e67e22', s=250, alpha=1.0, edgecolor='black', label=f'User: {user_label}')

axes[0,0].set_xscale('log')
axes[0,0].set_title('Plot 1: User Highlighted Wealth vs Health', fontsize=14, fontweight='bold')
axes[0,0].legend()

# PLOT 2: Healthcare Distribution (Random Data Only)
sns.boxplot(ax=axes[0,1], data=df, x='Continent', y='Healthcare_Index', palette='Set2')
axes[0,1].set_title('Plot 2: Healthcare Index (Random)', fontsize=14)

# PLOT 3: Regional Performance Averages (Random Data Only)
pivot_data = df.groupby('Continent')[['GDP_per_Capita', 'Healthcare_Index']].mean()
sns.heatmap(ax=axes[1,0], data=pivot_data, annot=True, cmap='Blues', fmt=".1f")
axes[1,0].set_title('Plot 3: Regional Averages (Random)', fontsize=14)

# PLOT 4: Life Expectancy Density (Random Data Only)
sns.kdeplot(ax=axes[1,1], data=df, x='Life_Expectancy', hue='Continent', fill=True, alpha=0.3)
axes[1,1].set_title('Plot 4: Health Density (Random)', fontsize=14)

# --- 5. CLEANUP ---
sns.despine()
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.95, top=0.88, wspace=0.25, hspace=0.35)

plt.show()