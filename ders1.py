#sözlük
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "ROFL": "bir şakaya karşılık cevap",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek" 
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    new_word = input("eklemek istediğiniz kelimeyi yazın (hepsini büyük harflerle yazın!):")
    meme_dict.append(new_word)
