from parse_money_tracker_data import Converting


class ConvertToDict:
    @staticmethod
    def create_dict(file):
    
    

        d = {}
        for el in Converting.ConvertTxtToList(file):
            if("===" in el):
                k =el[4:14]
                d[k] = []
                continue

            l = el.split(',')
            
            fin = []
            for el in l:

                if(el == l[2]):
                    el = el[0:len(el) - 1]

                fin.append(el)

            
            d[k].append(fin)
        return d

