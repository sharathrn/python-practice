score = 0.6
if score >= 0.9:
    label = "Excellent"
elif score >= 0.8:
    label = "Good"
elif score >= 0.7:
    label = "Average"
else:
    label = "Poor"
print(label)
