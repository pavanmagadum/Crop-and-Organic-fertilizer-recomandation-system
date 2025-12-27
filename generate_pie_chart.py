import matplotlib.pyplot as plt

# Feature importance data (from your Random Forest model)
features = ['Rainfall', 'Temperature', 'Potassium (K)', 'Humidity', 
            'Nitrogen (N)', 'Phosphorus (P)', 'pH']
importance = [28.3, 22.1, 15.7, 10.4, 9.8, 8.5, 5.2]

# Create figure
plt.figure(figsize=(10, 8))

# Define colors - green/blue for climate, orange/red for soil
colors = ['#10B981',  # Rainfall (green - climate)
          '#3B82F6',  # Temperature (blue - climate)
          '#F59E0B',  # Potassium (orange - soil)
          '#8B5CF6',  # Humidity (purple - climate)
          '#EF4444',  # Nitrogen (red - soil)
          '#EC4899',  # Phosphorus (pink - soil)
          '#6B7280']  # pH (gray - soil)

# Create pie chart
wedges, texts, autotexts = plt.pie(
    importance, 
    labels=features, 
    autopct='%1.1f%%',
    colors=colors, 
    startangle=90,
    textprops={'fontsize': 13, 'weight': 'bold'},
    pctdistance=0.85
)

# Make percentage text white for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add title
plt.title('Feature Importance Distribution\nClimate Factors vs Soil Factors', 
          fontsize=18, weight='bold', pad=20)

# Add text annotation showing climate vs soil split
plt.text(0, -1.3, 'Climate Factors (Rainfall + Temperature + Humidity): 60.8%', 
         ha='center', fontsize=12, weight='bold', color='#10B981',
         bbox=dict(boxstyle='round', facecolor='#E8F5E9', edgecolor='#10B981', linewidth=2))

plt.text(0, -1.5, 'Soil Factors (N + P + K + pH): 39.2%', 
         ha='center', fontsize=12, weight='bold', color='#F59E0B',
         bbox=dict(boxstyle='round', facecolor='#FFF3E0', edgecolor='#F59E0B', linewidth=2))

# Ensure circular pie chart
plt.axis('equal')

# Save with high resolution
plt.tight_layout()
plt.savefig('screenshot_pie_chart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("✅ Pie chart saved as 'screenshot_pie_chart.png'")
print("📊 File location: c:\\Users\\sw\\Desktop\\climate_aware_final_project\\screenshot_pie_chart.png")
print("\n📸 Next steps:")
print("1. Check the saved image")
print("2. Upload it to Overleaf with your IEEE paper")
print("3. The LaTeX code is already updated to include this figure!")

# Show the plot
plt.show()
