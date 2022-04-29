from typing import List, Dict, Union, Optional, List

StandardRow = Tuple[str, int]
SpecialRow = Tuple[int, str]
ItemRow = Union[StandardRow, SpecialRow]
ItemMapping = Dict[str, List[ItemRow]]
