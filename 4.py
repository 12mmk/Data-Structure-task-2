# given a list of votes

votes = ["blue", "red", "blue", "green", "red", "blue"]

# write a script to count the ccurences of blue. 
# if the count is 3 or higher print blue wins 
# other wise blue did not win

total_blue_votes = votes.count("blue")

if total_blue_votes >= 3:
    print("Blue wins!")
else:
    print("Blue did not win.")
    