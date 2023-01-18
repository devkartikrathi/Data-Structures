plt.plot(df['itr'], df['m'], color='pink', label='Merge Sort')
plt.plot(df['itr'], df['q'], color='orange', label='Quick Sort')
plt.plot(df['itr'], df['h'], color='cyan', label='Heap Sort')
plt.legend()