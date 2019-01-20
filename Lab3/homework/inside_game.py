def is_inside(x,y):
    toaDoX = float((x[0]-y[0])/y[2])
    toaDoY = float((x[1]-y[1])/y[3])
    if toaDoX >0 and toaDoX < 1 and toaDoY >0 and toaDoY<1:
        return True
    else:
        return False
print(is_inside([140, 30], [100, 60, 100, 200]))