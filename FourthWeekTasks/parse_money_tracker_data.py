import sys
 


class Converting:
    

    @staticmethod

    def ConvertTxtToList(file):
        with open(file,'r') as f:
            rows = []
            for r in f:
                rows.append(r) 


            return rows


