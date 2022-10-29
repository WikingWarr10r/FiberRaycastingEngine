keys = "qwertyuioplkjhgfdsazxcvbnm"

for i in range(0, len(keys) - 1):
    print(keys[i] + " = pygame.K_" + keys[i])