if __name__ == '__main__':
    
    students = []

    secondLowest = []
    #CREATE NESTED LIST AND STORE 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        nameAndscore = [name,score]
                
        students.append(nameAndscore)
    
    # SORTED BY SCORE       
    sortedbyScore = sorted(students, key = lambda x: x[1])  
    
    for a in range(1):
        for i in range(1,len(sortedbyScore)):
            
            if sortedbyScore[a][1] < sortedbyScore[i][1]:
                
                secondLowest.append(sortedbyScore[i])
                
                break
            
    #IF SECOND LOWEST SCORE IN SORTEDBYSCORE ADD TO EMPTY LIST so to result  
    result = []
    for i in range(0,len(sortedbyScore)):
        
        if sortedbyScore[i][1] == secondLowest[0][1]:
            
            result.append(sortedbyScore[i])
            
            
    #SORT RESULT BY NAME              
    sortedbyName = sorted(result,key = lambda x: x[0])
    
    for i in range(len(sortedbyName)):
        
        print(sortedbyName[i][0])