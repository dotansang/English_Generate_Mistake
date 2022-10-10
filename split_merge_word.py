import random


def split_word(word, max_split):
    assert max_split > 1, "max_split must greater than 1"
    max_length = len(word)
    if max_split > max_length:
        max_split = max_length
    split_points = sorted(random.sample(range(max_length), k=max_split - 1))
    return [w for w in [word[0:split_points[0]]] + [word[i:j] for i, j in zip(split_points, split_points[1:] + [None])]
            if w]


def split_word_noiser(noised_sentence, detect_labels, max_split=2, noise_rate=0.1):
    for i in range(len(noised_sentence)):
        if detect_labels[i] == 0 and random.random() <= noise_rate:
            noise = split_word(noised_sentence[i], max_split=max_split)
            if len(noise) > 1:
                noised_sentence[i] = noise
                detect_labels[i] = 2
    return noised_sentence, detect_labels


def find_sub_list(sl, l):
    results = []
    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if l[ind:ind + sll] == sl:
            results.append((ind, ind + sll - 1))
    return results


def merge_word_noiser(correct_sentence, noised_sentence, detect_labels, merge_length=2, noise_rate=0.3):
    valid_index = find_sub_list([0] * merge_length, detect_labels)
    print(valid_index)
    for start, end in valid_index:
        correct_sentence = correct_sentence[:start] + correct_sentence[start:end + 1] + correct_sentence[end:]
        noised_sentence = noised_sentence[:start] + ["".join(correct_sentence[start:end])] + noised_sentence[end:]
        detect_labels = detect_labels[:start] + [3] + detect_labels[end:]
    return correct_sentence, noised_sentence, detect_labels