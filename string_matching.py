"""
Efficient string matching (Aho-Corasick algorithm)

Author: Hélène Perée

Last modified date: 01/08/18

Python 3 (no libraries)
"""

def importText(filename):
    """
    :return: the text converted in lowercase (str).
    """
    file = open(filename)
    text = file.read()
    file.close()

    return text.lower()


def gotoFunction(keywords, symbols): # algorithm 2
    """
    This function computes the goto dictionary and starts computing the output
    dictionary.

    :return goto: dictionary where keys (tuples) = (current state, current symbol)
    and values (int) = the next state composing the same keyword
                      
    :return output: dictionary where keys (int) = states at which keywords end
    and values (list of str) = one corresponding keyword
    """
    goto = {}
    output = {}
    newstate = 0 # start state
    
    for i in range(len(keywords)):
        state = 0
        j = 0

        # we follow the path if the keyword overlaps with one already in it
        while (state, keywords[i][j]) in goto.keys():
            state = goto[(state, keywords[i][j])]
            j += 1

        # we add a path in the graph until the keyword is completely added
        for p in range(j, len(keywords[i])):
            newstate += 1 # not yet used state
            goto[(state, keywords[i][p])] = newstate
            state = newstate

        # the last state corresponds to the end of the keyword
        output[state] = [keywords[i]]

    # all symbols found in keywords but not in first position point to start state
    for a in symbols:
        if (0, a) not in goto.keys():
            goto[(0, a)] = 0
            
    return goto, output


def failureFunction(keywords, symbols, goto, output): # algorithm 3
    """
    This function computes the failure dictionary and finishes computing the
    output dictionary. The depth of a given state corresponds to the length of
    the shortest path from the start state (0) to this given state.

    :return failure: dictionary where keys (int) = states
    and values (int) = the previous state with the same symbol or 0
    
    :return output: dictionary where keys (int) = states at which keywords end
    and values (list of str) = all corresponding keywords
    """
    failure = {}
    queue = []

    # we compute depth = 1
    for a in symbols:
        if goto[(0, a)] != 0:
            s = goto[(0, a)]
            queue.append(s)
            failure[s] = 0 # depth -1 = 0
            
    # we compute depth > 1
    while queue != []:
        r = queue[0] # first-in
        del queue[0] # first-out

        for a in symbols:
            if (r, a) in goto.keys():
                s = goto[(r, a)]
                queue.append(s)
                state = failure[r] # state of depth -1

                # since (0, any a) is in the grap, a state will always be found
                while (state, a) not in goto.keys():
                    state = failure[state]

                # depth -1 = previous state with same symbol or 0
                failure[s] = goto[(state, a)]

                # failure[s] is in output if a keyword ends at this state
                if failure[s] in output.keys():
                    output[s].extend(output[failure[s]])
                    
    return failure, output


def patternMatchingMachine(text, keywords): # algorithm 1
    """
    This function prints the ending position(s) of the keywords in the text.
    """
    symbols = set(list(''.join(keywords))) # letters found in the keywords

    goto, output = gotoFunction(keywords, symbols)
    failure, output = failureFunction(keywords, symbols, goto, output)

    state = 0
    
    for i in range(len(text)):
        if text[i] in symbols:

            # we look for another path or 0
            while (state, text[i]) not in goto.keys() and state != 0:
                state = failure[state] 

            # we progress in new path or start again at start state
            state = goto[(state, text[i])] 

            if state in output.keys():
                print(i+1, output[state])
                


#x = "ushers"
#k = ["he", "she", "his", "hers"]

#x = "ATGGTCGGT"           
#k = ["GTC", "TC", "GGA", "CGGT"]

x = importText("input.txt") # if text import: use lowercase keywords
k = ["pattern", "tree", "state", "prove", "the", "it"]

patternMatchingMachine(x, k)
