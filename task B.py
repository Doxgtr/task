temperatures = [72, 75, 78, 82, 91, 95, 88]
threshold = 90

i = 0

while i < len(temperatures):
    if temperatures[i] > threshold:
        print("Temperature:", temperatures[i])
        print("Index:", i)
        break
    i += 1