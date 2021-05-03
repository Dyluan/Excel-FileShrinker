import pandas as pd

class Shrink:

    def __init__(self, filename, path_to_file, step):

        if path_to_file[-1:] != '\\':
            self.path_to_file = path_to_file + '\\'
        
        else:
            self.path_to_file = path_to_file

        self.file = self.path_to_file + filename
        self.step = step
        self.file_format = filename.split('.')[-1]

        self.go()
    
    def go(self):
        
        if 'csv' in self.file_format:

            df = pd.read_csv(self.file, sep=';', encoding='utf-8')
            csv_reader = 1
        
        else:
            df = pd.read_excel(self.file)
            csv_reader = 0

        file_size = len(df)

        cp = 1

        for i in range(1, file_size, self.step):

            #opens the file, skipping the first i elements and keeping the rest
            if csv_reader:
                df = pd.read_csv(self.file, sep=';', encoding='utf-8', skiprows=range(1, i))
            
            else:
                df = pd.read_excel(self.file, skiprows=range(1, i))

            #saving the content of the first step elements of the frame into another frame
            newFrame = df.head(self.step)
            new_file = self.file[:-4] + '_' + str(cp) + '.' + self.file_format

            if csv_reader:
                newFrame.to_csv(new_file, sep=';', index=False)
            
            else:
                newFrame.to_excel(new_file, index=False)

            cp += 1

s = Shrink('admin.xls', 'C:\\Users\\Dylan\\Documents\\python\\django\\apprendre\\mysite\\appartements\\aliloca\\festirent', 100)