import random

def create_puzzle(word, difficulty):
    if difficulty == "easy":
        num_of_letters = int(len(word) * 0.6)
    #Zorluk seviyesi easy ise kelime uzunluğunun %60'ı kadar harf verilir
    elif difficulty == "medium":
        num_of_letters = int(len(word) * 0.4)
    # Zorluk seviyesi medium ise kelime uzunluğunun %40'ı kadar harf verilir
    else:
        num_of_letters = int(len(word) * 0.2)
     # Zorluk seviyesi hard ise kelime uzunluğunun %20'si kadar harf verilir
    puzzle = ["_" for i in range(len(word))]
    word = list(word)
    random_indices = random.sample(range(0, len(word)), num_of_letters)
    for i in random_indices:
        puzzle[i] = word[i]
    random.shuffle(puzzle)
    return puzzle

def main():
    word_list = ["muş", "istanbul", "selanik", "ağrı", "şırnak", "hakkari"]
    word = random.choice(word_list)
    difficulty = input("Zorluk seviyesi (kolay, orta, zor): ")
    puzzle = create_puzzle(word, difficulty)
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    while "_" in puzzle and incorrect_guesses < max_incorrect_guesses:
        print("Kelimeyi tamamlar mısın? : ", " ".join(puzzle))
        user_guess = input("Cevabınız: ").lower()

        if user_guess == word:
            print("Harikasın, sen kazandın bu kelime ", word)
            break
        else:
            incorrect_guesses += 1
            print("Doğru değil: ", incorrect_guesses)

    else:
        print("Kaybettin, bu kelime ", word)

if __name__ == "__main__":
    main()
