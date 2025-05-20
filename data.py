plt.figure(figsize=(12, 6))
sns.barplot(data=top_cases, x='location', y='total_cases', palette='Reds')
plt.xticks(rotation=45)
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.tight_layout()
plt.show()


# Select a country (e.g., India)
india = df[df['location'] == 'India']

plt.figure(figsize=(12, 6))
plt.plot(india['date'], india['new_cases'], label='Daily New Cases', color='blue')
plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


plt.figure(figsize=(10, 5))
sns.histplot(df['new_deaths'].dropna(), bins=50, color='purple')
plt.title("Distribution of Daily New Deaths Globally")
plt.xlabel("New Deaths")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=latest_data, x='total_cases', y='total_deaths', hue='continent')
plt.xscale('log')
plt.yscale('log')
plt.title("Total Cases vs. Total Deaths (Log Scale)")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.show()
