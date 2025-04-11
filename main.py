import text_generator as tg

def main():
    generator = tg.TextGenerator()

    while True:
        starter_word = input("Please enter your chosen starter word: ")

        length = int(input("Please enter length of sentence: "))

        generated_sentence = generator.generate(starter_word, length)
        print("\nGenerated Sentence: ")
        print(generated_sentence)

        to_exit = input("\nType exit to leave, any other key to try enter another word: ")
        if to_exit == "Exit" or to_exit == "exit":
            break
        

if __name__ == "__main__":
    main()