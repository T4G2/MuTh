from typing import Optional

class Localization:
    def __init__(self, path: Optional[str] = None) -> None:
        self.dict = None
        if path is not None:
            self.load(path)

    def load(self, file_path: str) -> bool:
        new_dict = {}
        success = False
        with open(file_path, 'r') as f:
            # For now only 1 Liners can be open
            for line in f:
                if line.strip() == "":
                    continue
                splitted = line.split(sep=' ', maxsplit=1)
                if len(splitted) != 2:
                    success = False
                    return success
                new_dict[splitted[0]] = splitted[1]

            self.dict = new_dict
            success = True
        
        return success
    
    def get(self, str_name: str) -> str:
        item = self.dict.get(str_name)

        return f'[null: {str_name}]' if item is None else item
                    
        