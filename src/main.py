import good, bad

def main():
    while True:
        print("\nCheck the tests:")
        print("1. Good test")
        print("2. Bad test")
        print("0. Exit")

        choice = input("Enter the test number: ")

        if choice == '1':
            good.run_gallery_test()
        elif choice == '2':
            bad.run_gallery_test()
        elif choice == '0':
            print("Ending...")
            break
        else:
            print("Miss choise. Try again.")

if __name__ == "__main__":
    main()
