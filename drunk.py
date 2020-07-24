import random

def main(n):
    total_blocks = 0
    def drunk_walk():
        blocks = 0
        location = 6
        final_destination = "home"
        while (location != 1 and location != 11):
            next_step = random.randint(1, 10)
            if next_step <= 5:
                location -= 1
            elif next_step > 5:
                location += 1
            blocks += 1
        if location == 11: #If the student reaches jail;
            final_destination = "jail"
        print(f"Here we go again... time for a walk!\nWalked {blocks} blockes and,\nLanded at {final_destination}\n")
        return blocks

    for i in range(n):

         total_blocks += drunk_walk()

    average_blocks = total_blocks /n

    print(f"Average # of blocks equals {average_blocks}") #I'm aware that printing and then returning is not a best practice, but the problem says "print";
    return average_blocks

main(5)

