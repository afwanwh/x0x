#this apps is open

#Let's start with introduction

print "Hi, I am x0x. Could we introduce ourselves? (yes/no)"
answer = raw_input()
if answer.lower() == 'yes':
    print "Okay, what is your name?"
    name = raw_input()
    print "Hi", name
    print "Nice to meet you."
    print "What are you going to do?"
    print '1. Say "good bye"'
    print '2. Say "Thank you"'
    answer = raw_input()
    if answer == '1':
        print 'Well, good bye', name
    elif answer == '2':
        print 'Sakalangkong', name
    else:
        print 'You choose wrong answer, I am terminated.'
        print 'bye'
elif answer.lower() == 'no':
    print "thank you"
else:
    print "your answer is wrong"
    print "Please come back later. Thank you!"
    print "yoyoi oke"
