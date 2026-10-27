"""Small Python programming exercises for beginners."""


def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def fibonacci(count: int) -> list[int]:
    """Return the first `count` Fibonacci numbers."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def count_vowels(text: str) -> int:
    """Count vowels in a string."""
    return sum(1 for character in text.lower() if character in "aeiou")


def main() -> None:
    print("Python Programming Collection")
    print("1. Factorial")
    print("2. Fibonacci sequence")
    print("3. Count vowels")
    choice = input("Choose an exercise (1-3): ").strip()

    try:
        if choice == "1":
            number = int(input("Enter a non-negative integer: "))
            print(f"{number}! = {factorial(number)}")
        elif choice == "2":
            count = int(input("How many Fibonacci numbers? "))
            print(fibonacci(count))
        elif choice == "3":
            text = input("Enter text: ")
            print(f"Vowel count: {count_vowels(text)}")
        else:
            print("Please choose 1, 2, or 3.")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
