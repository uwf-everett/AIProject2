import text_generator as tg

def main():
    generator = tg.TextGenerator()

    while True:
        starter_word = input("Please enter your chosen starter word.")

        length = input("Please enter length of sentence.")
        #insert checks for legal input

        generated_sentance = generator.generate(starter_word, length)
        print(generated_sentance)

        to_exit = input("Type exit to leave, any other key to try enter another word.")
        if to_exit == "Exit" or to_exit == "exit":
            break
        

if __name__ == "__main__":
    main()