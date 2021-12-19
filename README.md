# Flight-Data-Analyzer
This is a flight analyzer script in Python for the post mission data analysis at Space Technology Lab
if len(output) == 6:
                print(output)
                for i in range(0,10):
                    #print('For i in range: ',i)
                    if output[i] == '.':
                        #print(output[i+1:i+3])
                        if i == 4:
                            output = output[2:i+4]
                            print(output)
                        elif i == 5:
                            output = output[2:i+4]
                            print(output)