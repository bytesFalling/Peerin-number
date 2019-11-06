#perrin number

def peerin( n ):
    if ( n== 0):
        return 3
    if (n == 1):
        return 0
    if (n == 2):
        return 2
    return peerin(n - 2) + peerin(n - 3)


# Main function
def main():
    n = int ( input ( "Enter positive interger: " ))
    if ( n < 0):
        print ( "Number needs to be positive")
        main()

    print(peerin(n))

main()
