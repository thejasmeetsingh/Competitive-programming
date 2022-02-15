if __name__ == "__main__":
    result = "Case #{}: {} is ruled by {}."
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    
    T = int(input())
    
    for _ in range(T):
        kingdom_name = input()
        
        if kingdom_name[-1] == 'y' or kingdom_name[-1] == 'Y':
            print(result.format(_ + 1, kingdom_name, 'nobody'))
        else:
            print(result.format(
                    _ + 1, 
                    kingdom_name, 
                    'Alice' if kingdom_name[-1] in vowels else 'Bob'
                ))
