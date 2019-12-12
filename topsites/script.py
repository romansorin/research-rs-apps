limit = 10001
lower = 1
interval = 100
sets = []

for i in range(lower, limit, interval):
    intervals = [i, i + interval - 1]
    print(f"/api?Action=TopSites&Count={interval}&CountryCode=US&ResponseGroup=Country&Output=json&Start={intervals[0]}")
