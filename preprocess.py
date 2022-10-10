import re

non_unicode = re.compile(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', re.IGNORECASE | re.DOTALL)

# uncommon_punc = re.compile(r"[$|&@©ø[\]'}{;„”»«‘’“¡¿·´¯§~³²ª¤¢¥½¬〟¶¸°÷º×〝〞❛❜‹›❝❞＂]")
# duplicate_punc = re.compile(r"([)(,`.\-\\?!/:\"\'_=+*])\1{2,}")
normalize_punc = re.compile(r" *([$<>|&@©)({}ø;„»«.,‘\-’“”〟〝〞‹›❝❞`\\?%!:+*]+) *")


def prepro(t):
    if "http" in t:
        return

    t = non_unicode.sub(r" ", t)
    t = normalize_punc.sub(r" \1 ", t)

    t = " ".join([i for i in t.split()])
    return t


with open("./data/wikihow_samples.txt") as f:
    example = [text.strip() for text in f]

# for text in example:
#     if text != prepro(text):
#         print(text)
#         print(prepro(text))
#         print()
preprocessed = [prepro(t) for t in example]
with open("./data/wikihow_samples_preprocess.txt","w") as f:
    for item in preprocessed[:1000]:
        if item:
            f.write(item+"\n")
