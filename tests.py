import math


def compare_dictionaries(d1, d2):
    """
    """
    if d1 == {}:
        return -50

    score = 0
    total_d1 = sum(d1.values())

    for i in d2:
        if i in d1:

            probability = d1[i] / total_d1
            score += math.log(probability) * d2[i]
        else:

            default_probability = 0.5 / total_d1
            score += math.log(default_probability) * d2[i]

    print(score)


# shakespeare_dict = {'love': 50, 'spell': 8, 'thou': 42}
# mystery_dict = {'love': 3, 'thou': 1, 'potter': 2, 'spam': 4}
# compare_dictionaries(shakespeare_dict, mystery_dict)