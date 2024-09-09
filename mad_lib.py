# Mad Lib example for functions.

def madlib(verb_1,verb_2,verb_3,noun_1,noun_2,noun_3,adjective_1,adjective_2):
    '''Mad lib fucntion'''
    story =f'''
It was a {adjective_1} day when I decided to take my [breed of dog], named 
[dog’s name], to the dog park. As soon as we arrived, [dog’s name] spotted a 
[breed of dog] chasing a {noun_1}. My dog immediately {verb_1} over to join in.
They ran around the park, their tails wagging with excitement.

Nearby, a [breed of dog] was trying to dig up a {noun_2}, while its owner 
{verb_2} and laughed. The scene was very {adjective_2}, especially when a 
small [breed of dog] began to race around, barking and playing with the other 
dogs.

As the day went on, the park became busier with dogs of all sizes. A massive 
[breed of dog] bounded over and knocked over a {noun_3} in the process. The 
dogs all played together until they were exhausted. My dog, [dog’s name], 
{verb_3} back to me, tired but happy after a long day of fun.
'''
    return story

output_story = madlib('ran','laughed','trotteed','ball','strick','bench','sunny','funny')

print(output_story)
