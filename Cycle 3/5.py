import matplotlib.pyplot as plt
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

transport_modes = ['Walking', 'cycling', 'car', 'Bus', 'train']
frequencies = [29, 15, 35, 18, 3]

plt.bar(transport_modes, frequencies, width=0.1, color='green')

plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

plt.show()
