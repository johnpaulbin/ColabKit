import fileinput
from tqdm.notebook import tqdm
from g2p_en import G2p


class transcript:
    def __init__(self,
                 filename: str, 
    ):
        self.filename = filename
        self.g2p = G2p()

  
    def psfix(self, prefix="", suffix=""):
        """
        psfix (Prefix / Suffix) will add the specified prefix / suffix per line of the transcript.
        """
      
        for line in fileinput.input(self.filename, inplace=1):
            line = line.rstrip('\n')
            print(f'{prefix}{line}{suffix}')


    def arpa(self):
        """
        arpa will replace the text column of a LJSpeech-style transcript with its arpabet equivalent.
        """

      
        for idx, line in enumerate(tqdm(fileinput.input(self.filename, inplace=1))):
            line = line.rstrip().split("|")
            text = line[1]
            text = " ".join(
                [
                    f"{{{s.strip()}}}" if not any(s.strip() == i for i in list(",.!?@#$%^&*()")) else s.strip()
                    for s in " ".join(self.g2p(text)).split("  ")
                ]
            )
            print(f"{line[0]}|{text}{'|' + line[2] if len(line) == 3 else ''}")