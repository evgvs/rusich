from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

markov = MarkovText()

with open('content') as fp:
    for line in fp:
        markov.data(line, part=True)


#print(markov(max_length=16, reply_to='sentence start', reply_mode=ReplyMode.END))

markov.save('markov.json')

#markov = MarkovText.from_file('markov.json')