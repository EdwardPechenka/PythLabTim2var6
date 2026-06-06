import os
from get_sum import get_sum

input_file = "numbers.txt"
output_file = "result.txt"

def main():
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = [float(x) for x in f.read().split()]
        
        total = get_sum(data)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Total result: {total}")
            
        print(f"Sum ({total}) has written in file {output_file}")

    except FileNotFoundError:
        print(f"Error, file {input_file} was not found")
    except ValueError as v_err:
        print(f"Error: the file has incorrect data. Details: {v_err}")
    except Exception as e:
        print(f"An unexpected error has occurred {e}")

if __name__ == "__main__":
    main()