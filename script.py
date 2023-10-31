# Define a function to count the number of matches between two sequences
def count_matches(seq1, seq2):
  # Initialize a counter for matches
  count = 0
  # Iterate through the sequences up to the length of the shorter sequence
  for i in range(min(len(seq1), len(seq2))):
    # Increment the counter if elements at the current position match
    if seq1[i] == seq2[i]:
      count += 1
  return count

# Define a function to find the maximum contiguous chain of matches between two sequences
def max_chain(seq1, seq2):
  # Initialize variables for the maximum and current chain lengths
  max_len = 0
  cur_len = 0
  # Iterate through the sequences up to the length of the shorter sequence
  for i in range(min(len(seq1), len(seq2))):
    # If elements at the current position match, increment the current chain length and update the maximum chain length
    if seq1[i] == seq2[i]:
      cur_len += 1
      max_len = max(max_len, cur_len)
    else:
      # Reset the current chain length if elements don't match
      cur_len = 0
  return max_len

# Define a function to shift a sequence by a given amount
def shift(seq, n):
  # Add n spaces at the beginning of the sequence and remove n characters from the end
  return " " * n + seq[:-n]

# Define a function to find the optimal alignment of two sequences that maximizes the number of matches or the maximum contiguous chain, depending on the mode
def align(seq1, seq2, mode, max_shift):
  # Initialize variables for the best score and alignment
  best_score = 0
  best_align = ("", "")
  # Iterate through shifts up to the maximum shift
  for n in range(max_shift + 1):
    # Shift the sequences
    shifted_seq1 = shift(seq1, n)
    shifted_seq2 = shift(seq2, n)
    # Calculate score based on the chosen mode
    if mode == "matches":
      score = count_matches(shifted_seq1, shifted_seq2)
    elif mode == "chain":
      score = max_chain(shifted_seq1, shifted_seq2)
    else:
      raise ValueError("Invalid mode")
    # Update the best score and alignment if the current score is higher
    if score >= best_score:
      best_score = score
      best_align = (shifted_seq1, shifted_seq2)
  return (best_score, best_align)

# Define a function to display an alignment of two sequences with matching nucleotides highlighted in red
def display_alignment(seq1, seq2):
  # Initialize an empty output string
  output = ""
  # Iterate through the sequences
  for i in range(min(len(seq1), len(seq2))):
    # If elements at the current position match, highlight in red
    if seq1[i] == seq2[i]:
      output += "\033[91m" + seq1[i] + "\033[0m" 
    else:
      # If elements don't match, add a space
      output += seq1[i] + " " 
    output += " " 
  output += "\n" 
  # Add the second sequence with spaces
  for i in range(max(len(seq1), len(seq2))):
    output += seq2[i] + " " 
  output += "\n" 
  return output

# Define a function to read a sequence from a file and return it as a string
def read_sequence(filename):
  # Read the contents of the file and remove unwanted characters
  with open(filename, "r") as f:
    contents = f.read()
  return contents.replace(" ", "").replace("\n", "").replace("\t", "")

# Define a function to display a menu of options for the user and return their choice as an integer
def display_menu():
  print("\n\033[92m====================================\033[0m")
  print("\033[92mDNA Similarity Calculator\033[0m")
  print("\033[92m====================================\033[0m \n")
  print("Please select one of the following options:")
  print("1. Set user defined maximum shift")
  print("2. Calculate and display the count of matches without any shifts done")
  print("3. Calculate and display the maximum contiguous chain without any shifts done")
  print("4. Calculate and display the optimal alignment of two sequences that maximizes the number of matches")
  print("5. Calculate and display the optimal alignment of two sequences that maximizes the maximum contiguous chain")
  print("6. Exit the program\n")
  
  try:
    choice = int(input("Enter your choice: "))
  except:
    choice = None
  # Get user input for their choice and return it as an integer
  return choice

# Define a function to validate the input mode and return the sequences
def get_sequences(input_mode):
  # Get sequences based on user input mode (console or file)
  if input_mode == "c":
    seq1 = input("Enter sequence 1: ")
    seq2 = input("Enter sequence 2: ")
  elif input_mode == "f":
    filename1 = input("Enter filename for sequence 1: ")
    filename2 = input("Enter filename for sequence 2: ")
    seq1 = read_sequence(filename1)
    seq2 = read_sequence(filename2)
  else:
    raise ValueError("Invalid input mode")
  return (seq1, seq2)

# Define a function to perform option 1: Set user defined maximum shift
def option_1():
  # Get user input for the maximum shift and validate it
  max_shift = int(input("Enter a positive integer for the maximum shift: "))
  if max_shift < 0:
    raise ValueError("Maximum shift must be positive")
  print(f"Maximum shift set to {max_shift}")
  return max_shift

# Define a function to perform option 2: Calculate and display the count of matches without any shifts done
def option_2():
  # Get user input for input mode (console or file)
  input_mode = input("Enter 'c' for console input or 'f' for file input: ")
  seq1, seq2 = get_sequences(input_mode)
  # Calculate and display the count of matches without shifts
  matches = count_matches(seq1, seq2)
  print(f"The number of matches without any shifts done is {matches}")

# Define a function to perform option 3: Calculate and display the maximum contiguous chain without any shifts done
def option_3():
  # Get user input for input mode (console or file)
  input_mode = input("Enter 'c' for console input or 'f' for file input: ")
  seq1, seq2 = get_sequences(input_mode)
  # Calculate and display the maximum contiguous chain without shifts
  chain = max_chain(seq1, seq2)
  print(f"The maximum contiguous chain without any shifts done is {chain}")

# Define a function to perform option 4: Calculate and display the optimal alignment of two sequences that maximizes the number of matches
def option_4(max_shift):
  if max_shift is None:
    print("Please set the user defined maximum shift first")
    return None
  else:
    # Get user input for input mode (console or file)
    input_mode = input("Enter 'c' for console input or 'f' for file input: ")
    seq1, seq2 = get_sequences(input_mode)
    # Calculate and display the optimal alignment based on matches
    score, alignment = align(seq1, seq2, "matches", max_shift)
    print(f"The optimal alignment of the sequences that maximizes the number of matches is:")
    print(display_alignment(*alignment))
    print(f"The number of matches in this alignment is {score}")

# Define a function to perform option 5: Calculate and display the optimal alignment of two sequences that maximizes the maximum contiguous chain
def option_5(max_shift):
  if max_shift is None:
    print("Please set the user defined maximum shift first")
    return None
  else:
    # Get user input for input mode (console or file)
    input_mode = input("Enter 'c' for console input or 'f' for file input: ")
    seq1, seq2 = get_sequences(input_mode)
    # Calculate and display the optimal alignment based on maximum contiguous chain
    score, alignment = align(seq1, seq2, "chain", max_shift)
    print(f"The optimal alignment of the sequences that maximizes the maximum contiguous chain is:")
    print(display_alignment(*alignment))
    print(f"The maximum contiguous chain in this alignment is {score}")

# Define a function to perform option 6: Exit the program
def option_6():
  print("Thank you for using DNA Similarity Calculator!\n")
  return False

# Define a function to run the main logic of the program
def main():
  # Initialize the maximum shift to None and set the program running
  max_shift = None
  running = True
  while running:
    # Display the menu and get the user's choice
    choice = display_menu()
    # Define a dictionary of actions for each menu choice
    actions = {1: option_1, 
               2: option_2, 
               3: option_3, 
               4: option_4, 
               5: option_5, 
               6: option_6}
    
    # Check if the user's choice is valid and execute the corresponding function
    if choice in actions:
        try:
            func = actions[choice]
            if choice == 4 or choice == 5:
                if max_shift is None:
                    print("Please set the user defined maximum shift first")
                    continue
                result = func(max_shift)
            else:
                result = func()
        except Exception as e:
            print(f"\033[91m An error occurred: {e} \033[0m")
        finally:
             if choice == 1:
                 max_shift = result
             elif choice == 6:
                 running = result
    else:
      # Display an error message for invalid choices
      print("\033[91m Invalid choice. Please enter a number between 1 and 6 \033[0m")

# Run the main function if this script is executed
if __name__ == "__main__":
  main()