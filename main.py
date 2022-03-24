def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import pandas as pd
import matplotlib.pyplot as plt

jsonData = pd.read_json("./data/postcodes.json")

csvData = pd.read_csv("./data/price_paid_records_small.csv")

# Make the town names upper case from the JSON file
jsonData["town"] = jsonData["town"].str.upper()

greenWich = jsonData.loc[jsonData.town == "GREENWICH"].copy()

# Create data frames that are above and below GreenWitch
addressesAboveZeroLat = jsonData.loc[jsonData.longitude > 0].copy()
addressesBelowZeroLat = jsonData.loc[jsonData.longitude < 0].copy()

addressesAboveZeroLat.to_csv("./dataOutput/dataOutputAboveZeroLong.csv")
addressesBelowZeroLat.to_csv("./dataOutput/dataOutputBelowZeroLong.csv")

# Match the town data of the JSON data to the
matchedAbove0TownData = addressesAboveZeroLat.set_index("town").join(csvData.set_index("Town/City"), how="inner")
matchedBelow0TownData = addressesBelowZeroLat.set_index("town").join(csvData.set_index("Town/City"), how="inner")

matchedAbove0TownData.to_csv("./dataOutput/joinedDatasetAbove0.csv")
matchedBelow0TownData.to_csv("./dataOutput/joinedDatasetBelow0.csv")

plt.figure(figsize=(6, 6))

plt.scatter(matchedAbove0TownData['longitude'], matchedAbove0TownData['latitude'], c="g", alpha=0.2, s=5*9)
plt.scatter(matchedBelow0TownData['longitude'], matchedBelow0TownData['latitude'], c='r', alpha=0.2, s=5*9)
plt.scatter(greenWich['longitude'], greenWich['latitude'], c='b', s=30*9, alpha=0.2)

plt.xlabel("Latitude", fontsize=14, labelpad=15)
plt.ylabel("Longitude", fontsize=14, labelpad=15)

plt.show()

