#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 28, 2021

user = int(input("Enter amount of social media followers:"))
if user < 0:
    print("Your influencer tier is: Error")
elif user < 1000:
    print("Your influencer tier is: Hyper Influnecer")
elif user < 10000:
    print("Your influencer tier is: Nano Influencer")
elif user < 100000:
    print("Your influencer tier is: Micro Influencer")
elif user < 500000:
    print("Your influencer tier is: Mid-Tier Influencer")
elif user < 1000000:
    print("Your influencer tier is: Macro Influencer")
elif user > 1000000:
    print("Your influencer tier is: Celebritiy Influencer")
