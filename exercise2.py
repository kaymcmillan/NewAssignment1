score = int(input("What's your credit score? "))

if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        category = "Excellent - Loan Approved"
        approved = True
    elif score >=700:
        category = "Good - Loan Approved with Review"
        approved = True
    elif score >= 600:
        category = "Fair - Loan Conditional"
        approved = False
    else:
        category = "Poor - Loan Denied"
        approved = False

if approved:
    rate_message = "Interest rate: Low"
else:
    rate_message = "Seek credit improvement."

print(f"{category}. {rate_message}")