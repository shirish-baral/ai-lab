class Stack:
    def __init__(self):
        self.stack = []

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Stack:", self.stack[::-1])

    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element}.")

    def pop(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print(f"Popped {self.stack.pop()}.")

def main():
    stack = Stack()

    while True:
        print("\nChoose an operation: a) Initialize b) Display c) Push d) Pop e) Exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'a':
            stack = Stack()
            print("Stack initialized.")
        elif choice == 'b':
            stack.display()
        elif choice == 'c':
            element = input("Enter element: ")
            stack.push(element)
        elif choice == 'd':
            stack.pop()
        elif choice == 'e':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
