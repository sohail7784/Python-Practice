
def minon_game(string):
    kevin=0 # here create a varaible called kevin count starts from zer
    staurt=0 
    vowels="aeiou" # create a varaible on vowels to detects wheather this type of character are in word

    for i in range(len(string)): # started the loop
        points=len(string) - i # converted into the index and subtracted from the loop
        if string[i] in vowels: # converted index
            kevin+=points # added the point + in case of vowels exits
        else:
            staurt+=points # added on consonents
    if staurt>kevin:
        print("staurt winner",staurt)
    elif kevin>staurt:
        print("kevin winner",kevin)
    else:
        print("drwa")
if __name__ == '__main__':
    s=input()
    minon_game(s)
