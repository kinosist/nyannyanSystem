import json
from typing import Any


def load_json(path: str) -> Any:
    """
    JSONファイルを読み込んでPythonオブジェクトとして返す。

    副作用: 指定されたファイルパスからファイルを読み込む外部接続操作を行う。
    
    Args:
        path (str): 読み込み対象のJSONファイルのパス。

    Returns:
        Any: デコードされたPythonオブジェクト（通常はdictやlist）。
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: Any) -> None:
    """
    Pythonオブジェクトを整形されたJSONとして指定ファイルに保存する。

    副作用: 指定されたファイルパスにファイルを書き込む外部接続操作を行う。

    Args:
        path (str): 保存先のファイルパス。
        data (Any): 保存するPythonオブジェクト（通常はdictやlist）。
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
