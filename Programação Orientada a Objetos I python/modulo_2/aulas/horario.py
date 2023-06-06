class Horario:
    '''
    classe pra representar um horario com hora, minuto e segundo
    '''
    
    def __init__(self, hour, minute, sec):
        
        self.h = hour
        self.m = minute
        self.s = sec
        
        
    def __repr__(self):
        
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
    
    
    def __str__(self):
        
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
            
    
    def __add__(self, other):
        
        ho = self.h + other.h
        mi = self.m + other.m
        se = self.s + other.s

        while se >= 60:
            mi = mi + 1
            se = se - 60

        while mi >= 60:
            ho = ho + 1
            mi = mi - 60

        while ho >= 24:
            ho = ho - 24

        return Horario(ho, mi, se)
    
    
    def __gt__(self, other):
        
        if self.h > other.h:
            
            return True
        
        elif self.h == other.h and self.m > other.m:
            
            return True
        
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            
            return True
        
        else:
            
            return False
    