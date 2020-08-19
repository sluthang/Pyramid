

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    choose = ''
    shapes = ["pyramid", "square", "triangle", "inverted_pyramid","diamond","k_shape"]
    while choose not in shapes:
        choose = input("Shape?: ").lower()
    return choose
    
    #return shape_param
                                                                                                                                                                                                                            

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = -1
    while height not in range(81):
        try:
            height = int(input("Height?: "))
        except:
            pass
    return height 
       # print("Invalid input , the range must be between 1-80")
        
   #else:
    #    return height_param 
                                

# TODO: Step 2
def draw_pyramid(height,outline):                                                                            
 if outline:   
       for i in range(1,height+1):
            for j in range(1,2*height):
                if (i==height or i+j==height+1) and i > 1:
                    print('*',end='')
                elif (j-i) == (height-1):
                    print('*',end='')
                    break
                else:
                    print(' ',end='')
            print()
               
        
 else :           
    for i in range(height):
            print(' ' * (height - i -1) + '*' *(2 *i + 1))
        

# TODO: Step 3
def draw_square(height, outline):
       
   
    if outline :
       for row in range(0,height):
           for col in range(0,height):
               if (row == 0 or row == height - 1 or col == 0 or col == height - 1):
                     print ('*',end ='')
               else :
                   print (' ',end = '')
           print()
    else :
        for i in range(0, height):
            print("*" * height)                     
    
# TODO: Step 4
def draw_triangle(height, outline):
    if outline:
  
        for i in range(0,height):
            for col in range(0,(i)):
                if i == 0 or col == 0 or i == height - 1 or col == height - 1:
                    print("*", end="")
                else :
                    print(end=" ")
            print("*")
        #print()

    else :
        for col in range(1,(height + 1)):
            print("*"* col)

def draw_inverted_pyramid(height,outline):
    if outline:
         for i in range(1,height+1):
            for j in range(1,2*height):
                if (i==height or i-j==height+1) and i < 1:
                    print('*',end='')
                elif (j+i) == (height+1):
                    print('*',end='')
                    break
                else:
                    print(' ',end='')
            print()  

    else :    
          for i in reversed(range(height)):
             print(' ' * (height - i - 1) + '*' * (2*i+1))            
      
def draw_diamond(height,outline):
    if outline:
        for i in range(1,height+1):
            for j in range(1,height-i+1):
                print(" ",end=" ")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print('*', end=' ')
                else:
                    print(' ',end="")
            #print()
        for i in range(height-1,0,-1):
            for j in range (1,height-i+1):
                print(' ',end=' ')
            for j in range(1,2*i):
                if j==1 or j==2*i-1:
                    print('*',end='')
            else:
                print(' ',end='')
        #print()
    else:    
        k = 2 * height -2
        for i in range(0,height):
             for j in range(0,k):
                 print(end=" ")
             k = k -1
             for j in range(0,i+1):
                 print("*",end=" ")
             print("")         
        k = height - 2
        for i in range(height, -1,-1):
            for j in range(k , 0 , -1):
                print(end=" ")
            k = k + 1
            for j in range(0,i + 1):
                print("*",end=" ")
            print("")     

def draw_k(height):
    for i in range(0,height+1):
      for j in range(0,height+1):
          if j == 0 or i - j == 3 or i + j == 3:
             print("*", end="")
          else:
             print(end=" ")
    print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
          draw_pyramid(height, outline)
    if shape == 'square':
          draw_square(height,outline)
    if shape == 'triangle':
          draw_triangle(height,outline) 
    if shape == 'inverted_pyramid':
          draw_inverted_pyramid(height,outline) 
    if shape == 'diamond' :
          draw_diamond(height,outline)  
    if shape == 'k_shape':
          draw_k(height)        
                        
     


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline_param = input("Outline only? (y/N):")
    if outline_param == 'y':
        return True
    else :    
        return False    

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

