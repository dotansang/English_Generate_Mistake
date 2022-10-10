import copy
import random

import simplejson
from tqdm import tqdm

from neuspell_noising import WordReplacementNoiser, ProbabilisticCharacterReplacementNoiser, CharacterReplacementNoiser
from similar_word import replace_word_noiser


def detection_label_generate(error_text, correct_text):
    labels = []
    er_spl = error_text.split()
    cr_spl = correct_text.split()
    if len(er_spl) != len(cr_spl):
        print(er_spl)
        print(cr_spl)
        print()
        return
    for i in range(len(er_spl)):
        if er_spl[i] != cr_spl[i]:
            labels.append(1)
        else:
            labels.append(0)
    return labels


with open("./data/wikihow_samples_preprocess.txt") as f:
    example_texts = [text.strip() for text in f]
# example_texts = [
#     "this is an example sentence to demonstrate neuspell_noising in the beautiful neuspell repository.",
#     "here is another such amazing example !!"
# ]


word_repl_noiser = WordReplacementNoiser(language="english")
word_repl_noiser.load_resources()
char_repl_noiser = CharacterReplacementNoiser()
char_repl_noiser.load_resources()
prob_repl_noiser = ProbabilisticCharacterReplacementNoiser()
prob_repl_noiser.load_resources()

noise_texts = []
# for sentence in example_texts:
#     select = random.choice([1, 2, 3, 4, 5])
#     noise = None
#     if select == 1:
#         noise = word_repl_noiser.noise([sentence])[0]
#     elif select == 2:
#         noise = char_repl_noiser.noise([sentence])[0]
#     # elif select == 3:
#     #     noise = prob_repl_noiser.noise([sentence])[0]
#     # elif select == 4:
#     #     noise = replace_word_noiser(sentence)
#     else:
#         noise = noise_texts.append(sentence)
#     if noise:
#         noise_texts.append(noise)
#     else:
#         noise_texts.append(sentence)


# noise_texts = word_repl_noiser.noise(example_texts)
noise_label = []
for i in range(len(noise_texts)):
    n = detection_label_generate(noise_texts[i], example_texts[i])
    if n:
        noise_label.append(n)

final_example = []
for i in tqdm(range(len(example_texts))):
    example = {
        "correct_text": example_texts[i],
        "noise_text": noise_texts[i],
        "detection_label": noise_label[i],
        "noises": []
    }
    noise_split = noise_texts[i].split()
    correct_text = example_texts[i].split()
    for u in range(len(noise_split)):
        # print(noise_label[i][u])
        if noise_label[i][u] == 1:
            example["noises"].append({
                "start": u,
                "end": u + 1,
                "noise_value": noise_split[u],
                "correct_value": correct_text[u]
            })
    final_example.append(example)

json_data = simplejson.dumps(final_example, ensure_ascii=False, encoding='utf-8', indent=4)
with open('./generated_noise/wikihow_example.json', 'w', encoding='utf8') as json_file:
    json_file.write(json_data)

# text = "I wan t to playwith you"
# print(text.split()[1:3])

# for i in range(len(example_texts)):
#     example_split = example_texts[i].split()
#     mistake_split = noise_texts[i].split()
#     for
#
# prob_char_repl_noiser = ProbabilisticCharacterReplacementNoiser(language="english")
# prob_char_repl_noiser.load_resources()
# noise_texts = prob_char_repl_noiser.noise(example_texts)
# print("*"*10)
# print(noise_texts)
#
# char_repl_noiser = CharacterReplacementNoiser(language="english")
# char_repl_noiser.load_resources()
# noise_texts = char_repl_noiser.noise(example_texts)
# print("*"*10)
# print(noise_texts)
