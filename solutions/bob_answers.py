__author__ = 'yury'

# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.

# Example: "Whoa, chill out!" == solution("1, 2, 3 GO!")

def solution(say):
    if "?" in say:
        return "Sure."
    elif "!" in say:
        return "Whoa, chill out!"
    elif not say.split():
        return "Fine. Be that way!"
    return "Whatever."
