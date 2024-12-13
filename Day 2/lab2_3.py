class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def display(self):
        """Display the contents of the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.items)

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return an item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed_item = self.items.pop(0)
        print(f"Dequeued: {removed_item}")
        return removed_item

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

# Demonstration
if __name__ == "__main__":
    queue = Queue()  # Initialize the queue

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.display()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
