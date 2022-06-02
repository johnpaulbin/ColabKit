import fileinput


class transcript:
    def __init__(self,
                 filename: str, 
    ):
        self.filename = filename


    def psfix(self, prefix="", suffix=""):

        """
        psfix (Prefix / Suffix) will add the specified prefix / suffix per line of the transcript.
        """
      
        for line in fileinput.input(self.filename, inplace=1):
            print(f'{prefix}{line.rstrip('\n')}{suffix}')