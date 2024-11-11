import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_2022_2023 = pd.DataFrame({
    "Category": ["Organic ", "Delta", "Sigma", "Population", "Waste"],
    "2023": [0.2618068146, 0.9661730948, 0.993859631, 0.8400325925, 0.9177923219],
    "2022": [0.3494012477, 0.9433275965, 0.9800176788, 0.831536957, 0.9136508228]
})

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35
x = np.arange(len(data_2022_2023["Category"]))

bars_2023 = ax.bar(x - width/2, data_2022_2023["2023"], width, label="2023", color='skyblue')
bars_2022 = ax.bar(x + width/2, data_2022_2023["2022"], width, label="2022", color='salmon')

for bars in [bars_2023, bars_2022]:
    for bar in bars:
        height = bar.get_height()
        ax.plot(bar.get_x() + bar.get_width() / 2, height, 'ro')

ax.set_ylim(0, 1.1)
ax.set_xlabel("Independent Variable", fontsize=14)
ax.set_ylabel("Correlation with percentage of active rat signs", fontsize=14)
ax.set_title("Comparison of Correlation for Different Variables (With Grouping)", fontsize=16)

ax.set_xticks(x)
ax.set_xticklabels([r"$org^j$", r"$\delta^j$", r"$\sigma^j$", r"$p^j$", r"$W^j$"], rotation=45, fontsize=12)

ax.legend(fontsize=12)

plt.tight_layout()
plt.show()






new_data = pd.DataFrame({
    "Category": ["Organic Waste", "Delta", "Sigma", "Population", "Waste"],
    "2023": [0.4160480984, 0.426396817, 0.4502023353, 0.254948341, 0.4000397373],
    "2022": [0.6059561026, 0.5961270735, 0.6610450048, 0.4296790687, 0.5572358496]
})

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35
x = np.arange(len(new_data["Category"]))

bars_2023 = ax.bar(x - width/2, new_data["2023"], width, label="2023", color='skyblue')
bars_2022 = ax.bar(x + width/2, new_data["2022"], width, label="2022", color='salmon')

for bars in [bars_2023, bars_2022]:
    for bar in bars:
        height = bar.get_height()
        ax.plot(bar.get_x() + bar.get_width() / 2, height, 'ro')

ax.set_ylim(0, 1.1)
ax.set_xlabel("Independent Variable", fontsize=14)
ax.set_ylabel("Correlation with percentage of active rat signs", fontsize=14)
ax.set_title("Comparison of Correlation for Different Variables (Without Grouping)", fontsize=16)

ax.set_xticks(x)
ax.set_xticklabels([r"$org_n$", r"$\delta_n$", r"$\sigma_n$", r"$p_n$", r"$W_n$"], rotation=45, fontsize=12)

ax.legend(fontsize=12)

plt.tight_layout()
plt.show()
