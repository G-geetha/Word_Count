def word_count(text):
    words = text.split()
    return len(words)
def main():
    
    print("Please enter a sentence or paragraph for word counting.")
    user_input = input("Enter text: ")
    if not user_input.strip():
        print("Error: You entered an empty string. Enter a valid input.")
        return 
    Word_Count = word_count(user_input)
    print(f"The number of words in the given text : {Word_Count}")

if __name__ == "__main__":
    main()
