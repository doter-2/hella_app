from dotenv import load_dotenv
import os

load_dotenv()
my_variable = os.getenv('MY_KEY')
print(my_variable)

def main():
    print("Hi gitler ")

name = "Tom"

if __name__ == "__main__":
    main()

