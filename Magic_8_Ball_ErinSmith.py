import random
import time

name = input("What is your name?: ")
print("What's up %s! I can predict your future" %name)

g_1 = "Yes"
g_2 = "Outlook seems good"
g_3 = "Results seems true"
m_1 = "It seems unclear"
m_2 = "Maybe..."
m_3 = "I'm not saying no, but I'm not saying yea.."
b_1 = "No"
b_2 = "Fear the Future"
b_3 = "Idk"
answers = [g_1,g_2,g_3,m_1,m_2,m_3,b_1,b_2,b_3]


while True:
    user_input = input("Please ask me a yes or no question or e[x]it.")
    if user_input.strip() == "x":
        print("Till we meet again... %s" %name)
        break
    else:
        print("Wait a mysterious 3 seconds... ^__^")
        time.sleep(3)
        print(random.choice(answers))
    
