"""
Main module to show one use case for the program.
"""

import gen_msg

def main():

    # Generate a random message signal.
    msg = gen_msg.gen_random_msg(20, seed=42)
    print(msg)
    

if __name__ == "__main__":
    main()