import hashlib

"""
La siguiente clase posee las 5 funcinoes hash mas usadas en la actualidad
"""

class Hasher:
    def __init__(self, cadena):
        self.cadena = cadena

    def hash_md5(self):
        return hashlib.md5(self.cadena.encode()).hexdigest()

    def hash_sha1(self):
        return hashlib.sha1(self.cadena.encode()).hexdigest()

    def hash_sha256(self):
        return hashlib.sha256(self.cadena.encode()).hexdigest()


    def hash_blake2(self):
        return hashlib.blake2b(self.cadena.encode()).hexdigest()


# Ejemplo de uso
if __name__ == "__main__":
    cadenas = ['password123',  
"qwerty",  
"12345678",  
"admin",  
"letmein",  
"welcome",  
"monkey",  
"abc123",  
"football",  
"123123",  
"sunshine",  
"iloveyou",  
"starwars",  
"12345",  
"dragon",  
"trustno1",  
"superman",  
"batman",  
"chocolate",  
"shadow",  
"qwertyuiop",  
"1qaz2wsx",  
"asdfghjkl",  
"baseball",  
"computer",  
'princess',  
'master',  
'654321',  
'password1',  
'qazwsx',  
'football123',  
'trustme',  
'hello123',  
'summer2018',  
'love123',  
'welcome123',  
'cheese',  
'sunshine123',  
'123qwe',  
'hunter2',  
'secret',  
'password2024',  
'michael',  
'harley',  
'pepper',  
'chocolate123',  
'ginger',  
"qC7u9VdW", 
    "uG6xZbS8", 
    "hQ2tLmB5", 
    "pF0iXrD3", 
    "wE9aNxT1", 
    "tY7pVuZ0", 
    "kO3bGzS7", 
    "fN8hRjL4", 
    "vK2iBwX9", 
    "aC6tPzQ2", 
    "mH9wZxR8", 
    "lF1bKqY3", 
    "sJ7cNmT0", 
    "rE4dWqU5", 
    "gV3oYkB9", 
    "cX2lAuF7", 
    "nS8pVrD0", 
    "dQ1mXwY3", 
    "bL6zHaF9", 
    "kT5oLpZ2", 
    "uJ3qWhV0", 
    "vC7sXiT4", 
    "tF9oZwQ1", 
    "pK6uNfB8", 
    "jG2rWsL0", 
    "wR4bVzM7", 
    "hX1oQpT5", 
    "yL9sCkZ0", 
    "aN6iYwF8", 
    "rD2tBvX7", 
    "cE4zPjK3", 
    "bW1lTqQ6", 
    "fV9hXrD5", 
    "jY7pKzS0", 
    "gC2oLmN8", 
    "kX3wVqP4", 
    "mJ9rZfT0", 
    "pW8sQnD7", 
    "uF1bYtL6", 
    "hG5xNxZ2", 
    "lR4pKsV9", 
    "vT0oYbX6", 
    "tD7pJfQ2", 
    "wC9nKmL3", 
    "dX4zYkF0", 
    "yV5oWbT2", 
    "cQ6pLwX1", 
    "hB9tNfJ7", 
    "bV2gYkD8", 
    "pQ4oSxL0", 
    "fT1rZbM3", 
    "kC7nXjY2", 
    "wB6oFvT0", 
    "rY3lNzP9", 
    "vJ8pWqL5", 
    "tG2oKxD7", 
    "pN1bXfY3", 
    "jW9rLqT6", 
    "hF4vYkB2", 
    "sP7oDgX0", 
    "gC8bQyW3", 
    "vL1nTzF4", 
    "tY5mKpS0", 
    "wX9fNqD2", 
    "rG3zLkP8", 
    "jF0oVxW7", 
    "hC2rQpM6", 
    "bY1tTzV9", 
    "kP7oLxD3", 
    "wF5sQnY0", 
    "tJ9rVbX2", 
    "pL4kWqS7", 
    "gB3yNfZ1", 
    "vT6oPjL8", 
    "wJ0nXkQ5", 
    "hY9rVdT2", 
    "jF7oBqS0", 
    "kG3pWzL4", 
    "lX1rYvN6", 
    "tC8oLqD7", 
    "pJ5rKzX0", 
    "wF3sQbT9", 
    "yL2nVhD6", 
    "gR7pW1X4", 
    "vK9tYfB3", 
    "pC0jLxT8", 
    "bR6oXfN1", 
    "hJ2wYvT7", 
    "kL5rVqX9", 
    "sQ8nB0P3", 
    "vX2yWkD4", 
    "pJ1tL6oF", 
    "hY9rQdV5", 
    "bF4sN2kX", 
    "rJ3oVtL8", 
    "wB0xQ9N", 
    "gL6yX5V", 
    "vJ7rQ2p", 
    "tP9yL0D", 
    "pF3oK6W", 
    "wR4nXb7", 
    "hV5jYkT", 
    "bY2nQ8R", 
    "pL0sK7X", 
    "gC3tW9L", 
    "yD6vXbF", 
    "tQ8pK1L", 
    "rJ9oV5B", 
    "kT7wF2n", 
    "lX0yJ3V", 
    "sB4qP9N", 
    "gY1rL8X", 
    "wV2nK5o", 
    "pF0tL7J", 
    "rQ3oX9V", 
    "vG6bK1T", 
    "tP5nW2L", 
    "hJ4rF9Q", 
    "kL3tY6X", 
    "sR2vD8P", 
    "bN1oQ4L", 
    "yJ0xV7T", 
    "pC9tW5X", 
    "hV3nF2Y", 
    "kJ4yL6X", 
    "vD7pQ0B", 
    "rF8nX5L", 
    "wT2kV3Y", 
    "tP1jL9F", 
    "bQ7oX3K", 
    "hY9rL2D"
    ]

    urls = ["http://127.0.0.1:3000/api?param=76f4b5319411de4f023d44eabb29c5b5"]

    for cadena in cadenas:
        hasher = Hasher(cadena)
        print("MD5:", hasher.hash_md5())
        urls.append(f"http://127.0.0.1:3000/api?param={hasher.hash_md5()}")
        # print("SHA1:", hasher.hash_sha1())
        # print("SHA256:", hasher.hash_sha256())
        # print("BLAKE2:", hasher.hash_blake2())
        # print("\n")
    # cadena = "password123"
    # hasher = Hasher(cadena)
    # print("MD5:", hasher.hash_md5())
    # print("SHA1:", hasher.hash_sha1())
    # print("SHA256:", hasher.hash_sha256())
    # print("BLAKE2:", hasher.hash_blake2())
    print(urls)
