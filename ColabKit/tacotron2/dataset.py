import pickle
from torch.utils.data import DataLoader
from tqdm.notebook import tqdm


class dataset:
    def __init__(self,
                transcript: str):
        self.transcriptPath = transcript


    def pickle(self, 
               file_name = "picklized_dataset.pkl",
               batch_size: int = 14, 
               compute_gst = None, 
               symbol_set: str = "nvidia_taco2", 
               text_cleaners: list = ["english_cleaners"],
               sampling_rate: int = 22050,
               arpabet: float = 1.0,
               shuffle = True):
        """
        pickle will serialize a dataset
        """

        try:
            from uberduck_ml_dev.data_loader import TextMelDataset, TextMelCollate
        except ImportError:
            print("Unable to run pickle function, as uberduck_ml_dev is not installed in your system. You can do so via: pip install git+https://github.com/uberduck-ai/uberduck-ml-dev.git")
            return

        print(f"""
            Beginning pickle with configuration:
              
            file name: {file_name}
            batch_size: {batch_size}
            compute_gst: {compute_gst}
            symbol_set: {symbol_set}
            text_cleaners: {text_cleaners}
            sampling_rate: {sampling_rate}
            arpabet: {arpabet}
            shuffle: {shuffle}
             """)

        def training_dataset_args():
            return {
                "audiopaths_and_text": self.transcriptPath,
                "text_cleaners": text_cleaners,
                "p_arpabet": arpabet,
                "n_mel_channels": 80,
                "sampling_rate": sampling_rate,
                "mel_fmin": 0,
                "mel_fmax": 8000,
                "filter_length": 1024,
                "hop_length": 256,
                "win_length": 1024,
                "symbol_set": symbol_set,
                "max_wav_value": 32768.0,
                "pos_weight": 10,
                "compute_gst": compute_gst,
            }
        
        train_set = TextMelDataset(
                    **training_dataset_args(),
                    debug=False,
                    debug_dataset_size=batch_size,
                )
                 
        collate_fn = TextMelCollate(
                    n_frames_per_step=1, include_f0=False
                )
                 
        train_loader = DataLoader(
                    train_set,
                    batch_size=batch_size,
                    shuffle=shuffle,
                    sampler=None,
                    collate_fn=collate_fn,
                )

        data = []
        for idx, v in enumerate(tqdm(train_loader)):
            data.append(v)

        with open(file_name, "wb") as f:
            pickle.dump(data, f)

        print("Pickle finished, file saved as:", file_name)
        return