
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and strip any trailing whitespace (like newlines)
        words = set(line.strip().lower() for line in file)
    return words

def create_board(board_string, size=4):
    """
    Converts a string of letters into a 2D board of the specified size.
    For example, 'abcd efgh ijkl mnop' becomes:
    [['a', 'b', 'c', 'd'],
     ['e', 'f', 'g', 'h'],
     ['i', 'j', 'k', 'l'],
     ['m', 'n', 'o', 'p']]
    """
    letters = board_string.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    board = [list(letters[i:i+size]) for i in range(0, len(letters), size)]
    return board

def is_valid_position(x, y, size):
    """Check if the (x, y) position is within the bounds of the board."""
    return 0 <= x < size and 0 <= y < size

def dfs(board, dictionary, word, x, y, visited, size):
    """
    Perform DFS to find all valid words starting from the board[x][y] position.
    """
    # Check if the current word is in the dictionary and is at least 3 letters long
    if word in dictionary and len(word) >= 3:
        found_words.add(word)

    # Possible movements in 8 directions (including diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_position(new_x, new_y, size) and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            dfs(board, dictionary, word + board[new_x][new_y], new_x, new_y, visited, size)
            visited[new_x][new_y] = False  # Backtrack

def find_all_words(board, dictionary):
    """
    Find all words in the boggle board that are in the dictionary.
    """
    size = len(board)
    visited = [[False] * size for _ in range(size)]
    global found_words
    found_words = set()

    for i in range(size):
        for j in range(size):
            visited[i][j] = True
            dfs(board, dictionary, board[i][j], i, j, visited, size)
            visited[i][j] = False

    return found_words
board = input("What does the boggle board look like? (4*4)")
boggle_board = create_board(board)
dictionary = load_dictionary('dictionary.txt')
found_words = find_all_words(boggle_board, dictionary)
print(f"Words found: {found_words}")
