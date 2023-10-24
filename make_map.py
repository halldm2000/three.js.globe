import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a figure and axis with an equirectangular projection, removing all padding
fig, ax = plt.subplots(figsize=(16, 8), subplot_kw={'projection': ccrs.PlateCarree()}, frameon=False)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Add ocean, continents, and coastlines
ax.add_feature(cfeature.OCEAN, facecolor='white')  # Oceans in white
ax.add_feature(cfeature.LAND, facecolor='#D3D3D3')  # Continents in light gray
ax.add_feature(cfeature.COASTLINE, edgecolor='#000000')  # Coastlines in darker gray

# Set extent to cover the whole globe
ax.set_extent([-180, 180, -90, 90])

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

# Remove the axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Save the figure
plt.savefig('./images/equirectangular_map_texture.png', dpi=600, pad_inches=0, transparent=True)

plt.show()
